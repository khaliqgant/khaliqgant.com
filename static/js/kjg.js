(function(){
    'use strict';

    /* global document */
    /* global responsiveNav */

    /**
     * Mobile Navigation classes
     */
    var nav = responsiveNav('.js-mobile-nav', {
        label: '',
        open: function(){
            document.getElementById('js-head').style.display = 'none';
        },
        close: function(){
            document.getElementById('js-head').style.display = 'block';
            document.getElementById('js-head').style.display = 'inline-block';
        }
    });


}());
