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
      if(json.fields.artist_type === 1){
        $("#artistMembers").text(`Integrantes: ${json.fields.members}`)
        $("#artistMembers").show()
      }else {
        $("#artistMembers").text(``)
        $("#artistMembers").hide()
      }
      modalDOM.foundation('open')
    },
    error: function(){
      alert("Error buscando al artista");
    }
  });
}

function deleteArtist(id){
  console.log(id)
  Swal.fire({
    title: '¿Estas seguro?',
    text: "Esta acción es irreversible",
    type: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Si, borrar'
  }).then((result) => {
    if (result.value) {
      $.ajax({
        url: `/records/artists/delete/${id}`,
        method: 'GET',
        success: function(response){
          console.log(response)
          Swal.fire(
            'Deleted!',
            'Your file has been deleted.',
            'success'
          )
          window.location.reload()
        },
        error: function(){
          alert("Error buscando al artista");
        }
      });
    }
  })
}