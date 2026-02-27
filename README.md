[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/LkIvP-P-)
# Lab 4: Conversational Tutor with LiteLLM and Ollama

## Overview

In this lab you'll build a web-based chat interface where a student converses with an AI tutor. The tutor is grounded in **hardcoded educational questions** that you embed in the system prompt.

## Setup

### 1. Install Ollama

```bash
# macOS / Linux
curl -fsSL https://ollama.com/install.sh | sh

# Or download from https://ollama.com/download
```

### 2. Pull a model

```bash
ollama pull llama3.2
```

### 3. Set up your Python environment

```bash
conda activate flask-env
pip install -r requirements.txt
```

### 4. Test from the command line first

```bash
python chat_cli.py
```

### 5. Run the web app

```bash
python app.py
```

Then open http://127.0.0.1:5000/ in your browser.

## Your Tasks

1. **Replace the example questions** in `questions.py` with at least 5 questions on a topic you know well. Include correct answers and common misconceptions.
2. **Design a system prompt** that tells the LLM how to tutor. This is the creative heart of the lab — what kind of tutor do you want to build?
3. **Build out the chat interface** — the starter gives you a bare minimum. Make it your own.
4. **Test and iterate** on your system prompt. Try correct answers, wrong answers, "I don't know," and off-topic messages.

## Project Structure

```
lab4-starter/
    app.py              # Flask app with / and /chat routes
    questions.py        # Your educational questions (replace the examples!)
    chat_cli.py         # Command-line LLM chat (for testing)
    templates/
        chat.html       # Chat web interface
    requirements.txt
```

## Reflection Questions

Answer each question below by writing in the space provided. This is a markdown file — you can edit it directly in your code editor or on GitHub.

### 1. How did designing a *system prompt* compare to designing *frames* in Lab 3? Which gives you more control over the learning experience? Which is more work?

```
Designing a system prompt proved to be more difficult that designing frames in Lab 3 since we had to trouble shoot the system prompt to work as intended. However, the system prompt still gave us more control over the learning experience since we could tell it how to help students when they get stuck on a topic. This allowed for a learning experience that could better help students, since the system prompt wouldn't be as hard-coded as the frames. The system prompt was more work as a lot of trial and error was needed to get desirable results, whereas the frames allowed us to output exactly what we wanted the user to see.
```

### 2. Your tutor has hardcoded questions but generates responses dynamically. When is this an advantage over canned feedback? When is it a risk?

```
Generating responses dynamically can be useful when the user gets stuck. For example, the tutor could rephrase questions if the student does not understand, and can even tell them whether they are on the right track. The tutor is also able to fit their responses to match that of the user, allowing for more depth than canned feedback which may not address misunderstandings the student has. However, dynamic responses become a risk when it overwhelms student with information that may or may not be relevant. This would cause confusion for the student, and hinder their learning experience.
```

### 3. What tutoring strategy did you choose, and why? If you could redesign it, what would you change based on testing?

```
We chose a mastery based tutoring strategy in which the tutor would make sure that the student had the main concepts of each question understood. We chose this strategy so that the tutor would remain on the same question so that the student could fully understand the topic of the current question. This mastery based tutoring would also used since it would give students feedback that they could work with to understand the main points. If we could redesign it, we would have the tutor ask about the fundamentals rather than making sure that the student is proficient. Doing so would allow for more responses to be accepted instead of responses that have to be similar to the answers we provided. We would also change the answers to make them less specific, including the fundamentals.
```

### 4. Skinner insisted on a low error rate and immediate, predictable reinforcement. Your LLM tutor is neither predictable nor error-free. Is that a problem? For whom?

```
Being nonpredictable is a problem for students because the responses it could give may be too wordy or not give enough information, causing the student to not understand where they went wrong if the answer was incorrect. Additionally, since student responses will vary, one could not predict how the tutor will respond, causing their response quality to vary per student. Not being error-free is a problem for the developer since any errors that come up will have to be addressed in the system prompt, which could lead to novel errors. 
```

### 5. A school wants to use your tutor with real students. Name three things you'd worry about.

```
Three things we would worry about are students breaking the tutor and getting unintended responses that could harm student learning, responses being overwhelming, thus causing confusion in students, and that the current system prompt is not conducive for learning in every student. This may be because some students learn better when presented with graphs and picture rather than blocks of text.
```

## Submission Checklist

- [ ] At least 5 educational questions with answers and misconceptions
- [ ] System prompt that defines the tutor's behavior
- [ ] Flask app with /chat route managing conversation history
- [ ] LiteLLM calls to a local Ollama model
- [ ] Working chat interface in the browser
- [ ] Tested with correct, incorrect, and edge-case inputs
- [ ] System prompt iterated at least once based on testing
- [ ] Reflection questions answered (above)
- [ ] Committed with meaningful commit messages
