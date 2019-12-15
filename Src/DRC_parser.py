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


    def DRC_parser(self):
        # f = open(self.file_path,"r")
        # x = f.readlines()
        # print(x)
        with open(self.file_path,'r') as f:
            data = f.read().replace('\n', '')
        x=data.split()
        for i in range(0,len(x)):
            if "-" in x:
                x.remove("-")
