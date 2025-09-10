import './app.css'

export default function App()
{
  return(
    <html>
      <body>
        <div className="wrapper">
          <div className="header">
            <h1 className="city">Francisco Morato</h1>
            <p className="temperature">16ºC</p>
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
    </body>
  </html>
  );
}