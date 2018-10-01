# Twitter : DevicePartha / Onet..@..
import time
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy import StreamListener

from ArduinoInterface import ArduinoInterface


# Listener Class Override
class DeviceListener(StreamListener):
    
    def __init__(self):
        super(DeviceListener, self).__init__()
        self.tweet_data = []
        self.arduino = ArduinoInterface('COM3')

    def on_data(self, data):
#        while True:
            #print(data)
        if data.find('#pdevice1973on') > -1:
            print(data)
            self.arduino.setLed('on')
        if data.find('#pdevice1973off') > -1:
            print(data)
            self.arduino.setLed('off')
        if data.find('#pdevice1973bye') > -1:
            print(data)
            self.arduino.setLed('bye')
            print('EXITING #########################################')
            exit()

    def on_timeout(self):
        print('Timeout...')
        return True # To continue listening

    def on_error(self, status_code):
        print('ERROR ############ ', status_code)
        if status_code == 420:
            return False

    def on_status(self, status):
        print('Tweet text: ' + status.text)
        for hashtag in status.entries['hashtags']:
            print(hashtag['text'])

def main():
    api_key = '<YOUR_API_KEY>' # "consumer_key"
    api_secret_key = '<YOUR_API_SECRET_KEY>'
    access_token = '<YOUR_ACCESS_TOKEN>'
    access_token_secret = '<YOUR_ACCESS_TOKEN_SECRET>'
    auth = OAuthHandler(api_key, api_secret_key)  # OAuth object
    auth.set_access_token(access_token, access_token_secret)

    #api = tweepy.API(auth)

    twitterStream = Stream(auth, DeviceListener())  # initialize Stream object with a time out limit
    twitterStream.filter(track=['#pdevice1973on', '#pdevice1973off', '#pdevice1973bye'], languages=['en'])  # call the filter method to run the Stream Object

if __name__ == "__main__":
    main()
