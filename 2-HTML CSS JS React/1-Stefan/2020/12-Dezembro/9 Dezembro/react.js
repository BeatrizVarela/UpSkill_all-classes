const h2 = React.createElement(
  "h2",
  { style: { color: "red" }, id: "myHeader2" },
  "Hello World!"
);
const h3 = React.createElement("h3", null, "Hello World!");
const div = React.createElement("h2", null, [h2, h3]);

ReactDOM.render(div, document.querySelector("#root"));

const h2 = <h2 style="color: red">Hello World!</>;
const h3 = <h3>Hello World!</h3>;
React.createElement("h3", null, "Hello World!");
const div = React.createElement("h2", null, [h2, h3]);

ReactDOM.render(div, document.querySelector("#root"));
