import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def weather():
    weather_data = None
    if request.method == "POST":
        city = request.form["city"]
        api_key = "your_api_key_here"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
    return render_template("weather.html", weather_data=weather_data)

if __name__ == "__main__":
    app.run(debug=True)
