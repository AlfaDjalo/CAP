import ollama

res = ollama.generate(
    model="gemma3:1b",
    # prompt="Hello."
    prompt="Who were the best Aussie rock bands of the 80s and 90s ?"
)

print(res["response"])