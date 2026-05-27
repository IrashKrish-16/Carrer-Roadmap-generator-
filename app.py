from gemini_helper import generate_roadmap
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():

    return render_template("home.html")


@app.route("/generate", methods=["POST"])
def generate():

    role = request.form["role"]

    ai_data = generate_roadmap(role)

    lines = ai_data.split("\n")

    roadmap = []

    for line in lines:

        if "|" in line:

            parts = line.split("|")

            # only accept proper AI rows
            if len(parts) >= 4:

                skill = parts[0].strip()

                time = parts[1].strip()

                project = parts[2].strip()

                resource = parts[3].strip()

                roadmap.append(
                    (
                        skill,
                        time,
                        project,
                        resource
                    )
                )

    return render_template(
        "result.html",
        role=role,
        roadmap=roadmap
    )


if __name__ == "__main__":

    app.run(debug=True)