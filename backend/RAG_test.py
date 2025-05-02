# from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.document_loaders import OnlinePDFLoader

from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_ollama import ChatOllama

from langchain_core.runnables import RunnablePassthrough
from langchain.retrievers.multi_query import MultiQueryRetriever

import ollama

doc_path = "../data/CAP_Game_Guide.pdf"
model = "deepseek-r1:7b"
# model = "deepseek-llm:7b"
# model = "gemma3:1b"

if doc_path:
    loader = PyMuPDFLoader(file_path=doc_path)
    # loader = UnstructuredPDFLoader(file_path=doc_path)
    data = loader.load()
    print("done loading...")
else:
    print("upload a PDF file")

# content = data[0].page_content
# print(content[:100])

# Split and chunk
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1200, chunk_overlap=300)
chunks = text_splitter.split_documents(data)
print("done splitting...")

# print(f"Number of chunks: {len(chunks)}")
# print(f"Example chunk: {chunks[0]}")

# Add to vector database
ollama.pull("nomic-embed-text")

vector_db = Chroma.from_documents(
    documents=chunks,
    embedding=OllamaEmbeddings(model="nomic-embed-text"),
    collection_name="simple-rag"
)
print("done adding to vector database...")

# Retrieval
llm = ChatOllama(model=model)

QUERY_PROMPT = PromptTemplate(
    input_variables=["question"],
    template="""You are an AI language model assistant specialising in exotic poker variants.
    Your task is to generate five different versions of the given user question to retrieve
    relevant documents from a vector database. By generating multiple perspectives on the user 
    question, your goal is to help the user overcome some of the limitations of the distance-based 
    similarity search. Provide these alternative questions separated by newlines.
    Original question: {question}"""
    # template="""You are an AI language model assistant. Your task is to generate five 
    # different versions of the given user question to retrieve relevant documents from
    # a vector database. By generating multiple perspectives on the user question, your
    # goal is to help the user overcome some of the limitations of the distance-based 
    # similarity search. Provide these alternative questions separated by newlines.
    # Original question: {question}"""
)

retriever = MultiQueryRetriever.from_llm(
    vector_db.as_retriever(), llm, prompt=QUERY_PROMPT
)

# RAG prompt
template = """Answer the question based ONLY on the following context
{context}
Question: {question}
"""

prompt = ChatPromptTemplate.from_template(template)

chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# res = chain.invoke(input=("Hello"))
res = chain.invoke(input=("How is the best low hand determined ?"))

print(res)