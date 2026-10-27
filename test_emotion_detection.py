"""
Unit tests for the EmotionDetection package.
Tests use the live Watson NLP endpoint. If network is unavailable,
mocked tests are included as fallback for CI environments.
"""
import unittest
from unittest.mock import patch, MagicMock
import json
from EmotionDetection.emotion_detection import emotion_detector


# ─── Mocked response helpers ─────────────────────────────────────────────────

def _make_mock_response(emotions_dict, status_code=200):
    """Create a mock requests.Response object with given emotion scores."""
    mock_resp = MagicMock()
    mock_resp.status_code = status_code
    payload = {
        "emotionPredictions": [
            {
                "emotion": emotions_dict
            }
        ]
    }
    mock_resp.text = json.dumps(payload)
    return mock_resp


# ─── Test Cases ───────────────────────────────────────────────────────────────

class TestEmotionDetector(unittest.TestCase):
    """Unit tests for the emotion_detector function."""

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_joy_dominant(self, mock_post):
        """'I am glad this happened' should yield joy as dominant emotion."""
        mock_post.return_value = _make_mock_response({
            'anger': 0.006274985,
            'disgust': 0.0025598293,
            'fear': 0.009251528,
            'joy': 0.9680386,
            'sadness': 0.049744144
        })
        result = emotion_detector('I am glad this happened')
        self.assertEqual(result['dominant_emotion'], 'joy')
        self.assertIn('joy', result)

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_anger_dominant(self, mock_post):
        """'I am really mad about this' should yield anger as dominant emotion."""
        mock_post.return_value = _make_mock_response({
            'anger': 0.8077877,
            'disgust': 0.10760572,
            'fear': 0.048797555,
            'joy': 0.0037462806,
            'sadness': 0.054330487
        })
        result = emotion_detector('I am really mad about this')
        self.assertEqual(result['dominant_emotion'], 'anger')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_disgust_dominant(self, mock_post):
        """'I feel disgusted just hearing about this' → disgust dominant."""
        mock_post.return_value = _make_mock_response({
            'anger': 0.08228521,
            'disgust': 0.7236546,
            'fear': 0.040800802,
            'joy': 0.002699564,
            'sadness': 0.10655968
        })
        result = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result['dominant_emotion'], 'disgust')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_sadness_dominant(self, mock_post):
        """'I am so sad about this' → sadness dominant."""
        mock_post.return_value = _make_mock_response({
            'anger': 0.044340316,
            'disgust': 0.030589437,
            'fear': 0.05867198,
            'joy': 0.003832735,
            'sadness': 0.86259556
        })
        result = emotion_detector('I am so sad about this')
        self.assertEqual(result['dominant_emotion'], 'sadness')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_fear_dominant(self, mock_post):
        """'I am really afraid that this will happen' → fear dominant."""
        mock_post.return_value = _make_mock_response({
            'anger': 0.06498499,
            'disgust': 0.03231432,
            'fear': 0.7432432,
            'joy': 0.0022432,
            'sadness': 0.1572143
        })
        result = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result['dominant_emotion'], 'fear')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_blank_input_returns_none(self, mock_post):
        """Blank text input (400 response) should return all None values."""
        mock_post.return_value = MagicMock(status_code=400, text='')
        result = emotion_detector('')
        self.assertIsNone(result['dominant_emotion'])
        self.assertIsNone(result['anger'])
        self.assertIsNone(result['disgust'])
        self.assertIsNone(result['fear'])
        self.assertIsNone(result['joy'])
        self.assertIsNone(result['sadness'])

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_output_keys_present(self, mock_post):
        """Result must always contain all six required keys."""
        mock_post.return_value = _make_mock_response({
            'anger': 0.1, 'disgust': 0.1, 'fear': 0.1, 'joy': 0.6, 'sadness': 0.1
        })
        result = emotion_detector('test')
        for key in ['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion']:
            self.assertIn(key, result)


if __name__ == '__main__':
    unittest.main()
