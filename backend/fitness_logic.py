def get_fitness_response(message):

    message = message.lower()

    if "weight loss" in message or "lose weight" in message:
        return "For weight loss, combine cardio exercises like running or cycling with a calorie deficit diet."

    elif "muscle" in message or "muscle gain" in message:
        return "For muscle gain, focus on strength training exercises like push-ups, squats, and weight lifting."

    elif "diet" in message:
        return "A healthy diet should include protein, vegetables, fruits, whole grains, and adequate water."

    elif "workout" in message or "exercise" in message:
        return "A beginner workout plan: push-ups, squats, lunges, planks, and 20 minutes of cardio."

    elif "bmi" in message:
        return "BMI can be calculated using the formula: weight (kg) / height (m)^2."

    else:
        return "I am your AI Fitness Coach. Ask me about workouts, diet, muscle gain, or weight loss."
