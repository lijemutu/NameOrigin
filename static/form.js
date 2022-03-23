$(document).ready(function () {
    $("form").submit(function (event) {
      var formData = {
        fn: $("#fn").val(),
        sn: $("#sn").val(),
        ssn: $("#ssn").val(),
      };
  
      $.ajax({
        type: "GET",
        url: "/NameApi/name",
        data: formData,
      }).done(function (data) {
        console.log(data);
      });
  
      event.preventDefault();
    });
  });