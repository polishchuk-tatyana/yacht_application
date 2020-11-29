$(document).ready(function(){
   var bron = $('#bron');
   console.log(bron);
   bron.on('submit', function (e){
      e.preventDefault();
      var submit_b = $('#submit_b');
      var yacht_id = submit_b.data("yacht_id");
      var yacht_model = submit_b.data("yacht_model");
      var yacht_paid = submit_b.data("yacht_paid");
      console.log(yacht_id, yacht_model,yacht_paid);

      var data = {};
      data.yacht_id = yacht_id;
      data.yacht_model = yacht_model;
      data.yacht_paid = yacht_paid;
      console.log(data);

      var csrf_token = $('#bron [name = "csrfmiddlewaretoken"]').val();
      data["csrfmiddlewaretoken"] = csrf_token;
      var url = bron.attr("action");

      $.ajax({
         url: url,
         type:'POST',
         data: data,
         cache: true,
         success: function (data){
            console.log("OK");
              console.log(data.nmb);
         },
         error: function (){
            console.log("error");
         }

      })
   })

});