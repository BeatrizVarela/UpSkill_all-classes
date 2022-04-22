import { useEffect, useRef } from "react";
import { useSelector } from "react-redux";

export default function Multiplier() {
  const count = useSelector((state) => state);

  //   let input = null;

  //   useEffect(() => {
  //     input = document.querySelector("input");
  //   }, []);

  let inputRef = useRef(null);

  // HOW TO CONSOLE.LOG THE USEREF
  //   useEffect(() => {
  //     console.log(inputRef);
  //   }, []);

  const onClickHandler = () => {
    const value = inputRef.current.value;
    console.log(value);
  };

  return (
    <div className="multiplier" style={{ marginTop: "20pt" }}>
      <button type="button" onClick={onClickHandler}>
        *
      </button>
      <input
        type="number"
        name="multiplier"
        style={{ marginLeft: "20pt" }}
        ref={inputRef}
        value="0
        "
      />
    </div>
  );
}
