$(function(){
    $('.filter').click(function(){
        $(this).addClass('active').siblings().removeClass('active');
        let valor = $(this).attr('data-nombre');
        if (valor === 'todos'){
            $('.cont-work').show('1000');
        }else{
            $('.cont-work').not('.'+valor).hide('1000');
            $('.cont-work').filter('.'+valor).show('1000');
        }
    });

    let equipo = $('#equipo').offset().top,
        servicio = $('#quienes').offset().top,
        trabajo = $('#productos').offset().top,
        ofertas = $('#ofertas').offset().top,
        contacto = $('#contacto').offset().top;
        


    window.addEventListener('resize', function(){
        let equipo = $('#equipo').offset().top,
            quienes= $('#quienes').offset().top,
            trabajo = $('#productos').offset().top,
            ofertas = $('#ofertas').offset().top,
            contacto = $('#contacto').offset().top;
           
           
    });

    $('enlace-inicio').on('click', function(e){
        e.preventDefault();
        $('html, body').animate({
            scrollTop: 0
        }, 600);
    });

    $('#enlace-equipo').on('click', function(e){
        e.preventDefault();
        $('html, body').animate({
            scrollTop: equipo - 100
        }, 600);
    });

    $('#enlace-quienes').on('click', function(e){
        e.preventDefault();
        $('html, body').animate({
            scrollTop: servicio - 100
        }, 600);
    });

    $('#enlace-productos').on('click', function(e){
        e.preventDefault();
        $('html, body').animate({
            scrollTop: trabajo - 100
        }, 600);
    });

    $('#enlace-ofertas').on('click', function(e){
        e.preventDefault();
        $('html, body').animate({
            scrollTop: ofertas - 100
        }, 600);
    });

    $('#enlace-contacto').on('click', function(e){
        e.preventDefault();
        $('html, body').animate({
            scrollTop: contacto - 100
        }, 600);
    });

  
   

});