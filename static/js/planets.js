$('#residentModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget)
    var apis = button.data('info').replace("]", "").replace("[", "").replace(/'/g, "").replace(/http/g, "https").split(",")
    var planet = button.data('planet')
    var modal = $(this)
    modal.find('.modal-title').text('Residents of ' + planet);
    $(".temp").remove();
    for (let i = 0; i < apis.length; i++) {
        $.getJSON(apis[i], function(response){
            if (response["height"] != "unknown") {
                 response["height"] = (parseInt(response["height"])/100).toString() + " meter"; 
            }
            if (response["mass"] != "unknown") {
                 response["mass"] = response["mass"] + " kg";
            }
            modal.find('.modal-body table').append("<tr class='temp'><td>" + response["name"] + "</td><td>" + response["height"] + "</td><td>" + response["mass"] + "</td><td>" + response["skin_color"] + "</td><td>" + response["hair_color"] + "</td><td>" + response["eye_color"] + "</td><td>" + response["birth_year"] + "</td><td>" + response["gender"] + "</td></tr>");
        });
    }  
})

$(".vote").on("click", function(){
    var button = $(this)
    planet = {'url': button.data('planet')}
    $(".alert").remove();
    $.ajax({
        type : 'POST',
        url : "/vote",
        contentType: 'application/json;charset=UTF-8',
        data : JSON.stringify(planet),
        success: function(response) {
            planet = JSON.parse(response)['planet']
            $("table").first().before("<div class='alert alert-success alert-dismissable'>"
                     + "<a href='#' class='close' data-dismiss='alert' aria-label='close'>&times;</a>"
                     + "<strong>Success! </strong> Your vote on " + planet + " has been registered.</div>");
        }
    });
 });
