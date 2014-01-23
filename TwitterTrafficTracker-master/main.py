import geo_code as geo
import final_twitter as twitter_api
import google_map_display as gmap

if __name__ == '__main__':
    c = twitter_api.TwitterDataFetch()
    c.TwitterSearch('traffic',100,10)
    b = geo.GeoCode()
    b.FetchCode()
    g = gmap.GoogleMapDisplay()
    g.map_draw()
 
