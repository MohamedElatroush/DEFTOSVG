# DEFTOSVG

  We used a given python def and lef file parsers to parse the needed data for generating the SVG file that handles drawing the layouts. Verification is done by comparing our output to an output from Klayout. We used the drawSVG library in python to handle drawing the cells/nets/pins...etc. 
  
  The program asks the user to enter the DEF file path, as well as the LEF file path. After extracting the needed information we called functions from drawSVG library to draw the rectangles representing the cells as well as the routing wires and pins. A for loop is created to match the name of a macro from the DEF (including the placement) to the same cell name in the LEF file to know the exact dimensions of the rects, many flags were created to identify which metal layer to use, or OBS if exists. Different loops with the same logic are created, such as the pins, as well as nets to perform routing on our design. 
