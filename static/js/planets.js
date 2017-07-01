$('#residentModal').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget)
  var residents = button.data('info') 
  var planet = button.data('planet')
  var modal = $(this)
  modal.find('.modal-title').text('Residents of ' + planet)
  modal.find('.modal-body').text(residents)
})