# questions.py
# Replace this with your own topic and questions (at least 5)!

TOPIC = "Data Structures in Python"

QUESTIONS = [
    {
        "question": "What is an array in Python?",
        "answer": "An array is a data structure that stores a collection of elements, typically of the same type, in contiguous memory locations.",
        "misconception": "Students sometimes say arrays are like lists because they both store multiple values."
    },
    {
        "question": "What is a linked list in Python?",
        "answer": "A linked list is a data structure where elements are stored in nodes, and each node points to the next node in the sequence.",
        "misconception": "Students sometimes confuse linked lists with arrays because both are used to store collections of data."
    },
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
    {
        "question": "Consider a binary tree (not necessarily a BST). When performing a preorder traversal, you get the following result: A, B, D, E, C . Which node is guaranteed to be the root of the tree?",
        "answer": "A",
        "misconception": "Students sometimes think the root depends on whether the tree is balanced or complete."
    },
    {
        "question": "A dictionary (hash map) is used to store student IDs as keys and GPAs as values. If two students have different IDs but end up in the same bucket, does the dictionary lose one of the values?",
        "answer": "No, the dictionary handles collisions internally, so both values are preserved.",
        "misconception": "Students sometimes think one value will be lost if there's a collision."
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
Work through the questions with the student. DO NOT reveal the answers. Make sure to include the exact question text in your response. The answer doesn't have to match the exact answer text, the student answer does however have to include the key parts of the answer text. Guide the student to discover the answers themselves. If the student gives an incorrect answer, gently correct them and explain the misconception. If they are on the right track, encourage them to keep going. Do one question at a time and wait for the student's response to be correct before moving on to the next question.
"""
