from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

access_token = "3340873871-WcyL5tEeNFLWNsSfp7rX0YcOlNF77eqwSJuEq33"
access_token_secret = "KWBNhNbjqyNEraZ2XKlkWnNFs8Ms8DxNsRWup1tToAEME"
consumer_key = "Kx8tRssQeuRTuPFXCYEoWXNLm"
consumer_secret = "hfC3k3LIE9jVk6mg11kRyrGn0q7BbvOHuYSmajW3pI3sIwyFip"


class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    stream.filter(track=['python', 'javascript', 'ruby'])
