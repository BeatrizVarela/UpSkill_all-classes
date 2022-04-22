import { useState } from 'react';
import s from '../styles/Tweet.module.css';
import styled from 'styled-components';

const Tweet = ({tweet, tweets, setTweets}) => {

    const onRemoveHandler=(event) => {
        const newTweets=tweets.filter((tweetItem) => {
            return tweetItem.id !== tweet.id;
        });
        setTweets(newTweets);
    }

    const [like, setLike] = useState(false);

    const onLikeHandler = (event) => {
        // buscar o indice to tweet
        setLike(!like);
    }

    const TweetContainer = styled.div`
        background-color: pink
        `

    return (
        <div className={s.tweet} id={tweet.id}>
            <TweetContainer>
                <div>
                    <h3>{tweet.text}</h3>
                    <p><i className={`fas fa-skull ${like? '' : 'hidden'}`}></i></p>
                </div>
                <button onClick={onRemoveHandler}>Remove</button>
                <button onClick={onLikeHandler}>Dislike</button>
            </TweetContainer>
        </div>
    );
}

export default Tweet;