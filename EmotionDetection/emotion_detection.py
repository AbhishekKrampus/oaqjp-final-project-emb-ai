"""Module for emotion detection using Watson NLP service."""
import requests


def emotion_detector(text_to_analyze):
    """
    Detect emotions in the given text using Watson NLP service.

    Args:
        text_to_analyze (str): The text to analyze for emotions.

    Returns:
        dict: A dictionary containing emotion scores and the dominant emotion.
              Returns None values if the input is invalid or an error occurs.
    """
    if not text_to_analyze or not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = (
        'https://sn-watson-emotion.labs.skills.network/v1/'
        'watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    headers = {
        'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock',
        'Content-Type': 'application/json'
    }
    payload = {
        'raw_document': {
            'text': text_to_analyze
        }
    }

    response = requests.post(url, json=payload, headers=headers, timeout=30)

    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    response_data = response.json()

    # Extract emotion predictions from the response
    emotions_data = (
        response_data
        .get('emotionPredictions', [{}])[0]
        .get('emotion', {})
    )

    anger = emotions_data.get('anger', 0)
    disgust = emotions_data.get('disgust', 0)
    fear = emotions_data.get('fear', 0)
    joy = emotions_data.get('joy', 0)
    sadness = emotions_data.get('sadness', 0)

    emotion_scores = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness
    }

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }
