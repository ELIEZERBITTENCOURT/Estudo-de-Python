function sendMessage() {
    var userMessage = document.getElementById('user-input').value;
    document.getElementById('chat').innerHTML += '<div class="user-message">' + userMessage + '</div>';
    document.getElementById('user-input').value = '';

    fetch('/get_response', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'user_message=' + encodeURIComponent(userMessage),
    })
    .then(response => response.json())
    .then(data => {
        var botResponse = data.bot_response;
        document.getElementById('chat').innerHTML += '<div class="bot-message">' + botResponse + '</div>';
    });
}
