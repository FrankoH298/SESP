import React, { useState, useEffect } from "react";
import Card from "../UI/Card";
import axios from "axios";

function Home() {
  const [stores, setStores] = useState([]);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/api/stores")
      .then((response) => {
        setStores(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  return (
    <>
      <div className="container">
        <div className="row">
          {stores.map((store) => {
            return (
              <div key={store.user}>
                <Card
                  key={store.user}
                  title={store.name}
                  maxAmount={store.max_people}
                  people={store.actual_people}
                  phone={store.telephone_number}
                />
              </div>
            );
          })}
        </div>
      </div>
    </>
  );
}

export default Home;
