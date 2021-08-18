import "materialize-css/dist/css/materialize.css";

import { useEffect } from "react";

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
      <a id="data"> text </a>
    </>
  );
}

export default Home;
