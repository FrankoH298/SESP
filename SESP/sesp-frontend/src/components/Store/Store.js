import React from "react";
import { useEffect, useState } from "react";
import ChartStats from "../ChartStats/ChartStats";
import { useLocation } from "react-router-dom";

function Store(){
  const location = useLocation();
  const [store, setStore] = useState([]);
  const storeProps = location.state?.storeProps;
  let socket = null;

  let createSocket = () => {
    socket = new WebSocket("ws://localhost:8000/ws/inicio/");
    socket.onmessage = (event) => {
      let datos = JSON.parse(event.data);
      console.log(datos.key_value)
      setStore(datos.key_value);
      storeProps.actualPeople = datos.key_value.actual_people;
      storeProps.maxPeople = datos.key_value.max_people;
      storeProps.name = datos.key_value.name;
      storeProps.telephoneNumber = datos.key_value.telephone_number;
      storeProps.isFull = datos.key_value.is_full;
      console.log(storeProps)
    };
    socket.onopen = () => {
      socket.send(storeProps.id);
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
  },[]);
  return (
    <>
      {/* <!-- Page Layout here --> */}
      <div className="container">
        <div className="row center" >
          <div className="col s12">
            <div className="row">
              <div className="col s12 m12">
                {/* <!-- Carta Principal --> */}
                <div className="card">
                  <div className="card-content">
                    <div  className="center-align">
                      <h3 style={{ margin: "0px" }} >{store.name}</h3>
                    </div>
                  </div>
                  <div className="card-action teal center-align">
                    <div className="row">
                      <div className="col s4">
                        <h5 className="white-text">Capacidad Maxima</h5>
                        <h2 className="white-text"style={{ margin: "0px" }}>
                          {store.max_people}
                        </h2>
                      </div>

                      <div className="col s4">
                        <h5 className="white-text">Personas Actuales</h5>
                        <h2 className="white-text"style={{ margin: "0px" }}>
                          {store.actual_people}
                        </h2>
                      </div>
                      <div className="col s4">
                        <h5 className="white-text">Telefono</h5>
                        <h2 className="white-text"style={{ margin: "0px" }}>
                          {store.telephone_number}
                        </h2>
                      </div>
                    </div>
                  </div>
                  <div
                    className={
                      "card-action" +
                      (store.is_full ? " red " : " green ") +
                      "center-align"
                    }
                  >
                    <h2
                      className="white-text center-align"
                      style={{ margin: "0px" }}
                    >
                      {store.is_full
                        ? "Lleno, no puedes pasar"
                        : "Puedes pasar"}
                    </h2>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <ChartStats store={storeProps} />
    </>
  );
};

export default Store;
