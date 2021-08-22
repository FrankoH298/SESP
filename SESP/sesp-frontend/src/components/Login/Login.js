import React from "react";

const Login = () => {
  return (
    <>
      <form method="POST" action="/logi">
        <div className="row" style={{ marginTop: "5rem" }}>
          <div className="container">
            <div className="col s12 m6">
              <div className="input-field col s12">
                <input id="email" type="email" className="validate" />
                <label htmlFor="email">Email</label>
              </div>
              <div className="input-field col s12">
                <input id="password" type="password" className="validate" />
                <label htmlFor="password">Contraseña</label>
              </div>
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
