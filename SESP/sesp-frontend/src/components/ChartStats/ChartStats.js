import React from "react";
import axios from "axios";
import { useState, useEffect } from "react";

import { Line, Pie, Bar } from "react-chartjs-2";

const ChartStats = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios
      .get("api/total_entries_by_day/")
      .then((response) => {
        setData(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  const lineData = {
    labels: ["Sabado 14", "Domingo 15", "Lunes 16", "Martes 17"],
    datasets: [
      {
        label: "Cantidad de Ingresos por dia",
        backgroundColor: "#00897b",
        borderColor: "#005249",
        fill: true,
        data: [15, 6, 20, 14],
      },
    ],
  };

  const pieData = {
    labels: Object.keys(data),
    datasets: [
      {
        label: "Ausentes",
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
        data: Object.values(data),
      },
    ],
  };

  const barData = {
    labels: ["Enero", "Febrero", "Marzo", "Abril"],
    datasets: [
      {
        label: "Ausencias",
        backgroundColor: [
          "#00897b",
          "#185855",
          "#8fe8df",
          "#0df8d8",
          "#ff6600",
          "#00fff8",
          "#9900ff",
          "#ff00aa",
          "#000000",
          "#6a6a6a",
          "#00ff7b",
          "#ff97f5",
          "#7d1717",
          "#e2c2ef",
          "#00391d",
          "#73a529",
        ],
        borderColor: "#ffffff",
        data: [351, 856, 965, 456],
      },
    ],
  };
  return (
    <>
      <div className="row">
        <div className="col s12 m8 l8">
          <div className="card">
            <div className="card-content">
              <div className="row">
                <div className="col s12 m6 l6 center-align">
                  <span>Ingresos por dia</span>
                  <div className="App">
                    <Line data={lineData} />
                  </div>
                </div>
                <div className="col s12 m6 l6 center-align">
                  <span>Dias con Mayores Ingresos</span>
                  <div>
                    <Pie data={pieData} />
                  </div>
                </div>
                <div className="col s12 m6 l6 center-align">
                  <span>Empleados con Mayores Ausencias (EN TOTAL)</span>
                  <div>
                    <Bar data={barData} />
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default ChartStats;
