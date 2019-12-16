from lef_parser import *
from def_parser import *
import drawSvg as draw
import re
from DRC_parser import *


def toSVG(read_path, path,path2):
    pth = read_path.split("/")
    for i in pth[-1]:
        if i == '.':
            dotindx = pth[-1].index(".", 0)
            pth[-1] = pth[-1][0:dotindx]

    ############

    ####################
    # parsing the def file
    def_parser = DefParser(read_path)
    def_parser.parse()
    macro = ""
    for key, val in def_parser.components.comp_dict.items():
        x = str(val).split()
        macro = macro + " " + x[3] + " " + str(x[5]).strip("[,") + " " + str(x[6]).strip("]") + " " + str(x[7])
    nets = []
    for key, val in def_parser.nets.net_dict.items():  # extracting nets information and putting in list
        nets += str(val).split()
    # print(nets)

    def_scale = def_parser.scale  # scalling the def
    # print("DEF scale: ",def_scale)

    MACRO = macro.split()  # DEF INFO CARRIER
    # print(MACRO)
    # getting the die area of the circuit
    z = def_parser.diearea

    pos = re.split('[, ()]', str(z))

    # diearea coordinates in string
    x1 = pos[1]
    # diearea coordinates in string
    x2 = pos[3]
    # diearea coordinates in string
    x3 = pos[7]
    # diearea coordinates in string
    x4 = pos[9]

    dx0 = int(x1)  # diearea coordinates in int
    dy0 = int(x2)  # diearea coordinates in int
    dx1 = int(x3)  # diearea coordinates in int
    dy1 = int(x4)  # diearea coordinates in int

    width = int(x3) - int(x1)  # getting the width of the are lower left - upper right
    height = int(x4) - int(x2)  # getting the hihgt of the are lower left - upper right
    clip = draw.ClipPath()
    d = draw.Drawing(width, height, origin=(0, - height), id="svgContainer")  # drawing of diearea
    d.append(draw.Rectangle(dx0, -(height + dy0), width, height, fill='#D8FEEA', fill_opacity=0.4, ))

    # parsing the lef file

    lef_parser = LefParser(path)  # getting the lef file path
    lef_parser.parse()

    x = ""
    for i in lef:  # putting lef infrmation in list
        x = x + i + " "
    lef_info = x.split()
    # print(lef_info)

    k = 0
    # g = ""

    counter = 0

    for i in range(0, len(MACRO)):  # for loop for drawing of components

        if k < len(MACRO):  # if we still have macro we keep drawing
            g = draw.Group()
            for j in range(0, len(lef_info)):  # loop on th size of the block in the LEF file on details of a macro
                if MACRO[k] == lef_info[j]:  # Matching macros from LEF / DEF
                    counter = counter + 1
                    # print(MACRO[k])
                    opacity = 0.6  # opacity of all rectangles, opacity only changes if OBS
                    xplacement = float(
                        MACRO[k + 1])  # extracting and storing placement and orientation of macro from DEF
                    yplacement = float(MACRO[k + 2])
                    orientation = MACRO[k + 3]
                    endindx = lef_info.index("END", j)  # Extracting macros's details
                    for m in range(j, endindx):
                        if (lef_info[m] == "Size"):
                            swidth = float(lef_info[m + 1]) * 100  # width size of macro
                            sheight = float(lef_info[m + 2]) * 100  # height width size of macrp
                            d.append(draw.Rectangle(xplacement - dx0, -(height - (yplacement - dy0)), swidth, sheight,
                                                    fill='#a877f2', stroke='#412f5c', stroke_width=10, fill_opacity=0.2,
                                                    class_="cell", name=MACRO[k], id=MACRO[k] + "_c" + str(counter)))
                        elif (lef_info[m] == "Layer:" or lef_info[m] == "Layer" or lef_info[m] == "LAYER"):  # Layer
                            met = lef_info[m + 1]
                            if (lef_info[m + 1] == "metal1"):
                                # COLOR CODE For each metal
                                color = "#7D5AB1"
                            elif (lef_info[m + 1] == "metal2"):
                                # COLOR CODE For each meta2
                                color = "#8C8E8E"
                            elif (lef_info[m + 1] == "metal3"):
                                # COLOR CODE For each meta3
                                color = "#FF839D"
                            elif (lef_info[m + 1] == "metal4"):
                                # COLOR CODE For each meta4
                                color = "#83C9FF"
                            elif (lef_info[m + 1] == "via1"):
                                # COLOR CODE For each via1
                                color = "#83FFC3"
                            elif (lef_info[m + 1] == "via2"):
                                # COLOR CODE For each via2
                                color = "#FFD683"
                            elif (lef_info[m + 1] == "via3"):
                                # COLOR CODE For each via3
                                color = "#83FFE1"
                        elif ((lef_info[m] == "PIN:")):
                            # metal info
                            met = lef_info[m + 1]
                            # pin info
                            pin = lef_info[m + 1]  # PIN NAME
                        elif ((lef_info[m] == "OBS")):  # setting different opacity for rectangles
                            met = lef_info[m + 1]
                            opacity = 0.6
                        elif ((lef_info[m] == "RECT")):  # extracting dimensions of rectangles in LEF
                            # x left
                            x0 = float(lef_info[m + 1]) * 100
                            # y left
                            y0 = float(lef_info[m + 2]) * 100
                            # x right
                            x01 = float(lef_info[m + 3]) * 100
                            # y right
                            y01 = float(lef_info[m + 4]) * 100
                            # width of the rects
                            rwidth = x01 - x0  # width of rectangle
                            # height of the rects
                            rheight = y01 - y0  # height of rectangle
                            if (orientation == "N"):
                                g.append(
                                    draw.Rectangle(xplacement - dx0 + x0, -(height - (yplacement - dy0 + y0)), rwidth,
                                                   rheight, fill=color, fill_opacity=opacity, class_=met))
                                g.append(draw.Text(pin, 20, xplacement - dx0 + x0, -(height - (yplacement - dy0 + y0)),
                                                   centre='origin', class_=met))
                            elif (orientation == "FN"):
                                FNx = x0 + ((swidth / 2 - x0) * 2) - rwidth
                                g.append(
                                    draw.Rectangle(xplacement - dx0 + FNx, -(height - (yplacement - dy0 + y0)), rwidth,
                                                   rheight, fill=color, fill_opacity=opacity, class_=met))
                                g.append(draw.Text(pin, 20, xplacement - dx0 + FNx, -(height - (yplacement - dy0 + y0)),
                                                   centre='origin', class_=met))
                            elif (orientation == "FS"):
                                FSy = y0 + ((sheight / 2 - y0) * 2) - rheight
                                g.append(
                                    draw.Rectangle(xplacement - dx0 + x0, -(height - (yplacement - dy0 + FSy)), rwidth,
                                                   rheight, fill=color, fill_opacity=opacity, class_=met))
                                g.append(draw.Text(pin, 20, xplacement - dx0 + x0, -(height - (yplacement - dy0 + FSy)),
                                                   centre='origin', class_=met))
                            elif (orientation == "S"):
                                Sx = x0 + ((swidth / 2 - x0) * 2) - rwidth
                                Sy = y0 + ((sheight / 2 - y0) * 2) - rheight
                                g.append(
                                    draw.Rectangle(xplacement - dx0 + Sx, -(height - (yplacement - dy0 + Sy)), rwidth,
                                                   rheight, fill=color, fill_opacity=opacity, Class=met))
                                g.append(draw.Text(pin, 35, xplacement - dx0 + Sx, -(height - (yplacement - dy0 + Sy)),
                                                   centre='origin', class_=met))
            d.append(g)
            k = k + 4

    nx = ""
    ny = ""

    for i in range(0, len(nets)):  # for loop to draw vias
        if (nets[i] == "M2_M1" or nets[i] == "M3_M2" or nets[i] == "M4_M3"):
            ny = nets[i - 1]
            nx = nets[i - 2]
            nx = int(nx.strip("[],"))
            ny = int(ny.strip("[],"))
            opacity = 0.5
            NETstartindx = lef_info.index(nets[i])
            if (nets[i] == "M2_M1" or nets[i] == "M3_M2"):
                NETendindx = lef_info.index("VIA", NETstartindx)
            elif (nets[i] == "M4_M3"):
                NETendindx = lef_info.index("Macro", NETstartindx)

            for n in range(NETstartindx, NETendindx):
                if (lef_info[n] == "LAYER"):  # Layer
                    if (lef_info[n + 1] == "metal1"):
                        color = "#7D5AB1"  # COLOR CODE For each metal
                    elif (lef_info[n + 1] == "metal2"):
                        # COLOR CODE For each meta2
                        color = "#8C8E8E"
                    elif (lef_info[n + 1] == "metal3"):
                        # COLOR CODE For each meta3
                        color = "#FF839D"
                    elif (lef_info[n + 1] == "metal4"):
                        # COLOR CODE For each meta4
                        color = "#83C9FF"
                    elif (lef_info[n + 1] == "via1"):
                        # COLOR CODE For each via1
                        color = "#83FFC3"
                    elif (lef_info[n + 1] == "via2"):
                        # COLOR CODE For each via2
                        color = "#FFD683"
                    elif (lef_info[n + 1] == "via3"):
                        # COLOR CODE For each via3
                        color = "#83FFE1"
                elif ((lef_info[n] == "RECT")):  # extracting dimensions of rectangles in
                    # x left
                    x0 = float(lef_info[n + 1]) * 100
                    # y left
                    y0 = float(lef_info[n + 2]) * 100
                    # xright
                    x01 = float(lef_info[n + 3]) * 100
                    # y right
                    y01 = float(lef_info[n + 4]) * 100
                    rwidth = x01 - x0  # width of rectangle
                    rheight = y01 - y0  # height of rectangle
                    d.append(draw.Rectangle(nx - dx0 + x0, -(height - (ny - dy0 + y0)), rwidth, rheight, fill=color,fill_opacity=opacity, class_=lef_info[n + 1]))

    i = 0
    RouteEnd = 0
    RouteStart = 0

    for i in range(0, len(nets)):
        # checking that am at metal components
        if (nets[i]=="NET_DEF:"):
            net_ident=nets[i+1]
            #g = draw.Group(fill="Black", Class="net", id=net_ident)
            g = draw.Group(fill="Black", Class="net", id=net_ident)

        if (nets[i] == "metal1" or nets[i] == "metal2" or nets[i] == "metal3" or nets[i] == "metal4" or nets[i]=="via1" or nets[i]=="via2"or nets[i]=="via3"):
            RouteStart = i

            if (nets[i] == "metal1"):
                met = nets[i]
                color = "#7D5AB1"  # COLOR CODE For each metal
                strokewidth = 0.6 * 100  # width of metal
            elif (nets[i] == "metal2"):
                # COLOR CODE For each meta2
                met = nets[i]
                color = "#8C8E8E"
                # width of meta2
                strokewidth = 0.6 * 100
            elif (nets[i] == "metal3"):
                met = nets[i]
                # COLOR CODE For each meta3
                color = "#FF839D"
                # width of meta3
                strokewidth = 0.6 * 100
            elif (nets[i] == "metal4"):
                met = nets[i]
                # COLOR CODE For each meta4
                color = "#83C9FF"
                # width of meta4
                strokewidth = 1.2 * 100
            elif (nets[i] == "via1"):
            # COLOR CODE For each via1
                met = nets[i]
                color = "#83FFC3"
            elif (nets[i] == "via2"):
                # COLOR CODE For each via2
                met = nets[i]
                color = "#FFD683"
            elif (nets[i] == "via3"):
                met = nets[i]
                # COLOR CODE For each via3
                color = "#83FFE1"

            # print(RouteStart)

            for j in range(i + 1, len(nets)):
                if (nets[j] == "M2_M1" or nets[j] == "M3_M2" or nets[j] == "M4_M3" or nets[j] == "metal1" or nets[j] == "metal2" or nets[j] == "metal3" or nets[j] == "metal4" or nets[j] == ";"):
                    RouteEnd = j
                    # print(RouteEnd)
                    break
            no_of_pairs = int((RouteEnd - RouteStart - 1) / 2)  # number of pairs of coordinates (x,y)
            temp = RouteStart

            if (no_of_pairs > 1):  # if number of pairs=1 , then only via and it's already drawn in previous loop

                for k in range(0, no_of_pairs - 1):  # extracting placement of wires and drawing routing
                    route_wirex0 = int(nets[temp + 1].strip("[],"))
                    route_wirey0 = int(nets[temp + 2].strip("[],"))
                    route_wirex1 = int(nets[temp + 3].strip("[],"))
                    route_wirey1 = int(nets[temp + 4].strip("[],"))
                    p = draw.Path(stroke_width=strokewidth, stroke=color, stroke_opacity=0.7, fill_opacity=0, id=met)
                    #g.append(draw.Rectangle(route_wirex1 - route_wirex0, route_wirey1 - route_wirey0,route_wirex0 - dx0, -(height  - (route_wirey0 - dy0)),stroke_width=strokewidth, stroke=color, stroke_opacity=0.7, fill_opacity=0,id = met))
                    #g.append(draw.Rectangle( route_wirex0 - dx0,
                                       #-(height - (route_wirey0 - dy0)),route_wirex1 - route_wirex0, route_wirey1 - route_wirey0, stroke_width=strokewidth, stroke=color,
                                       #stroke_opacity=0.7, fill_opacity=0, id=met))
                    p.M(route_wirex0 - dx0, -(height - (route_wirey0 - dy0)))  # Start path at point
                    p.l(route_wirex1 - route_wirex0, route_wirey1 - route_wirey0)  # Draw line to
                    g.append(p)
                    temp = temp + 2

                d.append(g)



    pin_info = []  # Contains the needed details to draw the pins
    splt = ""
    for keys, val in def_parser.pins.pin_dict.items():
        # print(keys)
        splt = str(val)
        # print(val)
        splt = splt.split()
        pin_info.append(splt[3])
        pin_info.append(splt[9].strip("[],"))
        pin_info.append(splt[10].strip("[],"))
        pin_info.append(splt[11].strip("[],"))
        pin_info.append(splt[12].strip("[],"))
        pin_info.append(splt[13].strip("[],"))
        pin_info.append(splt[15].strip("[],"))
        pin_info.append(splt[16].strip("[],"))
        pin_info.append(splt[17].strip("[],"))

    # print(pin_info)
    for b in range(0, len(pin_info)):
        if (pin_info[b] == "metal1" or pin_info[b] == "metal2" or pin_info[b] == "metal3" or pin_info[b] == "metal4"):
            pinx0 = int(pin_info[b + 1])
            piny0 = int(pin_info[b + 2])
            pinx1 = int(pin_info[b + 3])
            piny1 = int(pin_info[b + 4])
            pin_pos1 = int(pin_info[b + 5])
            pin_pos2 = int(pin_info[b + 6])
            pin_name = pin_info[b - 1]
            PINS = pin_name.replace('<', '')
            PINS = PINS.replace('>', '')
            d.append(draw.Rectangle(pin_pos1 - dx0, -(height - (pin_pos2 - dy0)), pinx1 - pinx0 + 200, piny1 - piny0 + 200,
                               fill='#B1725A', fill_opacity=0.6, Class="PIN", id=PINS))
            d.append(draw.Text(pin_name, 40, pin_pos1 - dx0, -(height - (pin_pos2 - dy0 - 20)), centre='origin',
                               Class="PINNames"))

        #drc_parser=[]
        #read_path = input("Enter DRC file path: ") #ENTER DRC FILE PATH HERE!
        drc = DRC_parser(path2)
        drc.parse()
        # x = drc_parser.DRC_parser()



    SVG = str(pth[-1]) + ".html"
    d.saveSvg("templates/" + SVG)  # draw svg image and give it a file name

    with open('htmlHead.txt', 'r') as file:
        Head = file.read()
    with open('htmlTail.txt', 'r') as file:
        Tail = file.read()
    with open("templates/" + SVG, 'r+') as f:
        content = f.read()
        contentX = content.replace(str(height), "950", 1)
        contentX = contentX.replace(str(width), "950", 1)
        f.seek(0, 0)
        f.write(Head + contentX + Tail)

    return SVG

