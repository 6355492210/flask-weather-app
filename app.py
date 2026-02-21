from flask import Flask, render_template, request, flash
from weather import get_weather   # updated function name
import os

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    data = None

    if request.method == 'POST':
        city = request.form.get('cityName')
        state = request.form.get('stateName')
        country = request.form.get('countryName')

        print("Form Data:", city, state, country)

        data = get_weather(city, state, country)

        print("Weather Data:", data)

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)   # production ma False karvu