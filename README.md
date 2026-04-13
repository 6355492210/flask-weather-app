# 🌦️ Flask Weather Web Application

A **Dockerized** Flask-based weather forecasting web app that fetches **real-time weather data** using the OpenWeather API and runs with **Gunicorn** for production-ready deployment.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Flask](https://img.shields.io/badge/Flask-2.x-green)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📌 Project Overview

This project demonstrates backend web development skills including REST API integration, Docker containerization, and production deployment with Gunicorn. Users can search for any city worldwide and instantly get live weather conditions.

---

## ✨ Features

- 🌍 **Real-Time Weather Data** — Live temperature, humidity, wind speed, and conditions
- 🔎 **City-Based Search** — Search by city, state (optional), and country
- ⚠️ **Error Handling** — Invalid city names, API failures handled gracefully
- 🔐 **Secure Configuration** — API keys stored in `.env` using `python-dotenv`
- 🐳 **Docker Support** — Fully containerized for easy deployment
- 🚀 **Production Ready** — Runs with Gunicorn WSGI server

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python 3.13, Flask |
| **API** | OpenWeather API |
| **Frontend** | HTML5, CSS3, Bootstrap, JavaScript |
| **Templating** | Jinja2 |
| **Deployment** | Docker, Gunicorn |
| **Security** | python-dotenv (.env) |
| **Tools** | Git, GitHub, VS Code, venv |

---

## ⚙️ How It Works

```
User enters city → Flask receives POST request
→ Backend calls OpenWeather API
→ JSON response parsed
→ Weather data passed to Jinja2 template
→ Results displayed dynamically
```

---

## 🚀 Installation & Setup

### Option 1 — Run with Docker (Recommended)

```bash
# Clone the repository
git clone https://github.com/6355492210/flask-weather-app.git
cd flask-weather-app

# Create .env file
echo "API_KEY=your_openweather_api_key" > .env

# Build and run Docker container
docker build -t flask-weather-app .
docker run -p 5000:5000 flask-weather-app
```

Visit: `http://localhost:5000`

---

### Option 2 — Run Locally

```bash
# Clone the repository
git clone https://github.com/6355492210/flask-weather-app.git
cd flask-weather-app

# Create virtual environment
python -m venv venv
source venv/bin/activate       # Linux/Mac
venv\Scripts\activate          # Windows

# Install dependencies
pip install -r requirements.txt

# Create .env file and add your API key
echo "API_KEY=your_openweather_api_key" > .env

# Run the app
python app.py
```

---

## 🔑 Get API Key

1. Go to [openweathermap.org](https://openweathermap.org/api)
2. Sign up for a free account
3. Copy your API key
4. Add it to `.env` file

---

## 📁 Project Structure

```
flask-weather-app/
│
├── templates/
│   └── index.html          # Main HTML Template
│
├── app.py                  # Flask App & Routes
├── weather.py              # API Integration Logic
├── requirements.txt        # Python Dependencies
├── Dockerfile              # Docker Configuration
├── .dockerignore
├── .gitignore
└── README.md
```

---

## 🧠 What This Project Demonstrates

- Flask routing & HTTP request handling (GET/POST)
- External REST API integration (OpenWeather)
- JSON response parsing & data extraction
- Jinja2 template rendering with dynamic data
- Environment variable security with `.env`
- Docker containerization & Gunicorn deployment
- Clean, modular project structure



---

## 👨‍💻 Author

**Vivek Vaghela | Python Backend Developer **
- GitHub: [@6355492210](https://github.com/6355492210)
- LinkedIn: [linkedin.com/in/vaghelavivekm](https://www.linkedin.com/in/vaghelavivekm)
- Location: Rajkot, Gujarat

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
