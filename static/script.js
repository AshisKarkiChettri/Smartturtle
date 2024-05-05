document.addEventListener("DOMContentLoaded", function() {
    const conversation = document.getElementById("conversation");
    const userInput = document.getElementById("userInput");
    const sendButton = document.getElementById("sendButton");

    function appendMessage(className, message) {
        const messageElement = document.createElement("div");
        messageElement.classList.add("message", className);
        messageElement.textContent = message;
        conversation.appendChild(messageElement);
    }

    function sendMessageToBackend(userInput) {
        fetch('http://<your-ngrok-url>/api', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ user_input: userInput })
        })
        .then(response => response.json())
        .then(data => {
            // Display bot response
            appendMessage("bot-message", data.response);
            // Handle the response from the backend
            // Here you can add code to handle the character count image if needed
        })
        .catch(error => console.error('Error:', error));
    }

    function sendMessage() {
        const message = userInput.value.trim();
        if (message === "") return;

        // Display user message
        appendMessage("user-message", message);
        userInput.value = "";

        // Send message to backend
        sendMessageToBackend(message);
    }

    sendButton.addEventListener("click", sendMessage);

    userInput.addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            sendMessage();
        }
    });
});
