import React from "react";
import { Link } from "react-router-dom";

const Card = (props) => {
  return (
    <>
      <div className="col s12 m6 l6">
        <div className="card">
          <div className="card-image">
            <img
              src="https://imgar.zonapropcdn.com/avisos/1/00/47/84/52/07/720x532/1765845046.jpg"
              alt="card-img"
            />{" "}
            {/* Imagen del local */}
            <span className="card-title">{props.name}</span>{" "}
            {/* Nombre del local */}
          </div>
          <div className="card-content">
            <p>Cantidad Maxima: {props.maxPeople}</p>
            <p>Personas en el local: {props.actualPeople}</p>
            <p>Teléfono: {props.telephoneNumber}</p>
          </div>
          <div className="card-action">
            <Link
              to={{
                pathname: "/store/",
                state: { storeProps: props },
              }}
            >
              Mas Información
            </Link>
          </div>
        </div>
      </div>
    </>
  );
};

export default Card;
