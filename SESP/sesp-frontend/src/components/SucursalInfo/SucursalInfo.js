import React from "react";
import { useEffect } from "react";
import ChartStats from "../ChartStats/ChartStats";

const SucursalInfo = (props) => {
  useEffect(() => {
    let socket = new WebSocket("ws://localhost:8000/ws/inicio/");
    socket.onmessage = (event) => {
      let datos = JSON.parse(event.data);
    };
    socket.onopen = () => {
      socket.send(1);
    };
    socket.onclose = () => {
      setTimeout(function () {
        socket = new WebSocket("ws://localhost:8000/ws/inicio/");
      }, 3000);
    };
  });
  return (
    <>
      {/* <!-- Page Layout here --> */}
      <div className="row">
        <div className="col s12 m8 l8">
          <div className="row">
            <div className="col s12 m12">
              {/* <!-- Carta Principal --> */}
              <div className="card">
                <div className="card-content">
                  <div className="center-align">
                    <h3 style={{ margin: "0px" }}>Falabella</h3>
                  </div>
                </div>
                <div className="card-action teal center-align">
                  <div className="row">
                    <div className="col s6">
                      <h5 className="white-text">Capacidad Maxima</h5>
                      <h2 className="white-text" style={{ margin: "0px" }}>
                        1000 {/* {{ store.max_people }} */}
                      </h2>
                    </div>
                    <div className="col s6">
                      <h5 className="white-text">Personas Actuales</h5>
                      <h2 className="white-text" style={{ margin: "0px" }}>
                        500 {/* {{ store.actual_people }} */}
                      </h2>
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
