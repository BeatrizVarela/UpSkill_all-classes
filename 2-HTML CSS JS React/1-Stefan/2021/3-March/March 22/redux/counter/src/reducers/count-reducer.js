const initialValue = 0;

export default function countReducer(state = initialValue, action) {
  switch (action.type) {
    case "ADD_TO_COUNT":
      return state + 1;
    case "SUB_TO_COUNT":
      return state - 1;
    case "MULT_COUNT":
      return state * action.payload.multiplier;
    default:
      return state;
  }
}
