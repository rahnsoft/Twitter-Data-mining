import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
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

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])
