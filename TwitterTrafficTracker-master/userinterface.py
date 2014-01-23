#!/usr/bin/python 

import cgi
import geo_code as geo
import final_twitter as twitter_api
import google_map_display as gmap


if __name__=='__main__':
    print('Content-Type: text/html; charset=utf-8\n')
    
    print
    
    form = cgi.FieldStorage()
    keyword = form.getfirst("keyword")
    radius = form.getfirst("radius")
    city = form.getfirst("city")
    c = twitter_api.TwitterDataFetch()
    c.TwitterSearch(keyword,100,radius,city)
    b = geo.GeoCode()
    b.FetchCode()
    g = gmap.GoogleMapDisplay()
    g.map_draw()
#    print "Successfully Data Genrated"
    print '''
     <!DOCTYPE html>
     <html>
 <style>
body {
background-image:url('/twitter/twitter.jpg');	
}
</style>
     <body>
     

     <h2><i>Above Data Genrated From Twitter</i></h2>
     <a href= http://localhost/twitter/map.html>This is map Link.Please Click Here to View Traffic Data on Google Map</a>
     <p>This is Succes</p>
     </body>
     </html>'''
