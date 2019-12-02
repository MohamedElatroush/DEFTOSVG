$( document ).ready(function() {

    //zooming and panning feature
    var options = {
        panEnabled: true
       , controlIconsEnabled: false
       , zoomEnabled: true
       , dblClickZoomEnabled: true
       , mouseWheelZoomEnabled: true
       , preventMouseEventsDefault: true
       , zoomScaleSensitivity: 0.2
       , minZoom: 1
       , maxZoom: 10
       , fit: true
       , contain: true
       , center: true
       , refreshRate: 'auto'
       }
     var svgElement = document.querySelector('#svgContainer');
     var panZoomTiger = svgPanZoom(svgElement,options);


    //searchable list generation
    $( ".cell" ).each(function() {
        $("#selectCell").append(new Option($(this).attr('id'), $(this).attr('id')));
    });
    
    $( ".net" ).each(function() {
        $("#selectCell").append(new Option($(this).attr('id'), $(this).attr('id')));
    });
    
    $( ".PIN" ).each(function() {
        $("#selectCell").append(new Option($(this).attr('id'), $(this).attr('id')));
    });
    
    
    //hovering feature
    $('body').on('mouseover', '.cell', function() {
        $('#cellViewer').html($(this).attr('id'));
    });

    //enabling visibility feature
    $('body').on('change', 'input[type="checkbox"]', function(){
        var c = $(this).attr('id');
        $('.'+ c).toggle();
    });
});

