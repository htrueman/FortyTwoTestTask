var count = 0;
var last_id = 0;
function update_items(){
    var rowCount = $('#req_table tr').length;
    // one of the rows is row with title,
    // and one with columns titles so 
    // totaly must be no more then 12 rows
    if (rowCount > 12) {
      $('#req_table tr:last').remove();
    }
}
function insRow(data)
{
    var x=document.getElementById('req_table');
    var row = x.insertRow(2);
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    var cell3 = row.insertCell(2);
    var cell4 = row.insertCell(3);
    var cell5 = row.insertCell(4);
    var cell6 = row.insertCell(-1);

    for(i=0;i<data.length;i++){
        cell1.innerHTML = '<strong>' + data[i].fields.author + '</strong>';
        cell2.innerHTML = '#' + data[i].pk;
        cell3.innerHTML = data[i].fields.date;
        cell4.innerHTML = data[i].fields.method;
        cell5.innerHTML = data[i].fields.name;
        cell6.innerHTML = data[i].fields.status;
        row.className = 'request';
        row.id = data[i].pk;
    }
    update_items()
}
var Active = 1;
function updateRequests(data){
   if (Active==0){
    count = count + data.length;
    $("title").html('('+count+')' + ' Name');
   }
   last_id = data[0].pk;
   
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
                if(data.length){
                  updateRequests(data);
                  insRow(data);
                };
            }
        });}
    , 2000);
});