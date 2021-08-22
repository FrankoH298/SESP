import "materialize-css/dist/css/materialize.css";
import { useEffect } from "react";
import { Link } from "react-router-dom";
import M from "materialize-css";

const Navbar = () => {
  useEffect(() => {
    let elems = document.querySelectorAll(".sidenav");
    M.Sidenav.init(elems);
    elems = document.querySelectorAll(".dropdown-trigger");
    M.Dropdown.init(elems);
  });

  return (
    <>
      <ul id="dropdown1" className="dropdown-content">
        {/* <li><a href="/"><i className="material-icons top">account_circle</i>Perfil</a></li> */}
        {/* <li><a href="/"><i className="material-icons top">logout</i>Log out</a></li> */}
        <li>
          <a className="" href="/login/">
            Iniciar Sesion
          </a>
        </li>
        <li>
          <a href="/">Registrarse</a>
        </li>
      </ul>
      <ul id="dropdown2" className="dropdown-content">
        {/* <li><a href="/"><i className="material-icons top">account_circle</i>Perfil</a></li> */}
        {/* <li><a href="/"><i className="material-icons top">logout</i>Log out</a></li> */}
        <li>
          <a className="" href="/login/">
            Iniciar Sesion
          </a>
        </li>
        <li>
          <a href="/">Registrarse</a>
        </li>
      </ul>
      <nav>
        <div className="container">
          <div className="nav-wrapper">
            <Link to="/" className="brand-logo">
              SESP
            </Link>
            <a
              href="menu"
              data-target="mobile-demo"
              className="sidenav-trigger"
            >
              <i className="material-icons">menu</i>
            </a>
            <ul className="right hide-on-med-and-down">
              <li>
                <a href="/">
                  <i className="material-icons right">store</i>stores
                </a>
              </li>
              <li>
                <a
                  href="perfil"
                  className="dropdown-trigger"
                  data-target="dropdown1"
                >
                  <i className="material-icons right">arrow_drop_down</i>Perfil
                </a>
              </li>
            </ul>
          </div>
        </div>
      </nav>
      <ul className="sidenav" id="mobile-demo">
        <li>
          <a href="/">
            <i className="material-icons right">store</i>stores
          </a>
        </li>
        <li>
          <a href="perfil" className="dropdown-trigger" data-target="dropdown2">
            <i className="material-icons right">arrow_drop_down</i>Perfil
          </a>
        </li>
      </ul>
    </>
  );
};

export default Navbar;
