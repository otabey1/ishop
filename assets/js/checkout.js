$(document).ready(function (){
    $('.one').on('click', function (){
        $('.credit-card-display').removeClass('d-none');
        $('.paypal-display').addClass('d-none');
        $('.bitcoin-display').addClass('d-none');
    });
    $('.two').on('click', function (){
        $('.paypal-display').removeClass('d-none');
        $('.credit-card-display').addClass('d-none');
        $('.bitcoin-display').addClass('d-none');
    });
    $('.three').on('click', function (){
        $('.bitcoin-display').removeClass('d-none');
        $('.paypal-display').addClass('d-none');
        $('.credit-card-display').addClass('d-none');
    });
});
