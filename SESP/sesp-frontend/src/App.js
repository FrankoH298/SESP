import "./App.css";

import Navbar from "./components/Navbar/Navbar";
import Home from "./components/Home/Home";
import ChartStats from "./components/ChartStats/ChartStats";
import "materialize-css/dist/css/materialize.css";

function App() {
  return (
    <>
      <Navbar />
      <h1 className="dummy-title" id="dummy-title">
        Hola
      </h1>
      <Home />
      <ChartStats />
    </>
  );
}

export default App;
