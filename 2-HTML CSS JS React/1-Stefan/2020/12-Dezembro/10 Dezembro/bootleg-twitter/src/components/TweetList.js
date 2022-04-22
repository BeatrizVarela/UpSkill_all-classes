import Tweet from './Tweet';

const TweetList = ({tweets,setTweets}) => {
    return (
    <div className="tweet-list">
        {
            tweets.map((tweet) => <Tweet tweet={tweet} tweets={tweets} setTweets={setTweets} key={tweet.id} />)
        }
    </div>
    )
}

export default TweetList;