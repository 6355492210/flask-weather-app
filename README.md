# Flask Weather App

A Dockerized Flask Weather Application using OpenWeather API.

## Tech Stack
- Flask
- Docker
- Gunicorn
- Python

## Run
docker build -t flask-weather-app .
docker run -p 5000:5000 flask-weather-app