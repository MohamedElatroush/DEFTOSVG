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
To run this website locally, clone the repo and run the server.py file using the command
```
python server.py
```
Now head over to http://127.0.0.1:5000/, the main web page should display. 

## What Has Been Done

1. Python SVG Generation Function
2. Flask Backend Handling
3. Zooming and Panning Feature
4. Cell Name Display on Hovering
5. Layers Enabling List of Checkboxes
6. Searchable Lists Generation
7. Searched Element Highlighting

## What is Left

1. DRC Violations Highlighting
2. Making a Bounding Rectangle for Each Cell, to make in invisible by default.

## References

https://github.com/ariutta/svg-pan-zoom#svg-pan-zoom-library


