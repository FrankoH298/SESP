import React, { useState, useEffect } from "react";
import Card from "../UI/Card";
import axios from "axios";

const Home = () => {
  const [stores, setStores] = useState([]);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/api/stores/")
      .then((response) => {
        setStores(response.data);
        console.log(response.data)
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
                  user={store.user}
                  id={store.id}
                  name={store.name}
                  maxPeople={store.max_people}
                  actualPeople={store.actual_people}
                  telephoneNumber={store.telephone_number}
                  isFull={store.is_full}
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
