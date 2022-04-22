import { useState,useRef } from 'react';  // 1 - importar useState
import TweetList from './components/TweetList';
import { uuid } from 'uuidv4';
import './styles/App.scss';

function App() {
  
  const inputRef = useRef(null);

  const [abc,setAbc]=useState("abc");

  const [tweets,setTweets]=useState([]); // 2 - definir o estado

   // useEffect(() => {
     // console.log("Hey we are using an Effect!")
    
   // }, [tweets]);

  const sumitClickHandler=(event) => {
    event.preventDefault();
    // abc = "submit"
    // console.log("submit button clicked");
    setAbc("Submit");
    // console.log(abc);
    const tweetObject = {
      id: uuid(),
      text: inputRef.current.value,
      liked: false
    }

    inputRef.current.value="";
    const newTweets =[...tweets, tweetObject]
    setTweets(newTweets)
  }

  const appStyles = {
    color: "white",
    backgroundColor: "rgb(226, 208, 228)"
  }

  return (
  <div className="App" style={appStyles}>
    <form>
      <input type="text" placeholder="What are you thinking?..." ref={inputRef} />
      <button onClick={sumitClickHandler} type="submit">{abc}</button>
    </form>
    <TweetList message="tweet" tweets={tweets} setTweets={setTweets} />
  </div>);
}

export default App;
