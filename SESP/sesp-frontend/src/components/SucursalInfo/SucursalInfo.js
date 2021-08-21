import React from "react";
import { useEffect } from "react";
import ChartStats from "../ChartStats/ChartStats";
import { useLocation } from "react-router-dom";

const SucursalInfo = () => {
  const location = useLocation();
  const sucursalProps = location.state?.sucursalProps;
  let socket = null;

  let createSocket = () => {
    socket = new WebSocket("ws://localhost:8000/ws/inicio/");
    socket.onmessage = (event) => {
      let datos = JSON.parse(event.data);
      document.getElementById("sucursalPeople").innerText = datos.key_value;
    };
    socket.onopen = () => {
      socket.send(sucursalProps.id);
    };
    socket.onclose = () => {
      setTimeout(() => {
        socket = null;
        createSocket();
      }, 3000);
    };
  };
  useEffect(() => {
    createSocket();

    return () => {
      socket.onclose = () => {}; // disable onclose handler first
      socket.close();
    };
  });
  return (
    <>
      {/* <!-- Page Layout here --> */}
      <div className="row" style={{ marginTop: "2rem" }}>
        <div className="container">
          <div className="col s12">
            <div className="row">
              <div className="col s12 m12">
                {/* <!-- Carta Principal --> */}
                <div className="card">
                  <div className="card-content">
                    <div className="center-align">
                      <h3 style={{ margin: "0px" }}>{sucursalProps.title}</h3>
                    </div>
                  </div>
                  <div className="card-action teal center-align">
                    <div className="row">
                      <div className="col s6">
                        <h5 className="white-text">Capacidad Maxima</h5>
                        <h2 className="white-text" style={{ margin: "0px" }}>
                          {sucursalProps.maxAmount}
                        </h2>
                      </div>
                      <div className="col s6">
                        <h5 className="white-text">Personas Actuales</h5>
                        <h2
                          className="white-text"
                          id="sucursalPeople"
                          style={{ margin: "0px" }}
                        >
                          {sucursalProps.people}
                        </h2>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <ChartStats />
    </>
  );
};

export default SucursalInfo;
