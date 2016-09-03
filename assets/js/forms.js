
var temp_err = [];

$(document).ready(function() {
    $('#form').submit(function() {
        var form = $('form')[0];
        var formData = new FormData(form);
        var $form = $(form);
        $.ajax({
            type: form.method,
            url: location.href,
            data: formData,
            contentType: false,
            processData: false,
            beforeSend: function(){
                $('#message').text('');
                $('.hidden').removeClass('hidden');
                var msg = 'Save changes...';
                $('#message').text(msg);
                $('#submit_button').addClass('hidden');
                $('#a_cancel').addClass('hidden');
                $("input").attr("disabled", "disabled");
                $("textarea").attr("disabled", "disabled");
        },
        xhr: function(){
            var xhr = $.ajaxSettings.xhr();
            xhr.upload.addEventListener('progress', function(evt){
                if(evt.lengthComputable) {
                    var percentComplete = Math.ceil(evt.loaded / evt.total * 100);
                    $('#progressbar').val(percentComplete).text('Loaded ' + percentComplete + '%');
                }
            }, false);
            return xhr;
        },
        success: function(data) {
            $('#message').text('');
            $('input').removeClass('error');
            var msg = 'Changes have been saved';
            $('#message').text(msg);
            for (i=0;i<temp_err.length;i++) {
                $('#' + temp_err[i]).remove();
            }
        },
        error: function(data) {
            errors = JSON.parse(data.responseText);
            display_form_errors(errors, $form);
        },
        complete: function(){
            $('.hidden').removeClass('hidden');
            $('#progressbar').addClass('hidden');
            $("input").removeAttr("disabled");
            $("textarea").removeAttr("disabled");
            setTimeout(function(){$('#message').text('');}, 2000);
            
        }
        });
        return false;
    });
});

function display_form_errors(errors, $form) {
     for (var k in errors) {
        if($("#" + k).length == 0) {
         $form.find('input[name=' + k + ']').after('<div class="error" id=' + k + '>' + errors[k] + '</div>');
         temp_err.push(k);
     }
     }
}
function ImagePreview(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $('img').css('max-width', 200);
            $('img').css('max-height', 200);
            $('.photo').removeClass('no-photo');
            $('img').attr('src', e.target.result);
            $('.no-img').addClass('img');
            $('.no-img').removeClass('no-img');
        };
        reader.readAsDataURL(input.files[0]);
    }
}


$(document).ready(function(){
    var id = 0;
    $("#id_photo").change(function(){
        ImagePreview(this);
        });
    });