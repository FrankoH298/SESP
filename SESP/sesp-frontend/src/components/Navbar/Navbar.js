import "materialize-css/dist/css/materialize.css";
import { useEffect } from "react";
import { Link } from "react-router-dom";
import M from "materialize-css";

function Navbar() {
  useEffect(() => {
    let elems = document.querySelectorAll(".sidenav");
    M.Sidenav.init(elems);
  });

  return (
    <>
      <nav>
        <div className="container">
          <div className="nav-wrapper">
            <Link to="/" className="brand-logo">
              SESP
            </Link>
            <a href="/" data-target="mobile-demo" className="sidenav-trigger">
              <i className="material-icons">menu</i>
            </a>
            <ul className="right hide-on-med-and-down">
              <li>
                <a href="/">Sass</a>
              </li>
              <li>
                <a href="/">Components</a>
              </li>
              <li>
                <a href="/">Javascript</a>
              </li>
              <li>
                <a href="/">Mobile</a>
              </li>
            </ul>
          </div>
        </div>
      </nav>

      <ul className="sidenav" id="mobile-demo">
        <li>
          <a href="/">Sass</a>
        </li>
        <li>
          <a href="/">Components</a>
        </li>
        <li>
          <a href="/">Javascript</a>
        </li>
        <li>
          <a href="/">Mobile</a>
        </li>
      </ul>
    </>
  );
}

export default Navbar;
