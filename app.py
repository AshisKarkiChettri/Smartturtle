from flask import Flask, render_template, request
import random
import matplotlib.pyplot as plt

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/response', methods=['GET', 'POST'])
def response():
    # Dictionary of predefined responses
    responses = {
        "greeting": ["Hello!", "Hi there!", "Hey! How can I assist you today?"],
        "farewell": ["Goodbye!", "See you later!", "Have a great day!"],
        "joke": ["Why don't scientists trust atoms? Because they make up everything!",
                 "What do you get when you cross a snowman and a vampire? Frostbite!"],
        "advice": ["Remember to always backup your data!",
                   "If you encounter technical issues, try restarting your device.",
                   "Stay updated with the latest security patches and updates."],
        "small_talk": ["How's your day going?",
                       "Do you have any exciting plans for the weekend?",
                       "What's your favorite movie or TV show?"],
        "common_questions": {
            "weather": ["The weather today is sunny with a high of 40°C.",
                        "Expect partly cloudy skies with a chance of showers later in the day."],
            "time": ["It's currently 2:30 PM.", "The time is 10:45 AM."]
        },
        "trivia": ["Did you know that the Great Wall of China is the longest man-made structure in the world?",
                   "The human brain has a storage capacity equivalent to 2.5 petabytes of digital memory!"],
        "activity_suggestion": ["Why not go for a walk in the park?",
                                "How about trying out a new recipe?",
                                "You could watch a movie or read a book to unwind."],
        "motivational_quote": ["The only way to do great work is to love what you do. - Steve Jobs",
                               "Believe you can and you're halfway there. - Theodore Roosevelt"],
        "technology_trends": ["Artificial Intelligence and Machine Learning are revolutionizing various industries.",
                              "Blockchain technology has the potential to transform financial transactions and supply chain management."],
        "book_recommendation": ["I recommend 'The Alchemist' by Paulo Coelho.",
                                "You might enjoy reading 'Atomic Habits' by James Clear."],
        "healthy_habit_tip": ["Make sure to stay hydrated throughout the day.",
                              "Try to incorporate more fruits and vegetables into your diet for better health."],
        "financial_tip": ["Start saving early and regularly to build a strong financial foundation.",
                          "Consider diversifying your investments to minimize risks."],
        "self_care_advice": ["Practice mindfulness and meditation to reduce stress levels.",
                             "Make time for hobbies and activities that bring you joy and relaxation."]
    }

    def get_response(prompt):
        user_input = prompt.lower()

        if "technical" in user_input:
            return random.choice(responses["advice"])
        elif "personal" in user_input:
            return random.choice(responses["small_talk"])
        elif "joke" in user_input:
            return random.choice(responses["joke"])
        elif "bye" in user_input or "goodbye" in user_input:
            return random.choice(responses["farewell"])
        elif any(greeting in user_input for greeting in ["hello", "hi", "hey"]):
            return random.choice(responses["greeting"])
        elif "weather" in user_input:
            return random.choice(responses["common_questions"]["weather"])
        elif "time" in user_input:
            return random.choice(responses["common_questions"]["time"])
        elif "trivia" in user_input:
            return random.choice(responses["trivia"])
        elif "activity" in user_input or "suggestion" in user_input:
            return random.choice(responses["activity_suggestion"])
        elif "motivation" in user_input or "quote" in user_input:
            return random.choice(responses["motivational_quote"])
        elif "trend" in user_input or "technology" in user_input:
            return random.choice(responses["technology_trends"])
        elif "book" in user_input or "recommendation" in user_input:
            return random.choice(responses["book_recommendation"])
        elif "healthy" in user_input or "habit" in user_input:
            return random.choice(responses["healthy_habit_tip"])
        elif "financial" in user_input or "money" in user_input:
            return random.choice(responses["financial_tip"])
        elif "self-care" in user_input or "self care" in user_input:
            return random.choice(responses["self_care_advice"])
        else:
            return "I'm sorry, I didn't quite catch that. How can I assist you further?"

    def count_characters(message):
        uppercase_count = sum(1 for char in message if char.isupper())
        lowercase_count = sum(1 for char in message if char.islower())
        return uppercase_count, lowercase_count

    def plot_pie(uppercase_count, lowercase_count):
        sizes = [uppercase_count, lowercase_count]
        labels = ['Uppercase characters', 'Lowercase characters']

        plt.figure(figsize=(8, 8))
        plt.pie(sizes, labels=labels, autopct='%3.1f%%', startangle=40)
        plt.axis('equal')
        plt.title('Pie Chart for character count')

        plt.savefig('static/plot.png')

    prompt = request.form['prompt']
    answer = get_response(prompt)
    uppercase_count, lowercase_count = count_characters(prompt)
    plot_pie(uppercase_count, lowercase_count)

    return render_template('index.html', reply=answer, total_characters=uppercase_count + lowercase_count,
                           uppercases=uppercase_count, lowercases=lowercase_count, plot_url='static/plot.png')
