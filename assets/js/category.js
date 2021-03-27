$(document).ready(function (){
    $('.grid').on('click', function (){
        $('.grid-view').removeClass('d-none');
        $('.list-view').addClass('d-none');
    });
    $('.list').on('click', function (){
        $('.list-view').removeClass('d-none');
        $('.grid-view').addClass('d-none');
    });
});