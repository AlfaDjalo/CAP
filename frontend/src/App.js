// import './App.css';
import Navbar from "./Navbar";
import Home from "./Home";
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

function App() {
  // const title = "Welcome to CAP"; // Removed unused variable
  const link = "https://github.com/AlfaDjalo/crazy-asian-poker-game-guide"
  return (
    <Router>
      <div className="App">
        <Navbar />
        <div className="Content">
          <Routes>
            <Route path="/" element={<Home />} />
          </Routes>
        </div>
        <a href={ link }>Github repo</a>
      </div>
    </Router>
  );
}

export default App;
