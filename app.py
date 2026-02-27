# app.py
from flask import Flask, render_template, request, session, jsonify
from litellm import completion
from questions import TOPIC, QUESTIONS, SYSTEM_PROMPT
import uuid

app = Flask(__name__)
app.secret_key = "change-this-to-something-secret"

# Ollama configuration
MODEL = "ollama/ministral-3:3b"
API_BASE = "http://localhost:11434"


def get_llm_response(conversation_history):
    """Send conversation history to the LLM and get a response."""
    try:
        response = completion(
            model=MODEL,
            messages=conversation_history,
            api_base=API_BASE,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error connecting to Ollama: {str(e)}. Is Ollama running?"


def init_session():
    """Ensure session state exists."""
    session.setdefault("history", [
        {"role": "system", "content": SYSTEM_PROMPT}
    ])
    session.setdefault("reactions", [])


@app.route("/")
def index():
    # Start fresh on page load
    session.clear()
    init_session()
    return render_template(
        "chat.html",
        topic=TOPIC,
        num_questions=len(QUESTIONS)
    )


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").strip()
    if not user_message:
        return jsonify({"error": "Empty message"}), 400

    # Initialize progress if missing
    if "progress" not in session:
        session["progress"] = {"attempted": 0, "correct": 0}

    # Initialize message counter if missing
    if "message_count" not in session:
        session["message_count"] = 0

    session["history"].append({"role": "user", "content": user_message})

    # Increment message count
    session["message_count"] += 1

    # Only start counting attempts after the first message
    if session["message_count"] > 1:
        session["progress"]["attempted"] += 1

    reply = get_llm_response(session["history"])

    # Generate a unique message ID for this assistant response
    message_id = str(uuid.uuid4())

    session["history"].append({"role": "assistant", "content": reply})
    session.modified = True

    return jsonify({
        "reply": reply,
        "message_id": message_id,
        "progress": session["progress"]
    })

@app.route("/react", methods=["POST"])
def react():
    data = request.get_json()

    message_id = data.get("message_id")
    reaction = data.get("reaction")

    if not message_id or not reaction:
        return jsonify({"error": "Invalid reaction"}), 400

    print(f"[REACTION] message={message_id} reaction={reaction}")

    # Store the reaction in session
    if "reactions" not in session:
        session["reactions"] = []
    
    session["reactions"].append({
        "message_id": message_id,
        "reaction": reaction
    })
    session.modified = True

    # Optional clarification for confused
    if reaction == "confused":
        clarification = (
            "Good question! Let's slow down and look at this step by step.\n\n"
            "Can you tell me which part specifically is confusing?"
        )
        return jsonify({
            "status": "ok",
            "clarification": clarification,
            "message_id": f"clarify-{message_id}"
        })

    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True)