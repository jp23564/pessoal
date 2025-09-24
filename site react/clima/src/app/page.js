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

        const weatherUrl = `https://api.open-meteo.com/v1/forecast?latitude=${data.results[0].latitude}&longitude=${data.results[0].longitude}&daily=weather_code,temperature_2m_max,temperature_2m_min&current=temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code&timezone=America%2FSao_Paulo`;
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

  const getWeatherDescription = (wmoCode) => {
    const weatherDescriptions = {
      0: "Céu limpo",
      1: "Principalmente claro",
      2: "Parcialmente nublado",
      3: "Nublado",
      45: "Nevoeiro e nevoeiro com deposição de gelo",
      48: "Nevoeiro e nevoeiro com deposição de gelo",
      51: "Garoa: Intensidade leve",
      53: "Garoa: Intensidade moderada",
      55: "Garoa: Intensidade densa",
      56: "Garoa congelante: Intensidade leve",
      57: "Garoa congelante: Intensidade densa",
      61: "Chuva: Intensidade leve",
      63: "Chuva: Intensidade moderada",
      65: "Chuva: Intensidade forte",
      66: "Chuva congelante: Intensidade leve",
      67: "Chuva congelante: Intensidade forte",
      71: "Nevada: Intensidade leve",
      73: "Nevada: Intensidade moderada",
      75: "Nevada: Intensidade forte",
      77: "Grãos de neve",
      80: "Chuva em forma de chuvas fortes: Intensidade leve",
      81: "Chuva em forma de chuvas fortes: Intensidade moderada",
      82: "Chuva em forma de chuvas fortes: Intensidade violenta",
      85: "Nevasca: Intensidade leve",
      86: "Nevasca: Intensidade forte",
      95: "Trovoada: Intensidade leve ou moderada",
      96: "Trovoada com granizo leve",
      99: "Trovoada com granizo forte"
    };
    return weatherDescriptions[wmoCode] || 'Código de clima desconhecido';
  };

  const formatDateToDDMM = (date) => {
    const [yy, mm, dd] = date.split('-');
    return `${dd}/${mm}`;
  };

  return (
    <html>
      <body>


        {weatherData && weatherData.current && weatherData.daily && (
          <>

            <div className="wrapper">
              <div className="header">
                <h1 className="city">{city}</h1>
                <p className="temperature">{weatherData.current.temperature_2m}°C</p>
                <p className="condition">{getWeatherDescription(weatherData.current.weather_code)}</p>
              </div>
              <div className="weather-details">
                <div className="humidity">
                  <p>Umidade</p>
                  <p>{weatherData.current.relative_humidity_2m}%</p>
                </div>
                <div className="wind-speed">
                  <p>Vento</p>
                  <p>{weatherData.current.wind_speed_10m}km/h</p>
                </div>
              </div>
              <div className="forecast">
                <h2 className="forecast-header">Próximos 3 Dias</h2>
                <div className="forecast-days">
                  <div className="forecast-day">
                    <p>{formatDateToDDMM(weatherData.daily.time[1])}</p>
                    <p>{getWeatherDescription(weatherData.daily.weather_code[1])}</p>
                    <p>Max: {weatherData.daily.temperature_2m_max[1]}°C</p>
                    <p>Min: {weatherData.daily.temperature_2m_min[1]}°C</p>
                  </div>
                  <div className="forecast-day">
                    <p>{formatDateToDDMM(weatherData.daily.time[2])}</p>
                    <p>{getWeatherDescription(weatherData.daily.weather_code[2])}</p>
                    <p>Max: {weatherData.daily.temperature_2m_max[2]}°C</p>
                    <p>Min: {weatherData.daily.temperature_2m_min[2]}°C</p>
                  </div>
                  <div className="forecast-day">
                    <p>{formatDateToDDMM(weatherData.daily.time[3])}</p>
                    <p>{getWeatherDescription(weatherData.daily.weather_code[3])}</p>
                    <p>Max: {weatherData.daily.temperature_2m_max[3]}°C</p>
                    <p>Min: {weatherData.daily.temperature_2m_min[3]}°C</p>
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