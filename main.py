from flask import Flask, render_template

from funcs import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)

candidate_list = load_candidates_from_json("candidates.json")


@app.route("/")
def main_page():
    return render_template("list.html", candidate=candidate_list)


@app.route("/candidates/<int:id>")
def candidates_page(id):

    cand_id = get_candidate(id)

    return render_template("card.html", candidate=cand_id)


@app.route("/search/<name>")
def candidates_names(name):
    candidates = get_candidates_by_name(name)

    return render_template("search.html", candidate=candidates, cand_len=len(candidates))


@app.route("/skills/<skill_name>")
def candidates_skill(skill_name):
    candidates = get_candidates_by_skill(skill_name)

    return render_template("skill.html", candidate=candidates, skill=skill_name, cand_len=len(candidates))


if __name__ == "__main__":
    app.run()
