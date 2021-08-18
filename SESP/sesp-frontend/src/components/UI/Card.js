import React from 'react'

const Card = () => {
  return (
    <>
      <div class="col s12 m4">
        <div class="card">
          <div class="card-image">
            <img src="https://imgar.zonapropcdn.com/avisos/1/00/47/84/52/07/720x532/1765845046.jpg" alt='card-img' /> {/* Imagen del local */}
            <span class="card-title">Card Title</span> {/* Nombre del local */}
          </div>
          <div class="card-content">
            <p>I am a very simple card. I am good at containing small bits of information.
            I am convenient because I require little markup to use effectively.</p> {/* Descripcion del local */}
          </div>
          <div class="card-action">
            <a href="/">Mas Inforamción</a>
          </div>
        </div>
      </div>
    </>
  )
}

export default Card
