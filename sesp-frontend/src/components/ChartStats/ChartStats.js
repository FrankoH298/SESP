import React from "react";
import axios from "axios";
import { useState, useEffect } from "react";

import { Line, Pie, Bar } from "react-chartjs-2";

const ChartStats = (props) => {
  const [line, setLine] = useState([]);
  const [pie, setPie] = useState([]);
  const [bar, setBar] = useState([]);
  const [line2, setLine2] = useState([])
  const [notAuthorized, setNotAuthorized] = useState(false);

  useEffect(() => {
    axios
      .get(
        "/api/total_entries_last_week/" + props.store.id,{headers: {"Authorization": "Token "+ localStorage.getItem('id_token')}}
      )
      .then((response) => {
        setLine(response.data);
      })
      .catch((error) => {
        setNotAuthorized(true);
      });

    axios
      .get("/api/total_entries_per_day/" + props.store.id,{headers: {"Authorization": "Token "+ localStorage.getItem('id_token')}})
      .then((response) => {
        setPie(response.data);
      })
      .catch((error) => {
        setNotAuthorized(true);
      });

    axios
      .get("/api/total_entries_per_hour_last_two_weeks/" + props.store.id,{headers: {"Authorization": "Token "+ localStorage.getItem('id_token')}})
      .then((response) => {
        setLine2(response.data);
      })
      .catch((error) => {
        setNotAuthorized(true);
      });

    axios
      .get("/api/total_entries_per_month/" + props.store.id,{headers: {"Authorization": "Token "+ localStorage.getItem('id_token')}})
      .then((response) => {
        setBar(response.data);
      })
      .catch((error) => {
        setNotAuthorized(true);
      });
  }, []);

  const lineData = {
    labels: Object.keys(line),
    datasets: [
      {
        label: "Cantidad de Ingresos por día",
        backgroundColor: "#00897b",
        borderColor: "#005249",
        fill: true,
        data: Object.values(line),
      },
    ],
  };

  const pieData = {
    labels: Object.keys(pie),
    datasets: [
      {
        label: "Ingresos",
        backgroundColor: [
          "#00897b",
          "#185855",
          "#8fe8df",
          "#254dcb",
          "#df1818",
          "#9900ff",
          "#ff00aa",
        ],
        borderColor: "#ffffff",
        data: Object.values(pie),
      },
    ],
  };

  const barData = {
    labels: Object.keys(bar),
    datasets: [
      {
        label: "Ingresos",
        backgroundColor: [
          "#69da86",
          "#d72bdb",
          "#7aef53",
          "#5c128f",
          "#20c1cb",
          "#260046",
          "#6f230e",
          "#03590b",
          "#29c152",
          "#ea9c62",
          "#0a4a3a",
          "#205ba8",
        ],
        borderColor: "#ffffff",
        data: Object.values(bar),
      },
    ],
  };

  const lineData2 = {
    labels: Object.keys(line2),
    datasets: [
      {
        label: "Cantidad de Ingresos por hora",
        backgroundColor: "#00897b",
        borderColor: "#005249",
        fill: true,
        data: Object.values(line2),
      },
    ],
  };

  const lineOptions = {
    elements: {
      line: {
        tension: 0.4, // disables bezier curves
      },
    },
  };
  if (!notAuthorized) {
    return (
      <>
        <div className="row">
          <div className="container">
            <div className="col s12">
              <div className="card">
                <div className="card-content">
                  <div className="row">
                    <div className="col s12 m6 l6 center-align">
                      <span>Ingresos por día</span>
                      <div className="App">
                        <Line data={lineData} options={lineOptions} />
                      </div>
                    </div>
                    <div className="col s12 m6 l6 center-align">
                      <span> Ingresos por Mes</span>
                      <div>
                        <Bar data={barData} />
                      </div>
                    </div>
                    <div className="col s12 m6 l6 center-align">
                      <span>Cantidad de Ingresos por hora</span>
                      <div>
                        <Line data={lineData2} options={lineOptions}/>
                      </div>
                    </div>
                    <div className="col s12 m4 l4 center-align">
                      <span>Días con mayores ingresos</span>
                      <div>
                        <Pie data={pieData}/>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </>
    );
  } else {
    return <></>;
  }
};

export default ChartStats;
