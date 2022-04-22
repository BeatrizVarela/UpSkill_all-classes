import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import { faMusic } from "@fortawesome/free-solid-svg-icons"

const Nav = ({openLibraryHandler}) => {

    return (
        <nav>
            <h1>comfy songs</h1>
            <button onClick={openLibraryHandler}>
                {'\u2728'}Library
                <FontAwesomeIcon icon={faMusic} />{'\u2728'}
            </button>
        </nav>
    )
} 

export default Nav;