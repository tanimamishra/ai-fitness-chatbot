# AI Fitness Chatbot

This project is an AI Fitness Chatbot built using LLM and Cloud technologies.

## Features
- Fitness advice chatbot
- Workout suggestions
- Diet recommendations
- Simple chatbot interface

## Technologies Used
- HTML
- JavaScript
- LLM (to be integrated)
- Cloud deployment (planned)

## Project Purpose
This project is developed for the Emerging Technology Lab project.

## Contributors
- Isha Sharma
- Tanima Mishra

## Backend

The backend of this project is built using **Flask (Python)**.

### API Endpoints

1. **Home Endpoint**

Route:
/
Description:
Checks if the backend server is running.

2. **Health Endpoint**

Route:
/health

Description:
Returns the status of the backend server.

Example response:
{
 "status": "Backend is running"
}

3. **Chat Endpoint**

Route:
/chat

Method:
POST

Description:
Receives a fitness question from the user and returns a chatbot response.

Example request:
{
 "message": "suggest workout"
}

Example response:
{
 "reply": "A beginner workout plan: push-ups, squats, lunges, planks, and 20 minutes of cardio."
}
