$(document).ready(function() {
    var URL = "http://localhost:8000/api/";

    $("#bot").click(function() {
        $.ajax({
            type: 'GET',
            url: URL + "auth/login/facebook",
            crossDomain: true,
            headers: { "Access-Control-Allow-Headers": "X-Requested-With, content-type" },
            //data: { get_param: 'code' },
            dataType: "json",

            success: function(respuesta) {
                console.log("dd" + respuesta);


            }
        })


    });

});