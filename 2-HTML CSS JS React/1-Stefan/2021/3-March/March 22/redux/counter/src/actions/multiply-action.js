export default function MultiplyAction(multiplier) {
  return {
    type: "MULT_COUNT",
    payload: {
      multiplier: multiplier,
    },
  };
}
