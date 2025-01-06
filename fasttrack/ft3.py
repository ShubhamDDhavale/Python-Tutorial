from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    languages = ["Python", "JavaScript", "C++"]
    return render_template("index.html", languages=languages)

if __name__ == "__main__":
    app.run(debug=True)
