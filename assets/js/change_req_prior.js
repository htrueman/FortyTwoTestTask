

$(document).ready(function(){
var pk = 0;
    function OnSubmit(id) {
        pk = $('.submit_button' + id).val();
        var $frm = $('#'+pk);
        $.ajax({
            type: "POST",
            url: "/requests/",
            global: false,
            data: $frm.serialize() + '&pk=' + pk,
            beforeSend: function(){
                $('.submit_button').addClass('hidden');
                $("input").attr("disabled", "disabled");
            },
            success: function(){
                location.reload(true);
            },
            error: function(data){
                errors = JSON.parse(data.responseText);
                display_form_errors(errors, pk);
            },
            complete: function(){
                $('.hidden').removeClass('hidden');
                $("input").removeAttr("disabled");
            }
        });
    }
function display_form_errors(errors, pk) {
    for (var k in errors) {
         $('.err'+pk).after('<div class="error">' + errors[k] + '</div>');
         setTimeout(function() {
              $('.error').hide();
         }, 2000);
    }
}
});