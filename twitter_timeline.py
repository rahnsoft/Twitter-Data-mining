import tweepy

#Variables that contains the user credentials to access Twitter API gotten from createing a developer account and creating an app to get the keys
# nicholas access token
access_token = "3617311579-tvFmjQcM5DRU4q7gLblsdP4meIlWvZLdwTZOUnC"
# nicholas access token secret
access_token_secret = "4auM08EANuJBw6vyVCJpNHVWb2fv1ETSa7apw6bs8Tuz0"
# nicholas twitter api key
consumer_key = "Ypq9D8XecPD32bdqKtig5zMpp"
#nicholas twitter api key secret
consumer_secret = "5ZPWNCdPazZTGkTxSXNFKiB4M3XmY30yEDUxGUdUiEAiYEIrxY"

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth)

# Using the API object to get tweets from your timeline, and storing it in a variable called public_tweets
public_tweets = api.home_timeline()
# foreach through all tweets pulled
for tweet in public_tweets:
   # printing the text stored inside the tweet object
   print tweet.text