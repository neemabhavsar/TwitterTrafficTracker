'''
This File Has Container of Geo Code Decoder from temp file and return geo location on human readable 
format
@author: Parth Shah 

'''
from pygeocoder import Geocoder,GeocoderError
import final_twitter as TwitterSearch
import re
import html_gen
import pygmaps
import webbrowser
from pymongo import Connection
import datetime
import conf

class GeoCode():
    def __init__(self):
        self.file_name = conf.FILE_NAME
        self.connection = Connection()
        self.db = self.connection['location']
        self.collection = self.db['address']
        
    def FetchCode(self):
        location = []
        
        self.pattern = '\[(\-?\d+\.\d+), (\-?\d+\.\d+)\]'
        self.file = open (self.file_name,'r')
        for i in self.file.readlines():
            self.result = re.search(self.pattern,i)
            if self.result:
                #print "Found Match"
                try:
                    results1 = Geocoder.reverse_geocode(float(self.result.group(1)),float(self.result.group(2)))
#                     print results1
                    post = {"address":results1,"date": datetime.datetime.utcnow()}
                    posts = self.db.post
                    
                    location.append(results1.__str__())
                    
                    
  #                  TwitterSearch.logging.info(results1)
                except GeocoderError:
                    print "Geo Coding Error\n\n Please Check Coordinate\n\n\n"

#        print location
#        print len(location)
        self.tbl = html_gen.HtmlGen(location)
        


