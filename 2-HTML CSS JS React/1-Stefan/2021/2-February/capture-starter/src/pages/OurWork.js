import athlete from "module";
import styled from "styled-components";

const OurWork = () => {
    return (
        <StyledWork>
        <div className="our-work">
            <h1>Our Work</h1>
        </div>
        </StyledWork>
    );
}

const StyledWork = styled.div`
    min-height: 100vh;
    overflow: hidden;
    padding: 5rem 10rem;
    h2 {
        padding: 1rem 0rem;
    }
`

const StyledMovie = styled.div`
    padding-bottom: 10rem;
    .line {
        height: 0.5rem;
        background-color: #cccccc;
        margin-bottom: 3rem;
    }
    img {
        width: 100%;
    }
`

export default OurWork;