$(document).ready(function() {
    $("#sendButton").click(function() {
        var query = $("#queryInput").val();

        $.ajax({
            type: "POST",
            url: "/send",
            contentType: "application/json",
            data: JSON.stringify({ "message": query }),
            success: function(data) {
                if (data.error) {
                    $("#outputArea").html("<p>Error: " + data.error + "</p>");
                } else {
                    $("#outputArea").html("<p>" + data.response + "</p>");
                }
            },
            error: function(xhr, status, error) {
                $("#outputArea").html("<p>Error: " + xhr.responseText + "</p>");
            }
        });
    });
});
