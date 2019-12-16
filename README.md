#  Web-based Layout Viewer

## Technical Aspects

1. Given the LEF and DEF files browsed by the user, the website calls a function generating and SVG file by parsing the files and generating the corresponding SVG file.

2. The function is called using Flask python library to serve as the backend framework of the website to take the file names as inputs from the user and call the SVG generation function.

3. The website is offering the user the following features to be executed on the frondend of the website using jQuery, HTML, and CSS:

    • Zooming and Panning: using svg-pan-zoom library: https://github.com/ariutta/svg-pan-zoom#svg-pan-zoom-library  
    • Display the cell type and instance name (type/name) when you hoover over the cell  
    • Provide an interface to search and highlight: by generating the corresponding searchable lists using jQuery  
    • Highlight the areas that have DRC violations


## How to Build and Run
To run this website locally, clone the repo and run the server.py file in the src folder of the main directory using the command
```
python server.py
```
Now head over to your localhost, or http://127.0.0.1:5000/, the main web page should display. 

## Dependencies
Flask  
drawSvg  
Regular Expression Operations (regex)  
Lef_parser  
Def_parser  
Lef_util  
Def_util  

## Limitations
Slower response with enabling layers when circuit size gets higher

## Future Work
Enhancing GUI and response time with large circuits  
Developing a built-in DRC violations generator  
Adding animations, styles, and stripples  

## Acknowledgement
We would like to express our very great appreciation to The American University in Cairo (AUC) for its continuous support, and the Digital Design II Course, under the supervision of Professor Mohamed Shalan.

## References

https://github.com/ariutta/svg-pan-zoom#svg-pan-zoom-library  
http://flask.palletsprojects.com/en/1.1.x/  
https://api.jquery.com/  


