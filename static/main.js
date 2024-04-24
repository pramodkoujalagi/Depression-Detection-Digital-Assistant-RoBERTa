$(document).ready(function() {
    $('#sentiment-form').on('submit', function(event) {
        event.preventDefault();
        var message = $('#message').val();
        $.ajax({
            url: '/predict',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ 'message': message }),
            success: function(data) {
                $('#sentiment-result').html('Sentiment: ' + data.sentiment);
            },
            error: function(xhr, status, error) {
                console.error(xhr.responseText); // Log any errors to the console
            }
        });
    });
});
