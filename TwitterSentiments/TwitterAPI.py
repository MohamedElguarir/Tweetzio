# Imports
import tweepy
import re
from datetime import datetime



# Twitter API credentials
consumer_key = "Yf5wvaYl9KePLVmAyiGlje3EW"
consumer_secret = "aFrhf1VMkDe3ivSBTHukl8puffUwJcDOwgG031Zg2KNOADD82F"
access_key = "1641206051918733318-8We0T4xqFcB4JgnJuXmWW3loTE55Tm"
access_secret = "2f4GIHgjOvT6LDXlr5A0HIKjQIk13LlFf7o80XM31YNNt"

auth_handler = tweepy.OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_secret)
auth_handler.set_access_token(access_key, access_secret)
api = tweepy.API(auth_handler)

def time_diffrence(date):
    today = datetime.today()
    tweet_date = datetime.strptime(date, "%d/%m/%Y")

    # Calculating the difference between the two dates
    delta = today - tweet_date
    
    # Formating the difference of dates
    if delta.days >= 7:
        weeks = delta.days // 7
        return(f"{weeks}w ago")
    elif delta.days > 0:
        return(f"{delta.days}d ago")
    else:
        total_seconds = delta.seconds
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        if hours > 0:
            return(f"{hours}h ago")
        elif minutes > 0:
            return(f"{minutes}m ago")
        else:
            return(f"{seconds}s ago")



def search_tweets(search_term, limit):
    tweets = tweepy.Cursor(api.search_tweets, q=search_term+" AND -filter:retweets AND -filter:replies", lang="en", tweet_mode="extended", result_type="recent").items(20)
    tweets_array = []

    for tweet in tweets:
        tweet_dict = {}

        tweet_dict["id"] = tweet.id
        tweet_dict["ScreenName"] = tweet.user.name
        tweet_dict["username"] = tweet.user.screen_name
        tweet_dict["tweet_text"] = re.sub(r"http\S+", "", tweet.full_text).strip()

        img = tweet.user.profile_image_url.replace("_normal", "_400x400")
        tweet_dict["user_profile_image_url"] = img

        date = tweet.created_at.strftime("%d/%m/%Y")
        tweet_dict["date"] = date
        tweet_dict["date_diff"] = time_diffrence(date)
        
        tweets_array.append(tweet_dict)

    return tweets_array





# def search_user_tweets(username, limit):
#     tweets = tweepy.Cursor(api.user_timeline, id=username, tweet_mode="extended", result_type="recent").items(limit)
#     tweets_array = []

#     for tweet in tweets:
#         tweet_dict = {}

#         # exclude retweets
#         tweet_dict["id"] = tweet.id
#         tweet_dict["ScreenName"] = tweet.user.name
#         tweet_dict["username"] = tweet.user.screen_name
#         tweet_dict["tweet_text"] = re.sub(r"http\S+", "", tweet.full_text).strip()
       

#         img = tweet.user.profile_image_url.replace("_normal", "_400x400")
#         date = tweet.created_at.strftime("%d/%m/%Y")
#         tweet_dict["date"] = date
#         tweet_dict["date_diff"] = time_diffrence(date)
#         tweet_dict["user_profile_image_url"] = img
#         tweets_array.append(tweet_dict)

#     return tweets_array