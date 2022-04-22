import axios from "axios";

export default function asyncUpdateAction(weatherUrl) {
  //   return axios.get(weatherUrl)
  //     .then(res => dispatch(updateAction(res.data.current.condition)))
  //     .catch(error => console.log)
  return async (dispatch) => {
    try {
      const res = await axios.get(weatherUrl);
      dispatch(updateAction(res.data.current.condition));
    } catch (error) {
      console.log(error);
    }
  };
}

function updateAction(weatherData) {
  return {
    type: "UPDATE",
    payload: { ...weatherData }, // ... = spread
  };
}
