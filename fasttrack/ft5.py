from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task_content = request.form["content"]
        new_task = Task(content=task_content)
        db.session.add(new_task)
        db.session.commit()
        return redirect("/")
    tasks = Task.query.all()
    return render_template("index2.html", tasks=tasks)

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
