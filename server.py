"""Flask web application for the Emotion Detector."""
from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')


@app.route('/emotionDetector')
def emotion_detector_route():
    """Handle emotion detection requests."""
    text_to_analyze = request.args.get('textToAnalyze', '').strip()

    if not text_to_analyze:
        return 'Invalid text! Please try again!'

    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'

    anger = result['anger']
    disgust = result['disgust']
    fear = result['fear']
    joy = result['joy']
    sadness = result['sadness']
    dominant = result['dominant_emotion']

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant}."
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
