from flask import Flask, render_template

from funcs import load_candidates_from_json

app = Flask(__name__)


@app.route("/")
def main_page():

    candidate = load_candidates_from_json("candidates.json")

    return render_template("list.html", candidate=candidate)


@app.route("/candidates/<int:id>")
def candidates_page():

    candidate = load_candidates_from_json("candidates.json")
    return render_template("card.html", candidate=candidate)


app.run()
