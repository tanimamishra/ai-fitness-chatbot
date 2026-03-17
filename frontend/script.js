async function sendMessage(){

    let userMessage = document.getElementById("userInput").value;

    let chatMessages = document.getElementById("chatMessages");

    // Show user message
    let userMsg = document.createElement("p");
    userMsg.className = "user-message";
    userMsg.innerText = userMessage;
    chatMessages.appendChild(userMsg);

    // Call backend API
    let response = await fetch("http://127.0.0.1:5000/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            message: userMessage
        })
    });

    let data = await response.json();

    // Show bot response
    let botMsg = document.createElement("p");
    botMsg.className = "bot-message";
    botMsg.innerText = "AI Fitness Coach: " + data.reply;
    chatMessages.appendChild(botMsg);

    // Clear input
    document.getElementById("userInput").value = "";
}
