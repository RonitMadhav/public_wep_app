from flask import Flask, request, jsonify
from flask_cors import CORS
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)
CORS(app)
analyzer = SentimentIntensityAnalyzer()

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.get_json()
    text = data['text']
    sentiment_scores = analyzer.polarity_scores(text)
    compound_score = sentiment_scores['compound']
    sentiment = 'positive' if compound_score >= 0.05 else 'negative' if compound_score <= -0.05 else 'neutral'
    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(port=5500, debug=True)
