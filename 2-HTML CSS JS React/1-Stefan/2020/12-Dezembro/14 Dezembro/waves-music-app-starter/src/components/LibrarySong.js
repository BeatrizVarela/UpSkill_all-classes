// import { config } from "@fortawesome/fontawesome-svg-core";

const LibrarySong = ({song, currentSong, setCurrentSong, songs, setSongs, isPlaying, setIsPlaying, audioRef}) => {
    const onSongSelectedHandler = async() => {
        const songId = song.id;
        const newSongs = songs.map((stateSong) => {
            if (songId === stateSong.id) {
                return {
                    ...song,
                    active: true
                }
            } else {
                return {
                    ...stateSong,
                    active: false
                }
            }
        });
        setSongs(newSongs);
        await setCurrentSong(song);
        setIsPlaying(true);
        audioRef.current.play();
    }
    return (
        <div className={`library-song ${song.active ? 'selected' : ''}`} onClick={onSongSelectedHandler}>
            <img src={song.cover} alt={`${song.name} cover`} />
            <div className="song-descrition">
                <h3>{song.name}</h3>
                <h4>{song.artist}</h4>
            </div>
        </div>
    );
}

export default LibrarySong;