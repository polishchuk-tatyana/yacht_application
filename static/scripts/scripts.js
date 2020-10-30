$(document).ready(function(){
   var izbr = $('#izbr');
   console.log(izbr);
   izbr.on('click', function (e){
      e.preventDefault();
      var yacht_id = izbr.data("yacht_id");
      var yacht_model = izbr.data("yacht_model");
      var yacht_paid = izbr.data("yacht_paid");
      var yacht_image = izbr.data("")
      console.log(yacht_id, yacht_model,yacht_paid);
   })

});