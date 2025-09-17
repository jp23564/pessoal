'use client'

import './app.css'
import { useState } from 'react'

function App() {

  const [weatherData, setWeatherData] = useState(null);
  const [city, setCity] = useState('Francisco Morato');

  useState(() => {

    const fetchWeatherData = async (cityName) => {
      try {
        const url = `https://geocoding-api.open-meteo.com/v1/search?name=${cityName}&count=1&language=en&format=json`;
        const response = await fetch(url);
        const data = await response.json();

        const weatherUrl = `https://api.open-meteo.com/v1/forecast?latitude=${data.results[0].latitude}&longitude=${data.results[0].longitude}&current=temperature_2m`;
        const weatherResponse = await fetch(weatherUrl);
        const weatherData = await weatherResponse.json();
        setWeatherData(weatherData);
        console.log(weatherData);

      } catch (error) {
        console.log(error);
      }
    }


    fetchWeatherData(city)

  }, [city]);

  return (
    <html>
      <body>


        {weatherData && weatherData.current && (
          <>

            <div className="wrapper">
              <div className="header">
                <h1 className="city">{city}</h1>
                <p className="temperature">{weatherData.current.temperature_2m}°C</p>
                <p className="condition">Ensolarado</p>
              </div>
              <div className="weather-details">
                <div className="humidity">
                  <p>Umidade</p>
                  <p>63%</p>
                </div>
                <div className="wind-speed">
                  <p>Vento</p>
                  <p>6km/h</p>
                </div>
              </div>
              <div className="forecast">
                <h2 className="forecast-header">Próximos 2 Dias</h2>
                <div className="forecast-days">
                  <div className="forecast-day">
                    <p>Segunda</p>
                    <p>Ensolarado</p>
                    <p>21°C</p>
                  </div>
                  <div className="forecast-day">
                    <p>Terça</p>
                    <p>Chuvoso</p>
                    <p>14°C</p>
                  </div>
                </div>
              </div>
            </div>

          </>
        )}

      </body>
    </html>
  );
}


export default App