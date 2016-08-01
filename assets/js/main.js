$(document).ready(function(){
    endlessFetching();
    $('body').mousemove(function(){
        dropTitleCounter();
    });;

});

function endlessFetching(){
    setTimeout(function() {newRequestsSince(getLastRequestId())}, 10000);
};

function getLastRequestId(){
    var lastId = /[0-9]+/.exec($("#0").children().attr('id'))[0];
    return lastId ? lastId : 0;
};

function newRequestsSince(since){
    $.ajax({
        url: "/requests/fetching/new",
        type: "GET",
        data: {"since": since},
    }).done(function(data){
        if (data['count'] > 0) {
            fetchNewRequests(data['count'])
        } else {
            endlessFetching()
        };
    });
};

function fetchNewRequests(count){
    console.log(Math.min(count,  maxRecordsPerPage()));
    $.ajax({
        url: "/requests/fetching/get",
        type: "GET",
        data: {'count': Math.min(count,  maxRecordsPerPage())},
    }).done(function(data){
        addUnreadedCount(data['requests'].length);
        refreshRequestsOnPage(data['requests']);
        endlessFetching();
    });
};

function refreshRequestsOnPage(requests){
    var delta = maxRecordsPerPage() - requests.length;
    $('.request').each(function(){
        var id = $(this).attr('id');
        if (id >= delta){
            $(this).remove();
        } else {
            $(this).attr('id', id + requests.length);
        }
    });

    requests.reverse().forEach(function(req, i, arr){
        var divId = requests.length - i - 1;
        $('<div/>',{
            'id': divId,
            'class':'request',
        }).prependTo('#requests');
        $('<div/>',{
            'id': req.pk,
            'text': '#'+req.pk+": "+req.date+" "+req.method+" "+req.path
        }).prependTo('#'+divId);
    });

};

function addUnreadedCount(delta){
    var currentCounter = /\([0-9]+\)/.exec($('title').text());
    var count = currentCounter ? parseInt(/[0-9]+/.exec(currentCounter)) + delta : delta;
    dropTitleCounter();
    var title = $('title').text();
    $('title').text('('+count+')'+title);
};

function dropTitleCounter(){
    var title = $('title').text().replace(/\([0-9]+\)/, '');
    $('title').text(title);
};

function maxRecordsPerPage(){
    return 10;
};