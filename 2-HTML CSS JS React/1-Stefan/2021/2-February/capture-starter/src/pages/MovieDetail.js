import { MovieState } from "../movieState";
import { useHistory } from "react-router-dom";
import { useState, useEffect } from "react-dom";
import styled from "styled-components";

const MovieDetail = () => {
    const history = useHistory();
    //console.log(history);
    const url = history.location.pathname;
    const [movies, setMovies] = useState(MovieState);
    const [movie,setMovie] = useState(null);

    useEffect(() => {
        const currentMovie = movies.filter((stateMovie) => stateMovie.url === url);
        setMovie(currentMovie[0]);
    }, [movies, url]);

    return (
        <>
            {movie && (
                <StyledMovieDetails>
                    <StyledHeadline>
                        <h2>{movie.title}</h2>
                        <img src={movie.mainImg} alt="movie main image" />
                    </StyledHeadline>
                </StyledMovieDetails>
            )}
        </>
    );
}

const StyledMovieDetails = styled.div`
    color: white;
`

const StyledHeadline = styled.div`
    min-height: 90vh;
    padding-top: 20vh;
    position: relative;
    h2 {
        position: absolute;
        top: 10%;
        left: 50%;
        transform: translate(-50%, 10%);
    }
`

export default MovieDetail;