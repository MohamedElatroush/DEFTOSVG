
 
$( document ).ready(function() {
    
    $( ".cell" ).each(function() {
        $("#selectCell").append(new Option($(this).attr('id'), $(this).attr('id')));
    });
    
    $( ".net" ).each(function() {
        $("#selectCell").append(new Option($(this).attr('id'), $(this).attr('id')));
    });
    
    $( ".PIN" ).each(function() {
        $("#selectCell").append(new Option($(this).attr('id'), $(this).attr('id')));
    });
    
    

    $('body').on('mouseover', '.cell', function() {
        $('#cellViewer').html($(this).attr('id'));
    });
    $('body').on('change', 'input[type="checkbox"]', function(){
        var c = $(this).attr('id');
        $('.'+ c).toggle();
    });
});

/*
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

 var select = $("#selectCell"); 
    var cell = $(".cell");
    for(var i = 0; i < cell.length; i++) {
        var opt = cell[i];
        var el = document.createElement("option");
        el.textContent = opt;
        el.value = opt;
        select.appendChild(el);
    }​

    var select2 = $("#selectNet"); 
    var net = $(".net");
    for(var i = 0; i < net.length; i++) {
        var opt = net[i];
        var el = document.createElement("option");
        el.textContent = opt;
        el.value = opt;
        select2.appendChild(el);
    }​
    
    var select3 = $("#selectPin"); 
    var pin = $(".PIN");
    for(var i = 0; i < pin.length; i++) {
        var opt = pin[i];
        var el = document.createElement("option");
        el.textContent = opt;
        el.value = opt;
        select3.appendChild(el);
    }​

*/ 