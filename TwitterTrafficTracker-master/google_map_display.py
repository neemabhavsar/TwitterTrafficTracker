import pygmaps,random,conf
import webbrowser,re
import final_twitter as TwitterSearch


class GoogleMapDisplay():
    def __init__(self):
        self.file_name = conf.FILE_NAME
        self.file_name2 = '/home/jinesh/Desktop/stops.txt'
        self.point_color = random.choice(['#FF0000','#00FF00'])
        self.point_color_bus = "#0000FF"
        self.zoom = "10"
        self.map_file_path = "/var/www/twitter/map.html"
        
    def map_draw(self):
        self.pattern = '\[(\-?\d+\.\d+), (\-?\d+\.\d+)\]'
        self.pattern1 = '\,(\-?\d+\.\d+),(\-?\d+\.\d+)'
        self.file = open (self.file_name,'r')
        self.file2 = open(self.file_name2,'r')
        self.map_point = pygmaps.maps(37.3333,-121.9000,self.zoom)
        for i in self.file.readlines():
            self.result = re.search(self.pattern,i)
            if self.result:
                self.map_point.addpoint(float(self.result.group(1)),float(self.result.group(2)),self.point_color)
            for i in self.file2.readlines():
                self.result2 = re.search(self.pattern1,i)
                if self.result2:
                    self.map_point.addpoint(float(self.result2.group(1)),float(self.result2.group(2)),self.point_color_bus)
                    
                
        self.map_point.draw(self.map_file_path)
        
                
                
            

            
            
       

