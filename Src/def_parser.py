"""
DEF Parser
Author: Tri Minh Cao
Email: tricao@utdallas.edu
Date: August 2016
"""

from def_util import *
from util import *
import re
import drawSvg as draw
import matplotlib.pyplot as plt

class DefParser:
    """
    DefParser will parse a DEF file and store related information of the design.
    """

    def __init__(self, def_file):
        self.file_path = def_file
        # can make the stack to be an object if needed
        self.stack = []
        # store the statements info in a list
        self.sections = []
        self.property = None
        self.components = None
        self.pins = None
        self.nets = None
        self.tracks = []
        self.gcellgrids = []
        self.rows = []
        self.diearea = None
        self.version = None
        self.dividerchar = None
        self.busbitchars = None
        self.design_name = None
        self.units = None
        self.scale = None

    def parse(self): #parsing the def file
        """
        Main method to parse the DEF file
        :return: void
        """
        print ("Start parsing DEF file...")
        # open the file and start reading
        f = open(self.file_path, "r+") #opening the def file

        # the program will run until the end of file f
        for line in f:
            # split the string by the plus '+' sign

            parts = split_plus(line) #removing the + sign
            for each_part in parts:

                # split each sub-string by space
                info = split_space(each_part)

                if len(info) > 0:
                    #print info
                    if info[0] == "PINS":
                        new_pins = Pins(int(info[1]))
                        #print(int(info[1]))
                        self.stack.append(new_pins)

                         #print (new_pins.type)
                    elif info[0] == "VERSION": #getting the version
                        self.version = info[1]

                    elif info[0] == "DIVIDERCHAR": #getting the dividechar simpole 
                        self.dividerchar = info[1]

                    elif info[0] == "BUSBITCHARS": #indicating if the busbitchars is enabled or not
                        self.busbitchars = info[1]
                    elif info[0] == "DESIGN" and len(info) <= 3:
                        # differentiate with the DESIGN statement inside
                        # PROPERTYDEFINITIONS section.
                        self.design_name = info[1]
                    elif info[0] == "UNITS": #getting the units section
                        self.units = info[2]
                        self.scale = info[3]
                    elif info[0] == "PROPERTYDEFINITIONS": 
                        new_property = Property()
                        self.stack.append(new_property)
                    elif info[0] == "DIEAREA": #getting the die area
                        info_split = split_parentheses(info)
                        pt1 = (int(info_split[1][0]), int(info_split[1][1]))
                        pt2 = (int(info_split[2][0]), int(info_split[2][1]))
                        self.diearea = [pt1, pt2]
                        #print(self.diearea)
                    elif info[0] == "COMPONENTS": #getting the components sections 
                        new_comps = Components(int(info[1]))
                        self.stack.append(new_comps)

                    elif info[0] == "NETS": #getting the net section
                        new_nets = Nets(int(info[1]))
                        self.stack.append(new_nets)

                    elif info[0] == "TRACKS": #getting the tracks info
                        new_tracks = Tracks(info[1])
                        new_tracks.pos = int(info[2])
                        new_tracks.do = int(info[4])
                        new_tracks.step = int(info[6])
                        new_tracks.layer = info[8]
                        self.tracks.append(new_tracks)
                        #print(self.tracks)


                    elif info[0] == "GCELLGRID":
                        new_gcellgrid = GCellGrid(info[1])
                        new_gcellgrid.pos = int(info[2])
                        new_gcellgrid.do = int(info[4])
                        new_gcellgrid.step = int(info[6])
                        self.gcellgrids.append(new_gcellgrid)
                    elif info[0] == "ROW": #getting the rows and their numbers
                        new_row = Row(info[1])
                        new_row.site = info[2]
                        new_row.pos = (int(info[3]), int(info[4]))
                        new_row.orient = info[5]
                        new_row.do = int(info[7])
                        new_row.by = int(info[9])
                        new_row.step = (int(info[11]), int(info[12]))
                        self.rows.append(new_row)
                        #for i in range(0, len(self.stack)):
                        #    print( new_row.site)

                    elif info[0] == "END": #checking if we reached the end
                        if len(self.stack) > 0:
                            self.sections.append(self.stack.pop())
                         #print ("finish")
                    else:
                        if len(self.stack) > 0:
                            latest_obj = self.stack[-1]
                            latest_obj.parse_next(info)
        f.close()
        #for i in range(0,len(self.stack)):
        #    print(self.stack[i])

        # put the elements in sections list into separate variables
        for sec in self.sections:
            if sec.type == "PROPERTY_DEF": #making list for properties 
                self.property = sec
            elif sec.type == "COMPONENTS_DEF": #making list for components 
                self.components = sec
            elif sec.type == "PINS_DEF": #making list for pins 
                self.pins = sec

            elif sec.type == "NETS_DEF": #making list for nets 
                self.nets = sec
        print ("Parsing DEF file done.\n")
        #print(self.property)


    def to_def_format(self): #generating the def file
        s = ""
        s += "#  Generated by tricao@utdallas.edu for testing only.\n\n"
        s += "VERSION " + self.version + " ;" + "\n"
        s += "DIVIDERCHAR " + self.dividerchar + " ;" + "\n"
        s += "BUSBITCHARS " + self.busbitchars + " ;" + "\n"
        s += "DESIGN " + self.design_name + " ;" + "\n"
        s += "UNITS DISTANCE " + self.units + " " + self.scale + " ;" + "\n"
        s += "\n"
        props = self.sections[0]
        s += props.to_def_format()
        s += "\n"
        s += "DIEAREA"
        s += (" ( " + str(self.diearea[0][0]) + " " + str(self.diearea[0][1]) +
             " )")
        s += (" ( " + str(self.diearea[1][0]) + " " + str(self.diearea[1][1]) +
             " )" + " ;")
        s += "\n\n"
        for each_row in self.rows:
            s += each_row.to_def_format()
            s += "\n"
        s += "\n"
        for each_tracks in self.tracks:
            s += each_tracks.to_def_format()
            s += "\n"
        s += "\n"
        for each_gcell in self.gcellgrids:
            s += each_gcell.to_def_format()
            s += "\n"
        s += "\n"
        comps = def_parser.sections[1]
        s += comps.to_def_format()
        s += "\n\n"
        pins = def_parser.sections[2]
        s += pins.to_def_format()
        s += "\n\n"
        nets = def_parser.sections[3]
        s += nets.to_def_format()
        return s

    def write_def(self, new_def, back_end=True, front_end=True):
        """
        Write a new def file based on the information in the DefParser object.
        Note: this method writes all information
        :param new_def: path of the new DEF file
        :param back_end: write BEOL information or not.
        :param front_end: write FEOL info or not.
        :return: void
        """
        f = open(new_def, mode="w+")
        print("Writing DEF file...")
        f.write(self.to_def_format())
        print("Writing done.")
        f.close()


# Main Class
if __name__ == '__main__':
    # read_path = "./libraries/DEF/c880_tri.def"
    read_path = "/Users/Hatem/Desktop/i2c_master.def"
    def_parser = DefParser(read_path)
    def_parser.parse()
    x = ""
    # compon={}
    # f = open("components.txt", "w")
    # for key, val in def_parser.components.comp_dict:
    #     f.write(str(key))
    #     f.write(str(val))
    #
    #     compon[key] = str(val)
    #     # x = str(val)
    #     # x.split(":")
    #     # print(x)
    #     #print(str(val).find("Macro: "))
    #     #print(str(key))
    #     x = str(val).split()
    #     #print(x[3])
    #     #compon[key] = str(val)
    #     y=x[5]+x[6]
    #     #print(y.split("[,]"))
    #     #print(y)
    #     #y.split()
    #     #print(y)
    #     compon[x[3]]=y

    # z = def_parser.diearea
    #
    # # print(compon.keys())
    #
    # pos = re.split('[, ()]',str(z))
    #
    # x1 = pos[1]
    # x2 = pos[3]
    # x3 = pos[7]
    # x4 = pos[9]
    #
    # width=int(x3)-int(x1)
    # height=int(x4)-int(x2)
    #
    # d = draw.Drawing(width,height, origin=(0,-height))    #drawing of diearea
    # d.append(draw.Rectangle(int(x1), int(x2), int(x3), int(x4), fill='#1248ff',opacity = 0.1,color = 'green', stroke = 'black', stroke_width=3))
    # d.saveSvg('example.svg')
    # d.savePng('example.png')
    #
    # # Display in iPython notebook
    # d.rasterize()  # Display as PNG
    # d  # Display as SVG

    #f.close()

    # f = open("pins.txt", "w")
    # for key, val in def_parser.pins.pin_dict.items():
    #     f.write(str(key))
    #     f.write(str(val))

    #f.close()

    # f = open("nets.txt", "w")
    # for key, val in def_parser.nets.net_dict.items():
    #     f.write(str(key))
    #     f.write(str(val))

    #print(def_parser.diearea)

    #f.write(str(def_parser.components.comp_dict))
    #f.close()

    #print("here")


    #for each_pin in def_parser.pins.pins:
    #    print (each_pin)

     #print(def_parser.to_def_format())

    # test macro and via (note: only via1)
    # macro_dict = macro_and_via1(def_parser)
    # for comp in macro_dict:
    #     print (comp)
    #     for pin in macro_dict[comp]:
    #         print ("    " + pin + ": " + str(macro_dict[comp][pin]))
    #     print ()
