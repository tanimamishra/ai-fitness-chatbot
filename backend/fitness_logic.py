def get_fitness_response(message):

    message = message.lower()

    if "weight loss" in message:
        return "To lose weight, try doing cardio exercises for 30 minutes daily."

    elif "muscle" in message:
        return "For muscle gain, focus on strength training and eat high protein foods."

    elif "diet" in message:
        return "A healthy diet includes protein, vegetables, fruits and whole grains."

    elif "workout" in message:
        return "Beginner workout: push-ups, squats, lunges and 20 minutes cardio."

    else:
        return "Stay active and exercise regularly to maintain good fitness."
