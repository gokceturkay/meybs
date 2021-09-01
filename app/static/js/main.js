var inCooldown = 0
var myKey = 27

$( document ).on( 'keydown',( function ( e ) {

    function sleep(time){
        return new Promise((resolve) => setTimeout(resolve, time));
    }

    if ( e.keyCode === myKey ) {
        myKey = 0

        sleep(10).then(() => {
            inCooldown = 1;
        })

        sleep(2000).then(() => {
            inCooldown = 0;
            myKey = 27
        })
    }

}));

var switchted = 0
var btn = $('#layer-switch')

$( document ).on( 'keydown',( function ( e ) {
    var esc = 27
    if (inCooldown === 0) {
        if (switchted === 0) {
            if (e.keyCode === esc) {
                $('#wall').fadeIn();
                $('#menu').delay("350").fadeIn();
                $('.navbar-brand').delay("350").addClass('text-white').addClass('position-fixed');
                btn.prop('disabled', true);
                setTimeout(function () {
                    btn.prop('disabled', false);
                }, 600);
                switchted = 1
            }
        } else if (switchted === 1) {
            if (e.keyCode === esc) {
                $('#menu').delay("100").fadeOut();
                $('#wall').delay("200").fadeOut();
                $('.navbar-brand').delay("200").removeClass('text-white').removeClass('position-fixed');
                btn.prop('disabled', true);
                setTimeout(function () {
                    btn.prop('disabled', false);
                }, 400);
                switchted = 0
            }
        }
    }
}));

$(document).ready(function(){

    $('#layer-switch').click(function () {
        if (switchted === 0) {
            $('#wall').fadeIn();
            $('#menu').delay("350").fadeIn();
            $('.navbar-brand').delay("350").addClass('text-white');
            btn.prop('disabled', true);
            setTimeout(function () {
                btn.prop('disabled', false);
            },600);
            switchted = 1
        }else if(switchted === 1){
            $('#menu').delay("100").fadeOut();
            $('#wall').delay("200").fadeOut();
            $('.navbar-brand').delay("200").removeClass('text-white');
            btn.prop('disabled', true);
            setTimeout(function () {
                btn.prop('disabled', false);
            },400);
            switchted = 0
        }
    });

});