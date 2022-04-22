import { createGlobalStyle } from "styled-components";

const GlobalStyles = createGlobalStyle`
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    body {
        font-family: 'Inter',sans-serif;
        background-color: #1b1b1b;
    }

    button {
        font-weight: bold;
        font-size: 1.1rem;
        cursor: pointer;
        padding: 1rem 2rem;
        border: 3px solid #23d997;
        background-color: transparent;
        color: white;
        transition: all 0.5 ease;
        &:hover {
            background-color: #23d997;
        }
    }

    h2 {
        font-weight: lighter;
        font-size: 4rem;
    }

    h3 {
        color: white;
    }

    h4 {
        font-size: 2rem;
        font-weight: bold;
    }

    span {
        font-weight: bold;
        color: #23d997;
    }
    
    p {
        padding: 3rem 0rem;
        color: #ccc;
        font-size: 1.4rem;
        line-height: 150%;
        letter-spacing: 2px;
    }
`

export default GlobalStyles;