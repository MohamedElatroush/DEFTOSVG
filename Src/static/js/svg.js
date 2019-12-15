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

    $('.metal1').toggle();
    $('.metal2').toggle();
    $('.metal3').toggle();
    $('.metal4').toggle();
    $('.via1').toggle();
    $('.via2').toggle();
    $('.via3').toggle();
    //$('.PIN').toggle();
    //$('.PINNames').toggle();

    //searchable list generation
    $( ".cell" ).each(function() {
        if($("#selectCellType option[value="+$(this).attr('name')+"]").length <= 0)
            $("#selectCellType").append(new Option($(this).attr('name'), $(this).attr('name')));
    });

    $( ".cell" ).each(function() {
        $("#selectCell").append(new Option($(this).attr('id'), $(this).attr('id')));
    });
    
    $( ".net" ).each(function() {
        $("#selectNet").append(new Option($(this).attr('id'), $(this).attr('id')));
    });
    
    $( ".PIN" ).each(function() {
        $("#selectPin").append(new Option($(this).attr('id'), $(this).attr('id')));
    });

    $("#selectCellType").select2();
    $("#selectCell").select2();
    $("#selectNet").select2();
    $("#selectPin").select2();

    $('#selectCellType').on('change', function() {
        if($("#selectCell").val()=="None")
        {
            $(".cell").css({fill:"#a877f2",fill_opacity:0.2,stroke_width:10});
        }
        $("rect[name="+$("#selectCellType").val()+"]").css({fill:"#ffff00",fill_opacity:1,stroke_width:20});
    });


    $('#selectCell').on('change', function() {
            if($("#selectCell").val()=="None")
            {
                $(".cell").css({fill:"#a877f2",fill_opacity:0.2,stroke_width:10});
            }
            $("#" + $("#selectCell").val()).css({fill:"#ffff00",fill_opacity:1,stroke_width:20});
    });

    $('#selectNet').on('change', function() {
        if($("#selectNet").val()=="None")
        {
            $(".net").css({stroke:"#ffff00", "stroke-width":0});
        }
        $("#" + $("#selectNet").val()).css({stroke:"#ffff00", "stroke-width":10});
    });

    $('#selectPin').on('change', function() {
        if($("#selectPin").val()=="None")
        {
            $(".PIN").css({fill:'#B1725A'});
        }
        $("#" + $("#selectPin").val()).css({fill:"#ffff00"});
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

