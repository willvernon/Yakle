from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load questions from a JSON file
with open("questions.json", "r") as f:
    questions = json.load(f)


@app.route("/")
def index():
    return render_template("index.html", question_count=len(questions))


@app.route("/question/<int:qid>")
def get_question(qid):
    if 0 <= qid < len(questions):
        return render_template("question.html", question=questions[qid], qid=qid)
    return "Quiz Complete!", 200


@app.route("/submit", methods=["POST"])
def submit_answer():
    qid = int(request.form["qid"])
    user_answer = request.form["answer"].strip().lower()
    correct_answer = questions[qid]["answer"].lower()
    is_correct = user_answer == correct_answer
    return render_template(
        "result.html", is_correct=is_correct, correct_awser=correct_answer, qid=qid
    )


if __name__ == "__main__":
    app.run(debug=True)
