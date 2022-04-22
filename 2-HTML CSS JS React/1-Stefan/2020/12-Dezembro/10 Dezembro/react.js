const App = () => {
  const currentTime = new Date().toLocaleDateString();
  return React.createElement("div", { className: "app" }, [
    Tweet(),
    Tweet(),
    Tweet(),
  ]);
};

const Tweet = () => {
  const styles = { color: "red" };
  return React.createElement("div", null, [
    React.createElement("p", { style: styles }, "Hello World"),
    React.createElement("button", null, "Submit"),
  ]);
};

/*
  const Tweet = () => {
    const currentTime = new Date().toLocaleDateString();
  const styles = {color: "red"};
  return React.createElement("div",null, [
    React.createElement("p", {style: styles}, currentTime),
    React.createElement("button", null, "Submit")
  ]);
} 
*/

ReactDOM.render([App()], document.getElementById("root"));

//

const Tweet = () => {
  const currentTime = new Date().toLocaleDateString();
  const styles = { color: "red" };
  return (
    <div>
      <p style={styles}>{currentTime}</p>
      <button>Submit</button>
    </div>
  );
};

const App = () => {
  return (
    <div>
      <Tweet />
      <Tweet />
      <Tweet />
    </div>
  );
};

ReactDOM.render([App()], document.getElementById("root"));

//

const Tweet = () => {
  const currentTime = new Date().toLocaleDateString();
  const styles = {
    color: "red",
    backgroundColor: "Yellow",
  };
  return (
    <div>
      <p style={styles}>{currentTime}</p>
      <button>Submit</button>
    </div>
  );
};

const App = () => {
  return (
    <div>
      <Tweet />
      <Tweet />
      <Tweet />
    </div>
  );
};

ReactDOM.render([App()], document.getElementById("root"));
