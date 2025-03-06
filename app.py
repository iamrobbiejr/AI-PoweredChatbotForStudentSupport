import json
import re
import string

import nltk
from flask import Flask, render_template, request, jsonify
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

app = Flask(__name__)

# Ensure necessary NLTK resources are downloaded
"""
NLTK (Natural Language Toolkit) resources are essential datasets and models used for natural language processing tasks.
These resources need to be downloaded separately from the NLTK library installation.

1. "punkt": A pre-trained model for tokenization, which splits text into sentences and words.
   It's crucial for the word_tokenize() function used in our preprocess() function.

2. "punkt_tab": An additional resource for the punkt tokenizer, providing improved tokenization capabilities.

3. "stopwords": A corpus of common words (like "the", "is", "at") that are often removed in text processing
   to focus on more meaningful words. This is used in our preprocess() function to filter out stop words.

Downloading these resources ensures that our text preprocessing and tokenization functions work correctly,
which is fundamental for the chatbot's ability to understand and process user input.
"""
nltk.download("punkt")
nltk.download('punkt_tab')
nltk.download("stopwords")


# Load knowledge base from JSON file
def load_knowledge_base():
    try:
        with open("static/university_knowledge_base.json", "r") as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading knowledge base: {e}")
        return {}


knowledge_base = load_knowledge_base()

# Define greeting responses
greeting_responses = "Hello! Welcome to our university chatbot. How can I assist you today? You can ask about admissions, courses, student services, and more..."
greetings = {"hi", "hie", "hello", "hey", "wassup", "good morning", "good afternoon", "good evening"}


def preprocess(text):
    """
    Preprocess the input text for natural language processing tasks.
    
    This function performs the following steps:
    1. Converts the text to lowercase
    2. Removes all punctuation
    3. Tokenizes the text into individual words
    4. Removes common English stop words
    
    Args:
    text (str): The input text to be preprocessed.
    
    Returns:
    list: A list of preprocessed tokens (words).
    
    Raises:
    Exception: If any error occurs during preprocessing.
    """
    try:
        # Convert text to lowercase
        text = text.lower()

        # Remove all punctuation using regex
        text = re.sub(f"[{string.punctuation}]", "", text)

        # Tokenize the text into individual words
        tokens = word_tokenize(text)

        # Get English stop words
        stop_words = set(stopwords.words("english"))

        # Remove stop words from tokens
        tokens = [word for word in tokens if word not in stop_words]

        return tokens
    except Exception as e:
        print(f"Error in preprocessing: {e}")
        return []


# Get response from knowledge base
def get_response(user_input):
    """
    Generate a response to the user's input based on the knowledge base.

    This function performs the following steps:
    1. Preprocesses the user input
    2. Checks if the input is valid
    3. Checks if the input is a greeting
    4. Searches the knowledge base for a matching response
    5. Returns a default response if no match is found

    Args:
    user_input (str): The raw input string from the user.

    Returns:
    str: A response string to be sent back to the user.

    Raises:
    Exception: If any error occurs during response generation.
    """
    try:
        # Preprocess the user input
        tokens = preprocess(user_input)

        # Check if the preprocessing resulted in any valid tokens
        if not tokens:
            return "Sorry, I couldn't process your input. Please try rephrasing your question."

        # Check if the input is a greeting
        if any(word in greetings for word in tokens):
            return greeting_responses

        # Search the knowledge base for a matching response
        for key in knowledge_base:
            # Check if any word in the knowledge base key matches any token
            if any(word in key.split() for word in tokens):
                return knowledge_base[key]

        # If no match found, return a default response
        return "Sorry, I do not understand your question. You can ask about admissions, courses, student services, and more..."

    except Exception as e:
        # Log the error and return a generic error message
        print(f"Error in getting response: {e}")
        return "An error occurred. Please try again later."


@app.route("/")
def index():
    return render_template("chat.html")


@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_message = request.json.get("message")
        if not user_message:
            return jsonify({"response": "Please enter a valid question."})
        response = get_response(user_message)
        return jsonify({"response": response})
    except Exception as e:
        print(f"Error in chat function: {e}")
        return jsonify({"response": "An unexpected error occurred. Please try again later."})


if __name__ == "__main__":
    app.run(debug=True)
