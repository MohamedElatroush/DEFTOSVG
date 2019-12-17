#parsing the DRC file to get the locations of the SRC errors and highlight them so that the user can fix 
#those probelms in his/her design 
class DRC_parser:

    def __init__(self, DRC_file):
        self.file_path = DRC_file
        self.violation_type = None
        self.x1 = None
        self.x2 = None
        self.y1 = None
        self.y2 = None
        self.drc_list = []



    def parse(self):
        with open(self.file_path,'r') as f:
            data = f.read().replace('\n', '')
        x=data.split()
        for i in range(0,len(x)):
            if "-" in x:
                x.remove("-")



        for i in range(0,len(x)):
            if (x[i] == "type:"):
                if(x[i+1]== 0):
                    color = "#FF0000"
                    self.drc_list.append("color:")
                    self.drc_list.append(color)
                if(x[i+1]== 2):
                    color = "#FFC500"
                    self.drc_list.append("color:")
                    self.drc_list.append(color)

            elif (x[i] == "srcs:"):
                self.drc_list.append("source:")
                self.drc_list.append(x[i+1] + x[i+2])
            elif (x[i]=="bbox"): #contains x0,y0 and x1,y1
                self.x1 = x[i+2]
                self.y1 = x[i+3]
                self.x2 = x[i+4]
                self.y2 = x[i+5]
                self.x1 = self.x1.replace('(','')
                self.x1 = self.x1.replace(',','')
                self.y1 = self.y1.replace(')','')
                self.x2 = self.x2.replace('(', '')
                self.x2 = self.x2.replace(',', '')
                self.y2 = self.y2.replace(')', '')

                self.drc_list.append("dimensions:")
                self.drc_list.append(self.x1)
                self.drc_list.append(self.y1)
                self.drc_list.append(self.x2)
                self.drc_list.append(self.y2)

        return self.drc_list
        # print(self.drc_list)





