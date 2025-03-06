# AI Chatbot for University FAQs

<p align="center">
  <img src="static/assets/android-icon-192x192.png" alt="Chatbot Image" width="100px">
</p>

This AI-powered chatbot is designed to assist students by answering frequently asked questions (FAQs) related to
university admissions, academic programs, student services, and more. Built with Flask and NLTK, it provides instant
responses based on a structured knowledge base.

## Features

- Handles FAQs about admissions, courses, scholarships, student services, and more.
- Supports greetings with a welcome message.
- Uses Natural Language Processing (NLP) for better understanding.
- Styled frontend using Tailwind CSS.

## Technologies Used

- **Backend:** Flask (Python)
- **NLP:** NLTK
- **Frontend:** HTML, JavaScript, Tailwind CSS

## Installation & Setup

### 1. Clone the Repository

```sh
  git clone https://github.com/your-repo/ai-university-chatbot.git
  cd ai-university-chatbot
```

### 2. Create a Virtual Environment (Optional but Recommended)

```sh
  python -m venv venv
```

#### Activate it:

- **Windows:** `venv\Scripts\activate`
- **Mac/Linux:** `source venv/bin/activate`

### 3. Install Dependencies

```sh
  pip install -r requirements.txt
```

### 4. Run the Application

```sh
  python app.py
```

Visit `http://127.0.0.1:5000/` in your browser.

## How to Use

1. Type a greeting (e.g., "hi", "hello") to receive a welcome message.
2. Ask a question about admissions, courses, or student services.
3. Get instant responses from the chatbot.

## Knowledge Base

The chatbot loads its responses from `knowledge_base.json`. To update responses, edit this file and restart the app.

## Contributing

Feel free to contribute by improving the chatbot logic, enhancing the knowledge base, or refining the UI.

## License

MIT License

---
Developed by Robby Malunga Jr. 🚀