function sendMessage(){

let userMessage = document.getElementById("userInput").value.toLowerCase();

let response = "";

if(userMessage.includes("weight loss")){
response = "For weight loss: do cardio 30 minutes daily and maintain a calorie deficit.";
}

else if(userMessage.includes("muscle")){
response = "For muscle gain: focus on strength training and eat high protein foods.";
}

else if(userMessage.includes("diet")){
response = "A balanced diet includes protein, healthy fats, and complex carbs.";
}

else{
response = "Stay active, exercise regularly, and maintain a healthy diet.";
}

let chatMessages = document.getElementById("chatMessages");

// user message
let userMsg = document.createElement("p");
userMsg.className = "user-message";
userMsg.innerText = userMessage;
chatMessages.appendChild(userMsg);

// bot message
let botMsg = document.createElement("p");
botMsg.className = "bot-message";
botMsg.innerText = "AI Fitness Coach: " + response;
chatMessages.appendChild(botMsg);

document.getElementById("userInput").value = "";

}
