import { StyledSection } from "../styles";
import styled from "styled-components";

const FaqSection = () => {
    return (
        <StyledFaqSection>
            <h2>
                Any questions? <span>FAQ</span>
            </h2>
            <div className="question">
                <h4>How do I start?</h4>
                <div className="answer">
                    <p>Lorem ipsum dolor sit amet</p>
                    <p>
                        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Reprehenderit placeat, perspiciatis vero accusamus illum facilis ullam delectus exercitationem minus non quisquam suscipit est error sequi magnam, perferendis fugit similique reiciendis?
                    </p>
                </div>
                <div className="faq-line"></div>
            </div>
            <div className="question">
                <h4>Daily Schedule</h4>
                <div className="answer">
                <p>Lorem ipsum dolor sit amet</p>
                    <p>
                        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Reprehenderit placeat, perspiciatis vero accusamus illum facilis ullam delectus exercitationem minus non quisquam suscipit est error sequi magnam, perferendis fugit similique reiciendis?
                    </p>
                </div>
                <div className="faq-line"></div>
            </div>
            <div className="question">
                <h4>Different payment methods</h4>
                <div className="answer">
                <p>Lorem ipsum dolor sit amet</p>
                    <p>
                        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Reprehenderit placeat, perspiciatis vero accusamus illum facilis ullam delectus exercitationem minus non quisquam suscipit est error sequi magnam, perferendis fugit similique reiciendis?
                    </p>
                </div>
                <div className="faq-line"></div>
            </div>
            <div className="question">
                <h4>What products do you offer?</h4>
                <div className="answer">
                <p>Lorem ipsum dolor sit amet</p>
                    <p>
                        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Reprehenderit placeat, perspiciatis vero accusamus illum facilis ullam delectus exercitationem minus non quisquam suscipit est error sequi magnam, perferendis fugit similique reiciendis?
                    </p>
                </div>
                <div className="faq-line"></div>
            </div>
        </StyledFaqSection>
    )
}

const StyledFaqSection = styled(StyledSection)`
    display: block;
    span {
        display: block;
    }
    h2 {
        padding-bottom: 2rem;
        font-weight: lighter;
    }
    .faq-line {
        background-color: #cccccc;
        height: 0.2rem;
        margin: 2rem 0rem;
        width: 100%;
    }
    .question {
        padding: 3rem 0rem;
        cursor: pointer;
    }
    .answer {
        padding: 2rem 0rem;
        p {
            padding: 1rem 0rem;
        }
    }
`

export default FaqSection;