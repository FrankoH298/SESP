import "./App.css";
import React, { useState, useEffect } from "react";
import Navbar from "./components/Navbar/Navbar";
import Home from "./components/Home/Home";
import SucursalInfo from "./components/SucursalInfo/SucursalInfo"
import ChartStats from "./components/ChartStats/ChartStats"
import "materialize-css/dist/css/materialize.css";

function App() {

  return (
    <>
      <Navbar />
      <Home />
      <SucursalInfo />
      <ChartStats />
    </>
  );
}

export default App;
