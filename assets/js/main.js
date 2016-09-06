var count = 0;
var last_id = 0;
var pk = 0;
var row_num = 2;
function update_items(){
    var rowCount = $('#req_table tr').length;
    // one of the rows is row with title,
    // and one with columns titles so 
    // totaly must be no more then 12 rows
    if (rowCount > 12) {
      $('#req_table tr:last').remove();
    }
}

function OnSubm(pk, priority) {
    var pr = $("#form_req").val();
    $.ajax({
      'type': 'POST',
      'data': {
        'pk': pk,
        'priority': pr,
        'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
      },
      'beforeSend': function(){
        $('.submit_button').addClass('hidden');
        $("input").attr("disabled", "disabled");
      },

      'error': function(data){
        errors = JSON.parse(data.responseText);
        display_form_errors(errors, pk);
      },
      'success': function(){
        location.reload(true);
      },
      complete: function(){
        $('.hidden').removeClass('hidden');
        $("input").removeAttr("disabled");
    }
    });
}

function insRow(data)
{
    
    var x=document.getElementById('req_table');
    $(".req_pr").each(function(i, obj) {
        if (($(this).text() > 0) && window.location.pathname == '/requests/prior/') {
           row_num++; 
        }
        else if (window.location.pathname == '/requests/prior_asc/') {
            if ($('#req_table tr').length == 12) {
                row_num++; 
            }
            else if ($(this).text() == 0){
                row_num = $('#req_table tr').length;
            }
            else {
                row_num = $('#req_table tr').length - $(this).text().length
            }
        }
    });

    var row = x.insertRow(row_num);
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    var cell3 = row.insertCell(2);
    var cell4 = row.insertCell(3);
    var cell5 = row.insertCell(4);
    var cell6 = row.insertCell(5);
    var cell7 = row.insertCell(6);
    var cell8 = row.insertCell(-1);

    for(i=0;i<data.length;i++){
        cell1.innerHTML = data[i].fields.priority;
        cell2.innerHTML = '<div class="form-group"><form method="POST" action="javascript:OnSubm('
        + data[i].pk + ',' + data[i].fields.priority + ');"><input type="hidden" name="csrfmiddlewaretoken" value="'+ token + '">'
        + dj_form + '<button type="submit" id="submit_button" value="' + data[i].pk
        + '" class="submit_button' + data[i].pk + ' btn btn-default">Submit\
        </button></div><div class="err' + data[i].pk + '"></div></form>';
        cell3.innerHTML = '<strong>' + data[i].fields.author + '</strong>';
        cell4.innerHTML = '#' + data[i].pk;
        cell5.innerHTML = data[i].fields.date;
        cell6.innerHTML = data[i].fields.method;
        cell7.innerHTML = data[i].fields.name;
        cell8.innerHTML = data[i].fields.status;
        row.className = 'request';
        cell1.className = 'req_pr';
        row.id = data[i].pk;
    }
    update_items();
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

        });
    }
    , 2000);

});