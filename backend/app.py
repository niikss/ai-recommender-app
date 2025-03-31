from flask import Flask, request, jsonify
from flask_cors import CORS
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Dummy training data
X_train = [
    # Movies
    "Suggest a movie", "I want to watch something", "Recommend a film",
    "Best movies to watch", "Give me movie suggestions", "Movie recommendations",

    # Music
    "Play some music", "Suggest songs", "Give me a playlist",
    "Recommend me a song", "I want to listen to music", "Good songs to play",

    # Books
    "Book to read", "Recommend a novel", "Suggest me a book",
    "Reading recommendation", "Any good books?", "Give me something to read"
]
y_train = [
    "movie", "movie", "movie", "movie", "movie", "movie",
    "music", "music", "music", "music", "music", "music",
    "book", "book", "book", "book", "book", "book"
]


# Train a Naive Bayes model
vectorizer = TfidfVectorizer()
X_train_vectors = vectorizer.fit_transform(X_train)
model = MultinomialNB()
model.fit(X_train_vectors, y_train)

def get_recommendations(user_input):
    user_vec = vectorizer.transform([user_input])
    predicted_label = model.predict(user_vec)[0]

    if predicted_label == "movie":
        return ["Inception", "Interstellar", "Tenet"]
    elif predicted_label == "music":
        return ["Blinding Lights", "Shape of You", "Levitating"]
    else:
        return ["Atomic Habits", "Sapiens", "1984"]

@app.route('/api/recommend', methods=['POST'])
def recommend():
    data = request.json
    user_input = data.get('input', '')
    recommendations = get_recommendations(user_input)
    return jsonify({"recommendations": recommendations})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

