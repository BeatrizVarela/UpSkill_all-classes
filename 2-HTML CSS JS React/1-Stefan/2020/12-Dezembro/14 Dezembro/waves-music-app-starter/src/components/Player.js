import { useRef,useState } from "react";
// importar os icons do font awesome
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
// procurar no fontawesome o nome dos icons desejados (encrever em camelCase)
import { faPlay, faPause, faAngleLeft, faAngleRight, faCloud } from "@fortawesome/free-solid-svg-icons";

// defenir os componentes
const Player = ({currentSong,setCurrentSong,songs,setSongs, isPlaying, setIsPlaying, audioRef}) => {

    const animateTrackRef = useRef(null);
    const [songInfo,setSongInfo] = useState({
        current: 0,
        duration: 0,
    }); // 1. criar estado song info

    const animationPercentage = Math.round((songInfo.current / songInfo.duration) * 100);

    // 2.1 Adicionar handlers nas setinhas
    // 2.2 Parar a musica atual que estiver a tocar
    // 2.3 Obter o indice da musica atual
    // 2.4 Obter o indice da musica seguinte ou anterior

    // Handlers
    const onAudioPlayHandler = (event) => { 
        if (isPlaying) {
            audioRef.current.pause();
            setIsPlaying(false);
        } else {
            audioRef.current.play();
            setIsPlaying(true);
        }
    }

    const onTimeUpdateHandler = (event) => { // 2. criar event handler
        const current = event.target.currentTime;
        const duration = event.target.duration;
/*         animateTrackRef.current.style = {
            transform: `translateX(${Math.round((current / duration) * 100)}%)`,
        }; */
        setSongInfo({
            current: current,
            duration: duration
        });
    }

    const onTimeChangeHandler = (event) => {
        audioRef.current.currentTime = event.target.value
        setSongInfo({...songInfo, current: event.target.value})
    }

    const skipTrackHandler = async(forwards) => {
        const songsLenght = songs.length;
        const currentSongIndex = songs.findIndex((song) => {
            return song.id === currentSong.id;
        });
        let nextIndex;
        if (forwards) {
/*             nextIndex = (currentSongIndex +1) % songsLenght; */
            if (currentSongIndex === (songsLenght -1)) {
                nextIndex = 0;
            } else {
                nextIndex = currentSongIndex +1;
            }
        } else {
/*             nextIndex = (songsLenght + (currentSongIndex -1)) % songsLenght; */
            if (currentSongIndex === 0) {
                nextIndex = songsLenght -1;
            } else {
                nextIndex = currentSongIndex -1;
            }
        }
        // skip track > next track goes back to 0:00 > starts playing automatically
        await setCurrentSong(songs[nextIndex]);
        notifyActiveLibraryHandler(songs[nextIndex]);
        setIsPlaying(true);
        audioRef.current.play();
    }

    const onEndedHandler = async(event) => {
        // 1. buscar proxima musica
        const songsCount = songs.length
        const currentSongIndex = songs.findIndex((song) => {
            return song.id === currentSong.id;
        });
        const nextIndex = (currentSongIndex + 1) % songsCount;

        // 2. tocar proxima musica
        await setCurrentSong(songs[nextIndex]);
        notifyActiveLibraryHandler(songs[nextIndex]);
        setIsPlaying(true);
        audioRef.current.play();
    }

    const notifyActiveLibraryHandler = (nextPrev) => {
        const newSongs = songs.map((song) => {
            if (song.id === nextPrev.id) {
                return {
                    ...song,
                    active: true
                }
            } else {
                return {
                    ...song,
                    active: false
                }
            }
        });
        setSongs(newSongs);
    }
    
    // Funcoes auxiliares
    const getTime = (time) => {
        return (
            Math.floor(time/60) + ":" + ("0" + Math.floor(time%60)).slice(-2)
        );
    }

return (
    <div className="player">
        <div className="time-control">
            <p>{getTime(songInfo.current)}</p>
            <div className="track" 
            style={{
                backgroundImage: `linear-gradient(to right, ${currentSong.color[0]}, ${currentSong.color[1]}, ${currentSong.color[2]}, ${currentSong.color[3]})`
            }}>
                <input type="range" min={0} max={songInfo.duration} value={songInfo.current} onChange={onTimeChangeHandler} />
                <div className="animate-track" ref={animateTrackRef} style={{transform: `translateX(${animationPercentage - 0.015*animationPercentage}%)`}}>
                    <div className="animate-track-thumb"><FontAwesomeIcon icon={faCloud} className="cloud" /></div>
                </div>
            </div>
            <p>{getTime(songInfo.duration)}</p>
        </div>
        <div className="play-control">
            <FontAwesomeIcon icon={faAngleLeft} size="2x" onClick={() => skipTrackHandler(false)} />
            <FontAwesomeIcon icon={isPlaying ? faPause : faPlay} size="2x" onClick={onAudioPlayHandler} />
            <FontAwesomeIcon icon={faAngleRight} size="2x" onClick={() => skipTrackHandler(true)} />
            <audio 
                src={currentSong.audio} 
                ref={audioRef} 
                onTimeUpdate={onTimeUpdateHandler}
                onLoadedMetadata={onTimeUpdateHandler}
                onEnded={onEndedHandler}
            />
        </div>
    </div>
    );
}

export default Player;