from html import HTML


class HtmlGen():
    def __init__(self,list_data):
        self.h = HTML()
	        
	self.table = self.h.table(border='2',align='center')
	
	
        for i in range(len(list_data)):
            self.r = self.table.tr
            self.r.td('%s'%str(i+1))
            self.r.td(list_data[i])
        print self.table
        
            
    

