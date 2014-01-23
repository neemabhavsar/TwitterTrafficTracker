'''
Twitter Tweet Grep Program v 1.0 
Obtain Real time Tweet Geo Location in human readable form Insert into Database.

@author: Parth Shah
'''

from twython import Twython
import re,os
from pygeocoder import Geocoder,GeocoderError
import logging
import conf 

#Twitter Account Data Starts From Here.This data is Provide Oauth authentication for accessing twitter API.

TWITTER_APP_KEY = 'HHazuNmQ6JEhPRn7cHpNA'
#TWITTER_APP_KEY = 'Nkqlrw1uNNBOfmginFp9Tg'

TWITTER_APP_KEY_SECRET = 'wRpO0LQS3veYRZXqvyV1ujatCZsH5BYbZ5nGh5heU' 
#TWITTER_APP_KEY_SECRET ='ctjWjFxQLb1XTJ8st4UiCDNcQXbXaSTNibivbPirk'

TWITTER_ACCESS_TOKEN = '2188902330-VYUy6S5uHZRIT0bprzuOPjVrTLWVADJgEin0JnQ'
#TWITTER_ACCESS_TOKEN = '132029232-RDy9XPcRg9sl6MGlXZw7fW9KLqV6ZfOOfGxzgIAC'
TWITTER_ACCESS_TOKEN_SECRET = 'Xv8Y1Gw2ZpXgO5SCVNcZ8FFZEzRI1S1dKklk9AGWbVk6T'
#TWITTER_ACCESS_TOKEN_SECRET = 'BRvoEDM7zSQZ1B0NPrWdK970OpEfR28ZO369NzP5A46IA'


logging.basicConfig(filename='/tmp/twtter.log',format='%(asctime)s %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')

class TwitterDataFetch():
    def __init__(self):
        self.twitter_obj =  Twython( app_key=TWITTER_APP_KEY, 
                                    app_secret=TWITTER_APP_KEY_SECRET, 
                                    oauth_token=TWITTER_ACCESS_TOKEN, 
                                    oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)
        logging.basicConfig(filename='/tmp/twtter.log',format='%(asctime)s %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')

        logging.info("oAuth Params created\n\n")
        
    def TwitterSearch(self,keyword,count,radius,city):
        self.query = self.twitter_obj.search(q='#'+str(keyword),count = count,geocode = conf.geo_codes[str(city)]+str(radius)+"mi")
        self.tweetdata =  self.query ['statuses']
        logging.info("Setting Tweet Data and Finding Keywords\n\n\n")
        try:
            f = open (conf.FILE_NAME,'w')
            for data in self.tweetdata:
                logging.info(data)
#                print data
                data = str(data['geo'])
                f.write(data+'\n')
                logging.info(data+'\n')
        except IOError:
            logging.error("FILE NOT FOUND\n\n\n,Please Check File\n")
 #           print "ERROR: FILE NOT FOUND\n\n\n"
            f.close()
    
    

        

