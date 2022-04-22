import { useEffect, useRef } from "react";
import { weatherUrlForCity } from "./api";
import { useSelector, useDispatch } from "react-redux";
import asyncUpdateAction from "./actions/update-action";

function App() {
  const dispatch = useDispatch();

  const cityInputRef = useRef(null);

  const weatherData = useSelector((state) => state);
  console.log(`weather data: ${weatherData}`);

  const fetchWeatherData = (dispatch) => {
    dispatch(asyncUpdateAction(weatherUrlForCity(cityInputRef.current.value)));
  };

  // PROMISE com then
  useEffect(() => {
    fetchWeatherData(dispatch);
  }, [dispatch]);

  // OUTRO TIPO DE PROMISE
  // const fetchWeather = async(url) {
  //   try {
  //     const weatherData = await axios.get(WEATHER_URL);
  //     console.log(weatherData)
  //   } catch (error) {
  //     console.log(error)
  //   }
  // }

  const onSubmitHandler = (event) => {
    event.preventDefault();
    fetchWeatherData(dispatch);
  };

  return (
    <div className="App">
      <form>
        <input type="text" defaultValue="Lisbon" ref={cityInputRef} />
        <input
          type="submit"
          value="Update"
          style={{ marginLeft: "10pt" }}
          onClick={onSubmitHandler}
        />
      </form>
      <p>Code: {weatherData.code}</p>
      <img src={weatherData.icon} alt={weatherData.text} />
      <h3>Description: {weatherData.text}</h3>
    </div>
  );
}

export default App;
