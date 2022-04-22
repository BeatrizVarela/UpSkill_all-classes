import LibrarySong from "./LibrarySong";

const Library = ({songs, currentSong, setCurrentSong, setSongs, isLibraryOpen, isPlaying, setIsPlaying, audioRef}) => {
    return (
        <div className={`library ${isLibraryOpen ? "open": ""}`}>
            <h2>{'\u2728'}Library{'\u2728'}</h2>
            <div className="library-songs">
            {
                songs.map((song) => {
                    return <LibrarySong 
                        key={song.id}
                        song={song} 
                        songs={songs} 
                        setSongs={setSongs} 
                        currentSong={currentSong}
                        setCurrentSong={setCurrentSong}
                        isPlaying={isPlaying}
                        setIsPlaying={setIsPlaying}
                        audioRef={audioRef} />
                })
            }
            </div>
        </div>
    );
}

export default Library;