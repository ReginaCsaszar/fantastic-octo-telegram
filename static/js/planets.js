$('#residentModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget)
    var residents = button.data('info') 
    var planet = button.data('planet')
    var modal = $(this)
    modal.find('.modal-title').text('Residents of ' + planet)
    $(".temp").remove()
    apis = residents.replace("]", "").replace("[", "").replace(/'/g, "").split(",")
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
var modal = $(this)
    modal.find('.modal-title').text('Residents of ' + planet)