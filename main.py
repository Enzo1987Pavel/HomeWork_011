from flask import Flask, render_template

from funcs import load_candidates_from_json

app = Flask(__name__)


@app.route("/")
def main_page():

    candidates_list = load_candidates_from_json("candidates.json")
    return render_template("list.html", candidates=candidates_list)


@app.route("/candidates/<int:id>")
def candidates_page():

    candidates_list = load_candidates_from_json("candidates.json")
    return render_template("card.html", candidates=candidates_list)


app.run()
