import React, { useState } from 'react';

function App() {
  const [input, setInput] = useState('');
  const [recommendations, setRecommendations] = useState([]);

  const handleSubmit = async () => {
    const response = await fetch('https://ai-recommender-app.onrender.com/api/recommend', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({ input }),
});


      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ input }),
    });

    const data = await response.json();
    setRecommendations(data.recommendations);
  };

  return (
    <div className="min-h-screen bg-gray-50 flex items-center justify-center p-6">
      <div className="max-w-xl w-full bg-white shadow-md rounded-xl p-8">
        <h2 className="text-3xl font-bold text-purple-700 mb-6 text-center">
          🎬 AI Recommendation Demo
        </h2>

        <div className="flex gap-2 mb-6">
          <input
            className="flex-1 p-3 border border-gray-300 rounded-lg shadow-sm"
            type="text"
            value={input}
            placeholder="Enter your preference (e.g., music or movie)"
            onChange={(e) => setInput(e.target.value)}
          />
          <button
            className="bg-purple-600 text-white px-5 py-3 rounded-lg hover:bg-purple-700 transition"
            onClick={handleSubmit}
          >
            Get Recommendations
          </button>
        </div>

        <ul className="list-disc pl-5 space-y-1 text-lg text-gray-700">
          {recommendations.map((item, idx) => (
            <li key={idx}>{item}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default App;

