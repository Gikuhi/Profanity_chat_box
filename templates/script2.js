function sendMessage() {
    var messageInput = document.getElementById('message-input');
    var message = messageInput.value.trim();

    if (message === '') {
        return;
    }

    // Clear the input field
    messageInput.value = '';

    // Send the message to the server
    fetch('/send_message', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'message=' + encodeURIComponent(message),
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Display the message in the chat container
            var messageContainer = document.getElementById('message-container');
            var newMessage = document.createElement('div');
            newMessage.textContent = message;
            messageContainer.appendChild(newMessage);
        } else {
            alert(data.message);
        }
    })
    .catch(error => {
        console.error('Error sending message:', error);
    });
}
