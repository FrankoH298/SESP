import "materialize-css/dist/css/materialize.css";

import { useEffect } from "react";
import Card from "../UI/Card";

function Home() {
  useEffect(() => {
    let socket = new WebSocket("ws://localhost:8000/ws/inicio/");
    socket.onmessage = function (event) {
      let data = event.data;
      document.querySelector("#data").innerText = data;
    };
  });
  return (
    <>
      <a id="data" href='/'> text </a>
      <div className='container'>
        <div className='row'>
          <Card />
          <Card />
          <Card />    
        </div> 
      </div>
    </>
  );
}

export default Home;
