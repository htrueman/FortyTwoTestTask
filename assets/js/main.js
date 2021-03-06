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
    
    var req_table=document.getElementById('req_table');
    $(".req_pr").each(function(i, obj) {
        if (($(this).text() > 0) && sort == 'prior') {
           row_num++; 
        }
        else if (sort == 'prior_asc') {
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

    var row = req_table.insertRow(row_num);
    var cells = [];
    var rows = 7;
    var num = [0,1,2,3,4,5,6,7];
    if (auth == false) {
        rows = 6;
        num = [0,1,2,2,3,4,5,6];
    }
    for (i=-1; i<rows; i++) {
        cells.push(row.insertCell(i));
    }
    
    for(i=0;i<data.length;i++){
        cells[num[1]].innerHTML = data[i].fields.priority;
        if (auth == true) {
            cells[num[2]].innerHTML = 
                '<div class="form-group">\
                <form method="POST" \
                action="javascript:OnSubm(' + data[i].pk + ',' 
                + data[i].fields.priority + ');">\
                    <input type="hidden" name="csrfmiddlewaretoken" value="'+ token + '">'
                    + dj_form 
                    + '<button type="submit" id="submit_button" value="' + data[i].pk
                    + '" class="submit_button' + data[i].pk + ' btn btn-default">\
                    Submit\
                    </button>\
                </form>\
                </div><div class="err' + data[i].pk + '"></div>';
        }
        cells[num[3]].innerHTML = '<strong>' + data[i].fields.author + '</strong>';
        cells[num[4]].innerHTML = '#' + data[i].pk;
        cells[num[5]].innerHTML = data[i].fields.date;
        cells[num[6]].innerHTML = data[i].fields.method;
        cells[num[7]].innerHTML = data[i].fields.name;
        cells[num[0]].innerHTML = data[i].fields.status;
        row.className = 'request';
        cells[1].className = 'req_pr';
        row.id = data[i].pk;
    }
    update_items();
}
var title = $('title').text().replace(/\([0-9]+\)/, '');
var Active = 1;
function updateRequests(data){
    if (Active==0){
        count = count + data.length;
        $("title").text('('+count+')'+title);
   }
   last_id = data[0].pk;
}

$(window).focus(function() {
    $('title').text(title);
    count = 0;
    Active = 1;
});

$(window).blur(function() {
    Active = 0;
});

var link = $('a.sort_link').attr('href');
$(document).ready(function(){
    $("title").text('('+count+')'+title);
    setInterval(function(){
        $.ajax({
            url: link,
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