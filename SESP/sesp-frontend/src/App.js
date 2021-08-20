import "./App.css";
import React, { useState, useEffect } from "react";
import Navbar from "./components/Navbar/Navbar";
import Home from "./components/Home/Home";
import "materialize-css/dist/css/materialize.css";

function App() {

  return (
    <>
      <Navbar />
      <Home />
    </>
  );
}

export default App;
