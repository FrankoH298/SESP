import "./App.css";
import React from "react";
import Navbar from "./components/Navbar/Navbar";
import Home from "./components/Home/Home";
import SucursalInfo from "./components/SucursalInfo/SucursalInfo";
import "materialize-css/dist/css/materialize.css";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Login from "./components/Login/Login";

function App() {
  return (
    <>
      <Router>
        <Navbar />
        <Switch>
          <Route path="/sucursal-info/" component={SucursalInfo} />
          <Route path="/login/" component={Login} />
          <Route path="/" component={Home} exact />
        </Switch>
      </Router>
    </>
  );
}

export default App;
