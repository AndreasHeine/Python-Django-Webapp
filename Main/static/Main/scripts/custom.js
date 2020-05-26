'usestrict';

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        var cookies = document.cookie.split(";");
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Check if this cookie string begin with the name we want
            if (cookie.substring(0, name.length + 1) === (name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
             }
         }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
        }
    }
});

// POST-REQUEST
var postdata = function () {
    var data = {"toServer":"datafromcustom.js"};
    //console.log(data);
    $.ajax({
        method:"POST",
        url:"main/ajax/json",
        contentType:"application/json",
        data: JSON.stringify(data),
        dataType: "json",
        success: function(data) {
            //console.log(data);
        }
    });
};

// GET-REQUEST
var getdata = function () {
    var data;
    $.ajax({
        type: "GET",
        url: "main/ajax/json",
        data: data,
        async: true,
        beforeSend: function (xhr) {
            if (xhr && xhr.overrideMimeType) {
                xhr.overrideMimeType("application/json;charset=utf-8");
            }
        },
        dataType: "json",
        success: function (data) {
            document.getElementById("time").innerHTML = data["time_value"]; 
            //console.log(data);
        }
    });
};

// CYCLIC GET-REQUEST
// setInterval(getdata, 1000);
// setInterval(postdata, 2000);