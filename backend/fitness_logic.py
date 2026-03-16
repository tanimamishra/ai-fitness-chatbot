def get_fitness_response(message):

    message = message.lower()

    if "weight loss" in message:
        return "For weight loss, do cardio 30 minutes daily and maintain a calorie deficit."

    elif "muscle" in message:
        return "For muscle gain, focus on strength training and increase protein intake."

    elif "diet" in message:
        return "A balanced diet should include protein, vegetables, healthy fats and complex carbs."

    elif "workout" in message:
        return "Beginner workout: pushups, squats, lunges and light cardio."

    else:
        return "Stay active, exercise regularly and maintain a healthy diet."
