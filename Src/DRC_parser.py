class DRC_parser:

    def __init__(self, DRC_file):
        self.file_path = DRC_file
        self.violation_type = None
        self.dimensions = None


    def DRC_parser(self):
        f = open(self.file_path,"r")
        x = f.readlines()
        print(x)