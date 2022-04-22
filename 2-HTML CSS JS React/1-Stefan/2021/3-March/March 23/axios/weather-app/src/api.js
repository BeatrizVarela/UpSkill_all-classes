const BASE_URL = `https://api.weatherapi.com/v1/current.json`;

export const weatherUrlForCity = (city) => {
  return `${BASE_URL}?key=${process.env.REACT_APP_WEATHER_API_KEY}&q=${city}&aqi=no`;
};
