import tweepy 
import json
consumer_key = "NezhcZ7ZOHTFMyvKNuwdxEpb4" 
consumer_secret = "SkaBr8LQ3PNTTYXD4z1lbV886A2MT22fFmEvPNoqWRPG3nD4QE"
access_key = "1020013932403019776-tOjd5QMASut2DSegqOp3kwQiyV6m5N"
access_secret = "E4RD5jIqJqIFeHvOK82YsTZi1IXVJVEqZXK2OOAtLdaBj"
  
# Function to extract tweets 
def get_tweets(username): 
          
        # Authorization to consumer key and consumer secret 
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
        # Access to user's access key and access secret 
        auth.set_access_token(access_key, access_secret) 
  
        # Calling api 
        api = tweepy.API(auth) 
  
        # 200 tweets to be extracted 
        number_of_tweets=2000
        tweets = api.user_timeline(screen_name=username, count=number_of_tweets) 
  
        # Empty Array 
        tmp=[]
  
        # create array of tweet information: username,  
        i=1
        tweets_for_json = {tweet.text for tweet in tweets}
        tmp.append("TWEETS")
        for j in tweets_for_json: 
  
            # Appending tweets to the empty array tmp 
            tmp.append(str(i)+") "+j)
            i=i+1
        # Printing the tweets 
        with open('ET.json', 'w') as f:
            json.dump(tmp, f, indent=2)
  
  
# main CALLING 
if __name__ == '__main__': 
    get_tweets("economictimes")