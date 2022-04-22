const initialState = {
  code: 420,
  icon: "//cdn.weatherapi.com/weather/64x64/day/116.png",
  text: "It's weed time",
};

export default function weatherReducer(state = initialState, action) {
  switch (action.type) {
    case "UPDATE":
      return {
        code: action.payload.code,
        icon: action.payload.icon,
        text: action.payload.text,
      };
    default:
      return { ...state };
  }
}
