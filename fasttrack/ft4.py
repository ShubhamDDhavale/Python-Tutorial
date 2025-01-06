from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        return f"Thank you, {name}. Your message has been received."
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
