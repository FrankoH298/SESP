import React from "react";

const Login = () => {
  return (
    <>
      <form>
        <div Name="row" style={{ marginTop: "5rem" }}>
          <div className="container">
            <div Name="col s12 m6">
              <div className="input-field col s12">
                <input id="email" type="email" className="validate" />
                <label for="email">Email</label>
              </div>
              <div className="input-field col s12">
                <input id="password" type="password" className="validate" />
                <label for="password">Contraseña</label>
              </div>
            </div>
            <button class="waves-effect waves-light btn red">
              Inciar Sesión
            </button>
          </div>
        </div>
      </form>
    </>
  );
};

export default Login;
