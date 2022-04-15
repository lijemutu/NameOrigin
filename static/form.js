$(document).ready(function () {
  $("#lastname").submit(function (event) {
    var formData = {
      name: $("#name").val(),
      type: $("#type").val(),
    };

    $.ajax({
      type: "GET",
      url: "/NameApi/partialname",
      data: formData,
    }).done(function (data) {
      console.log(data);
      var countries = data.countries;
      countries.forEach((country) =>
        $(".resultTablePartialName").append(
          "<tr>" +
            "<td>" +
            data.name +
            "</td>" +
            "<td>" +
            country.jurisdiction +
            "</td>" +
            "<td>" +
            country.incidence +
            "</td>" +
            "</tr>"
        )
      );
    });

    event.preventDefault();
  });

  $("#fullname").submit(function (event) {
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
      var name = data.forename;
      var secondName = data.surname;
      var countries = data.countries;
      if (data.hasOwnProperty("secondSurname")) {
        countries.forEach((country) =>
          $(".resultTableFullName").append(
            "<tr>" +
              "<td>" +
              name +
              " " +
              secondName +
              " " +
              data.secondsurname +
              "</td>" +
              "<td>" +
              country.jurisdiction +
              "</td>" +
              "<td>" +
              country.percent +
              "</td>" +
              "</tr>"
          )
        );
      } else {
        countries.forEach((country) =>
          $(".resultTableFullName").append(
            "<tr>" +
              "<td>" +
              name +
              " " +
              secondName +
              "</td>" +
              "<td>" +
              country.jurisdiction +
              "</td>" +
              "<td>" +
              country.percent +
              "</td>" +
              "</tr>"
          )
        );
      }
    });

    event.preventDefault();
  });

});

