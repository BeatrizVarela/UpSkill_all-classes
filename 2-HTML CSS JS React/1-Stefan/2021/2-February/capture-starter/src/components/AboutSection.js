import home1 from "../img/home1.png";
//import styled from "styled-components";
import {StyledSection, StyledImage, StyledDescription, StyledHide} from "../styles";

const AboutSection = () => {
    return (
        <StyledSection>
            <StyledDescription>
                <StyledImage>
                    <StyledHide>
                        <h2>We work to make</h2>
                    </StyledHide>
                    <StyledHide>
                        <h2>your <span>dreams</span></h2>
                    </StyledHide>
                    <StyledHide>
                        <h2>come true.</h2>
                    </StyledHide>
                </StyledImage>
                <p>Contact us for any photography or videography ideas that you have. We have professionals with amazing skills.</p>
                <button>
                    Contact Us
                </button>
            </StyledDescription>
            <div className="image">
                <img src={home1} alt="guy with a camera" />
            </div>
        </StyledSection>
    )
}

export default AboutSection;