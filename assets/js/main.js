var count = 0;
var last_id = 0;
function update_items(){
    while($('.request').length>10){
        $('.request:last').remove();
    }
}
var Active = 1;
function updateRequests(data){
   if (Active==0){
    count = count + data.length;
    $("title").html('('+count+')' + ' Name');
   }
   last_id = data[0].pk;
   for(i=0;i<data.length;i++){
       var insert = '<div class="request">' +
                      '<strong>' + data[i].fields.author + '  ' + '</strong>' +
                      '#' + data[i].pk + '  ' +
                      data[i].fields.date + '  ' +
                      data[i].fields.method + '  ' +
                      data[i].fields.name + '  ' +
                      data[i].fields.status + '  ' + '</div>';
       $(insert).insertBefore($('.request:first'));
   }
   update_items();
}

$(window).focus(function() {
    $("title").html('Name');
    count = 0;
    Active = 1;
});

$(window).blur(function() {
    Active = 0;
});

$(document).ready(function(){
    $("title").html('('+count+')' + ' Name');
    setInterval(function(){
        $.ajax({
            url: '/requests/',
            data: {'last_unread_item': last_id},
            dataType: 'json',
            success: function(data){
                if(data.length){updateRequests(data);
                };
            }
        });}
    , 2000);
});