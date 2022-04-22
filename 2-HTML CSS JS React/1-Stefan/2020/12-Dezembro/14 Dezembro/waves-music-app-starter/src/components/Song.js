// import EDM from "../data";
// import "../styles/_song.scss";

const Song = ({currentSong}) => {
    return (
        <div className="song">
            <img src={currentSong.cover} alt={currentSong.name} />
            <h2>{currentSong.name}</h2>
            <h3>{currentSong.artist}</h3>
        </div>
    );
}

export default Song;