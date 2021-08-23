import React from "react";
import { Link } from "react-router-dom";
import Background from "./static/background.jpeg";

const Card = (props) => {
  return (
    <>
      <div className="col s12 m6 l6">
        <div className="card">
          <div className="card-image waves-effect waves-block waves-light">
            <img className="activator" src={Background} />{" "}
          </div>
          <div className="card-content">
            <span className="card-title activator grey-text text-darken-4">
              {props.name}
              <i className="material-icons right">more_vert</i>
            </span>
            <Link
              className="teal-text"
              to={{
                pathname: "/store/",
                state: { storeProps: props },
              }}
            >
              Más Información
            </Link>
          </div>
          <div className="card-reveal">
            <span className="card-title grey-text text-darken-4">
              {props.name}
              <i className="material-icons right">close</i>
            </span>
            <p>Cantidad Máxima: {props.maxPeople}</p>
            <p>Personas en el local: {props.actualPeople}</p>
            <p>Teléfono: {props.telephoneNumber}</p>
            <p>Dirección: {props.address}</p>
          </div>
        </div>
      </div>
    </>
  );
};

export default Card;
