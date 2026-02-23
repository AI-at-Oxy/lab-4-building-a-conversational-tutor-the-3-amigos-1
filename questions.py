# questions.py
# Replace this with your own topic and questions (at least 5)!

TOPIC = "Data Structures in Python"

QUESTIONS = [
    {
        "question": "How do Stacks work in Python?",
        "answer": "A stack is a collection of items that follows the Last In, First Out (LIFO) principle. You can use a list and the append() and pop() methods to implement a stack.",
        "misconception": "Students often think that stacks are the same as queues, but they operate in opposite ways."
    },
    {
        "question": "How do Queues work in Python?",
        "answer": "A queue is a collection of items that follows the First In, First Out (FIFO) principle. You can use the collections.deque class to implement a queue efficiently.",
        "misconception": "Students often confuse queues with stacks and get the order of operations wrong."
    },
]

# Build the system prompt with your questions baked in
SYSTEM_PROMPT = f"""You are a friendly tutor helping a student learn about {TOPIC}.

Here are the questions you should work through with the student:

"""

for i, q in enumerate(QUESTIONS, 1):
    SYSTEM_PROMPT += f"""Question {i}: {q['question']}
  Correct answer: {q['answer']}
  Common misconception: {q['misconception']}

"""

SYSTEM_PROMPT += """
Work through the questions with the student. DO NOT reveal the answers. Make sure to include the exact question text in your response. Instead, guide the student to discover the answers themselves. If the student gives an incorrect answer, gently correct them and explain the misconception. If they are on the right track, encourage them to keep going. Do one question at a time and wait for the student's response to be correct before moving on to the next question.
"""
