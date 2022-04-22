import { useDispatch, useSelector } from "react-redux";
import addAction from "./actions/add-action";
import subAction from "./actions/subtract-action";
import Message from "./components/message";
import Multiplier from "./components/multiplier";

function App() {
  const dispatch = useDispatch();

  const count = useSelector((state) => state);
  // console.log(count);

  return (
    <div className="App">
      <h1>Count: {count}</h1>
      <button type="button" onClick={() => dispatch(addAction())}>
        +
      </button>
      <button
        type="button"
        onClick={() => dispatch(subAction())}
        style={{ marginLeft: "20pt" }}
      >
        -
      </button>
      <Multiplier />
      <Message />
    </div>
  );
}

export default App;
