$(function(){
  fetchArtistTypes()
  $('#artist_type').change(function() {
    $('#members_row').toggle($(this).val() == 1)
  });
});

function fetchArtistTypes(){
  $.ajax({
    url: '/records/artisttype',
    method: 'GET',
    success: function(response) {
      let artistTypeDOM = $('#artist_type')
      artistTypeDOM.html('')
      let types = JSON.parse(response)
      let type = {}
      let optionHTML = ''
      let i = 0
      for(i = 0; i < types.length; ++i){
        type = types[i]
        optionHTML = `<option value="${type.pk}">${type.fields.name}</option>`
        artistTypeDOM.append(optionHTML)
      }
      $('#members_row').toggle(types[0].pk == 1)
    }, error:function(a,b,c){
      console.log(a)
      console.log(b)
      console.log(c)
    }
  });
}