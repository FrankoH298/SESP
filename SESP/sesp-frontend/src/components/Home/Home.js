import "materialize-css/dist/css/materialize.css";

import { useEffect } from "react";
import Card from "../UI/Card";

function Home() {
  useEffect(() => {
    let socket = new WebSocket("ws://localhost:8000/ws/inicio/");
    socket.onmessage = function (event) {
      document.querySelector("#dummy-title").innerText = event.data;
    };
    socket.onopen = function (event) {
      socket.send(1);
    };
    socket.onclose=function(event){
      setTimeout(connect, 5000); //re-connect after 5 seconds
    }
  });
  return (
    <>
      <div className="container">
        <div className="row">
          <Card />
          <Card />
          <Card />
        </div>
      </div>
    </>
  );
}

export default Home;
