import { useState, useRef } from "react";
// child files
import Player from "./components/Player";
import Song from "./components/Song";
import Library from "./components/Library";
import Nav from "./components/Nav";
import data from "./data";
// scss styles
import "./styles/App.scss";

function App() {

  const [songs, setSongs] = useState(data());
  const [currentSong, setCurrentSong] = useState(songs[0]);
  const [isLibraryOpen, setIsLibraryOpen] = useState(false);
  const [isPlaying,setIsPlaying] = useState(false);

  const audioRef = useRef(null);

  const openLibraryHandler = () => {
    setIsLibraryOpen(!isLibraryOpen);
  }
  
  return (
    <div className={`App ${isLibraryOpen? 'library-active': ''}`}>
      <Nav openLibraryHandler={openLibraryHandler} />
      <Song currentSong={currentSong} />
      <Player 
        currentSong={currentSong} 
        setCurrentSong={setCurrentSong} 
        songs={songs} 
        isPlaying={isPlaying}
        setIsPlaying={setIsPlaying}
        audioRef={audioRef}
        setSongs={setSongs} />
      <Library 
        songs={songs} 
        setSongs={setSongs} 
        currentSong={currentSong} 
        setCurrentSong={setCurrentSong} 
        isLibraryOpen={isLibraryOpen}
        isPlaying={isPlaying}
        setIsPlaying={setIsPlaying}
        audioRef={audioRef} />
    </div>
  );
}

export default App;
