$('#statModal').on('show.bs.modal', function (event) {
    var modal = $(this)
    $(".voterows").remove();
    $.getJSON("/stat", function(response){
        var data = response['data']
        for (let i = 0; i < data.length; i++) {
            var row = data[i]
            modal.find('.modal-body table').append("<tr class='voterows'><td>" + row[1] + "</td><td>" + row[0] + "</td></tr>");
        }
    }); 
})