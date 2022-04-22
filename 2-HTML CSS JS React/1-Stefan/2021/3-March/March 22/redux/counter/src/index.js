import React from "react";
import ReactDOM from "react-dom";
import { Provider } from "react-redux";
import { createStore } from "redux";
import App from "./App";
import countReducer from "./reducers/count-reducer";
import reportWebVitals from "./reportWebVitals";

// HOW REDUX WORKS BASICALLY
// const [state, setState] = useState({
//   "count": 0,
//   "users": []
// });

// const reducer = (action) =>  {
//   switch (action.type) {
//     case "ADD_TO_COUNT":
//       setState({...state, count: count + 1})
//   }
// }

const store = createStore(
  countReducer,
  window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
);

ReactDOM.render(
  <React.StrictMode>
    <Provider store={store}>
      <App />
    </Provider>
  </React.StrictMode>,
  document.getElementById("root")
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
