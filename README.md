#  Web-based Layout Viewer

## Technical Aspects

1. Given the LEF and DEF files browsed by the user, the website calls a function generating and SVG file by parsing the files and generating the corresponding SVG file.

2. The function is called using Flask python library that is used to serve for the backend of the website to take the file names as inputs from the user and call the SVG generation function.

3. The website is offering the user the following features to be executed on the frondend of the website using jQuery, HTML, and CSS:

    • Zooming and Panning: using svg-pan-zoom library: https://github.com/ariutta/svg-pan-zoom#svg-pan-zoom-library  
    • Display the cell type and instance name (type/name) when you hoover over the cell  
    • Provide an interface to search and highlight: by generating the corresponding searchable lists using jQuery  
    • Highlight the areas that have DRC violations


## What Has Been Done

1. Python SVG Generation Function
2. Flask Backend Handling
3. Zooming and Panning Feature
4. Cell Name Display on Hovering
5. Layers Enabling List of Checkboxes
6. Searchable Lists Generation 

## What is Left

1. DRC Violations Highlighting
2. Searched Element Highlighting

## References

https://github.com/ariutta/svg-pan-zoom#svg-pan-zoom-library


