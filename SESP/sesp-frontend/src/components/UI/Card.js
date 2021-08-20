import React from "react";

const Card = (props) => {
  return (
    <>
      <div className="col s12 m4">
        <div className="card">
          <div className="card-image">
            <img
              src="https://imgar.zonapropcdn.com/avisos/1/00/47/84/52/07/720x532/1765845046.jpg"
              alt="card-img"
            />{" "}
            {/* Imagen del local */}
            <span className="card-title">{props.title}</span>{" "}
            {/* Nombre del local */}
          </div>
          <div className="card-content">
            <p>Cantidad Maxima: {props.maxAmount}</p>
            <p>Personas en el local: {props.people}</p>
            <p>Teléfono: {props.phone}</p>
          </div>
          <div className="card-action">
            <a href="/">Mas Inforamción</a>
          </div>
        </div>
      </div>
    </>
  );
};

export default Card;
