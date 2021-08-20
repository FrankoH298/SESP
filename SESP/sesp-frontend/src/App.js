import "./App.css";
import React, { useState, useEffect } from "react";
import Navbar from "./components/Navbar/Navbar";
import Home from "./components/Home/Home";
import ChartStats from "./components/ChartStats/ChartStats";
import "materialize-css/dist/css/materialize.css";

function App() {
  const [counterText, setCounterText] = useState("Hola");

  useEffect(() => {
    const socket = new WebSocket("ws://localhost:8000/ws/inicio/");
    socket.onmessage = (event) => {
      setCounterText(event.data);
    };
    socket.onopen = () => {
      socket.send(1);
    };
    // socket.onclose=function(event){
    //   setTimeout(connect, 5000); //re-connect after 5 seconds
    // }
  });

  return (
    <>
      <Navbar />
      <h1 className="dummy-title" id="dummy-title">
        {counterText}
      </h1>
      <Home />
    </>
  );
}

export default App;
