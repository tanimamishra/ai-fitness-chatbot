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

document.getElementById("response").innerText = "AI Fitness Coach: " + response;
document.getElementById("userInput").value = "";

}
