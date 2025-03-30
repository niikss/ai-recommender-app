# 🎬 AI Recommendation App

A full-stack AI-powered web app that gives personalized recommendations for movies, music, or books based on user input — powered by a custom ML classifier.

---

## 🧠 Features

- 🔁 Full-stack: React frontend + Flask backend
- 🧠 ML-powered text classifier (TF-IDF + Naive Bayes)
- 🎨 Tailwind CSS styling
- 🌍 Ready to deploy (Netlify + Render)

---

## 🚀 How It Works

1. User types free-form input (e.g. "Suggest me a movie")
2. Request is sent to Flask API (`/api/recommend`)
3. ML model predicts category (movie / music / book)
4. Recommendation list is returned and rendered on screen

---

## 📦 Local Setup

### 🔹 Backend (Flask + ML)

```bash
cd backend
pip install -r requirements.txt
python app.py
```
Runs at: http://localhost:3000

📸 Demo

Try:

"I want a movie" → 🎬
"Play something" → 🎵
"Suggest a book" → 📚
