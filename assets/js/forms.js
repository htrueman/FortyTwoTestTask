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
            window.location.replace("/"); // redirect user to contacts page after
            // successful data saving
            setTimeout(function(){$('#message').text('');}, 2000);
        }
        });
        return false;
    });
});

function display_form_errors(errors, $form) {
     for (var k in errors) {
         $form.find('input[name=' + k + ']').after('<div class="error">' + errors[k] + '</div>');
         setTimeout(function() {
              $('.error').hide();
         }, 3000);
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