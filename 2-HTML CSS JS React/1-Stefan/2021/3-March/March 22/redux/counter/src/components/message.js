import { useSelector } from "react-redux";

export default function Message() {
  const count = useSelector((state) => state);

  return (
    <div className="multiplier">
      <p>I know how to count until {count}</p>
    </div>
  );
}
