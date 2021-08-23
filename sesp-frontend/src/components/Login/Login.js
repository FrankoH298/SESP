import React from "react";
import { useState } from "react";
import { useHistory } from "react-router-dom";
import axios from "axios";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

const Login = () => {
  let history = useHistory();

  function setToken(idToken) {
    localStorage.setItem("id_token", idToken);
  }

  const [error, setError] = useState(null);
  const [username, setUsername] = useState();
  const [password, setPassword] = useState();
  function handleChangePassword(event) {
    setPassword(event.target.value);
  }
  function handleChangeUsername(event) {
    setUsername(event.target.value);
  }
  function submitHandler(event) {
    const data = { username: username, password: password };
    event.preventDefault();
    axios
      .post("/api-token-auth/", data)
      .then((response) => {
        setToken(response.data["token"]);
        history.go(-1);
      })
      .catch((error) => {
        console.log(error);
        setError(error.response.status);
      });
  }
  return (
    <>
      <form onSubmit={submitHandler}>
        <div className="row" style={{ marginTop: "5rem" }}>
          <div className="container">
            <div className="col s12 m6">
              <div className="input-field col s12">
                <input
                  id="username"
                  name="username"
                  type="text"
                  className="validate"
                  onChange={handleChangeUsername}
                />
                <label htmlFor="username">Username</label>
              </div>
              <div className="input-field col s12">
                <input
                  id="password"
                  type="password"
                  className="validate"
                  onChange={handleChangePassword}
                />
                <label htmlFor="password">Contraseña</label>
              </div>
              {error === 400 ? (
                <div className="col s-12">
                  <div className="card red darken-2">
                    <div className="card-content">
                      <p className="white-text">
                        Datos Incorrectos, por favor intente de nuevo.
                      </p>
                    </div>
                  </div>
                </div>
              ) : (
                ""
              )}
            </div>
            <button className="waves-effect waves-light btn red">
              Inciar Sesión
            </button>
          </div>
        </div>
      </form>
    </>
  );
};

export default Login;
