## 🌦️ Flask Weather Web Application
## 📌 Project Overview
Flask Weather App is a web-based weather forecasting application built using Flask (Python backend) that fetches real-time weather data from an external API and displays it in a user-friendly interface.

The application demonstrates:
1. REST API integration
2. Backend request handling
3. Form data processing
4. Dynamic template rendering
5. Error handling
6. Environment variable security

This project showcases backend development skills and API integration knowledge.

## 🚀 Key Features
## 🌍 Real-Time Weather Data
1. Fetches live weather using external Weather API
2. Displays:
    1. Temperature
    2. Humidity
    3. Weather condition
    4. Wind speed
    5. Location details

## 🔎 City-Based Search
1. User can enter:
    1. City
    2. State (optional)
    3. Country
2. Dynamic result rendering using Flask templates

## ⚠️ Error Handling
1. Handles invalid city names
2. Displays user-friendly error messages
3. API failure handling

## 🔐 Secure Configuration
1. API keys stored in .env
2. Uses python-dotenv
3. No hardcoded secrets

## 🛠️ Tech Stack
## 🔹 Backend
1. Python 3.13
2. Flask
3. Requests
3. Dotenv

## 🔹 Frontend
1. HTML
2. CSS
3. Bootstrap
4. JS

## 🔹 Tools
1. VS Code
2. Git & GitHub
3. Virtual Environment (venv)
4. Docker

## ⚙️ How It Works
1️. User enters city in form
2️. Flask receives POST request
3️. Backend calls weather API using requests
4️. JSON response parsed
5️. Data passed to template
6️. Weather displayed dynamically

## 🌐 API Integration
1. Used external Weather API
2. Handled JSON parsing
3. Managed HTTP status codes
4. Implemented API error handling

## 🧠 What This Project Demonstrates (HR Perspective)
1. Flask routing & request handling
2. API integration experience
3. JSON parsing & data handling
4. Template rendering (Jinja2)
5. Environment variable security
6. Clean project structure
7. Git usage

## Run
docker build -t flask-weather-app .
docker run -p 5000:5000 flask-weather-app