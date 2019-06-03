$(function(){
});

function detailsArtist(id){
  console.log(id)
  $.ajax({
    url: `/records/artists/${id}`,
    method: 'GET',
    success: function(response){
      console.log(response)
      let json = JSON.parse(response)
      json = json.pop()
      let modalDOM = $('#detailsModal')
      $("#artistTitle").text(`${json.fields.name}`)
      $("#artistType").text(`${json.fields.artist_type == 1? "Band":"Solo"}`)
      $("#artistOriginCountry").text(`País de origen: ${json.fields.origin_country}`)
      $("#artistFoundingDate").text(`Fecha de inicio: ${json.fields.founding_date}`)
      $("#artistMembers").show(json.fields.artist_type == 1)
      if(json.fields.artist_type == 1){
        $("#artistMembers").text(`Integrantes: ${json.fields.members}`)
      }
      modalDOM.foundation('open')
    },
    error: function(){
      alert("Error buscando al artista");
    }
  });
}