import home2 from "../img/home2.png";
import clock from "../img/clock.svg";
import teamwork from "../img/teamwork.svg";
import diaphragm from "../img/diaphragm.svg";
import money from "../img/money.svg";
import styled from "styled-components";
import { StyledDescription, StyledImage, StyledSection } from "../styles";

const ServicesSection = () => {
    return (
        <StyledServicesSection>
            <StyledDescription>
                <h2>
                    High <span>quality</span> services
                </h2>
                <StyledCards>
                    <StyledCard>
                        <div className="icon">
                            <img src={clock} alt="clock icon"/>
                            <h3>Efficient</h3>
                        </div>
                        <p>Lorem, ipsum dolor</p>
                    </StyledCard>
                    <StyledCard>
                        <div className="icon">
                            <img src={teamwork} alt="teamwork icon"/>
                            <h3>Teamwork</h3>
                        </div>
                        <p>Lorem, ipsum dolor</p>
                    </StyledCard>
                    <StyledCard>
                        <div className="icon">
                            <img src={diaphragm} alt="diaphragm icon"/>
                            <h3>Diaphragm</h3>
                        </div>
                        <p>Lorem, ipsum dolor</p>
                    </StyledCard>
                    <StyledCard>
                        <div className="icon">
                            <img src={money} alt="money icon"/>
                            <h3>Affordable</h3>
                        </div>
                        <p>Lorem, ipsum dolor</p>
                    </StyledCard>
                </StyledCards>
            </StyledDescription>
            <StyledImage>
                <img src={home2} alt="camera" />
            </StyledImage>
        </StyledServicesSection>
    )
}

const StyledServicesSection = styled(StyledSection)`
    padding: 100pt;
    h2 {
        padding-bottom: 5rem;
    }
    p {
        width: 70%;
        padding: 2rem 0rem 4rem 0rem;
    }
`

const StyledCards = styled.div`
    display: flex;
    flex-wrap: wrap;
`

const StyledCard = styled.div`
    flex-basis: 20rem;
    .icon {
        display: flex;
        align-items: center;
        h3 {
            margin-left: 1rem;
            background: white;
            color: black;
            padding: 1rem;
        }
    }

    @media screen and (max-width: 900px) {
        flex-basis: 15rem;
    }
`

export default ServicesSection;