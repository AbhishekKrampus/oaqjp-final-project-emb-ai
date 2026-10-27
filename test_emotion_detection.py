"""Unit tests for EmotionDetection package."""
import unittest
from unittest.mock import patch, MagicMock
from EmotionDetection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test cases for the emotion_detector function."""

    def _make_mock_response(self, emotions, status_code=200):
        """Helper to build a mock response object."""
        mock_response = MagicMock()
        mock_response.status_code = status_code
        mock_response.json.return_value = {
            'emotionPredictions': [
                {
                    'emotion': emotions
                }
            ]
        }
        return mock_response

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_emotion_joy(self, mock_post):
        """Test that joy is detected as dominant emotion for positive text."""
        mock_post.return_value = self._make_mock_response({
            'anger': 0.006,
            'disgust': 0.002,
            'fear': 0.005,
            'joy': 0.900,
            'sadness': 0.010
        })
        result = emotion_detector('I am glad this happened')
        self.assertEqual(result['dominant_emotion'], 'joy')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_emotion_anger(self, mock_post):
        """Test that anger is detected as dominant emotion for angry text."""
        mock_post.return_value = self._make_mock_response({
            'anger': 0.850,
            'disgust': 0.100,
            'fear': 0.010,
            'joy': 0.002,
            'sadness': 0.020
        })
        result = emotion_detector('I am really mad about this')
        self.assertEqual(result['dominant_emotion'], 'anger')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_emotion_disgust(self, mock_post):
        """Test that disgust is detected as dominant emotion for disgusting text."""
        mock_post.return_value = self._make_mock_response({
            'anger': 0.050,
            'disgust': 0.800,
            'fear': 0.010,
            'joy': 0.005,
            'sadness': 0.020
        })
        result = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result['dominant_emotion'], 'disgust')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_emotion_sadness(self, mock_post):
        """Test that sadness is detected as dominant emotion for sad text."""
        mock_post.return_value = self._make_mock_response({
            'anger': 0.010,
            'disgust': 0.005,
            'fear': 0.020,
            'joy': 0.002,
            'sadness': 0.900
        })
        result = emotion_detector('I am so sad about this')
        self.assertEqual(result['dominant_emotion'], 'sadness')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_emotion_fear(self, mock_post):
        """Test that fear is detected as dominant emotion for fearful text."""
        mock_post.return_value = self._make_mock_response({
            'anger': 0.020,
            'disgust': 0.010,
            'fear': 0.870,
            'joy': 0.002,
            'sadness': 0.050
        })
        result = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result['dominant_emotion'], 'fear')

    def test_blank_input_returns_none(self):
        """Test that blank input returns None values."""
        result = emotion_detector('')
        self.assertIsNone(result['dominant_emotion'])
        self.assertIsNone(result['anger'])
        self.assertIsNone(result['joy'])

    def test_whitespace_input_returns_none(self):
        """Test that whitespace-only input returns None values."""
        result = emotion_detector('   ')
        self.assertIsNone(result['dominant_emotion'])

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_http_400_returns_none(self, mock_post):
        """Test that HTTP 400 response returns None values."""
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.json.return_value = {}
        mock_post.return_value = mock_response
        result = emotion_detector('invalid input causing 400')
        self.assertIsNone(result['dominant_emotion'])
        self.assertIsNone(result['anger'])

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_output_contains_all_five_emotions(self, mock_post):
        """Test that the output dictionary contains all five emotion keys."""
        mock_post.return_value = self._make_mock_response({
            'anger': 0.1,
            'disgust': 0.1,
            'fear': 0.1,
            'joy': 0.6,
            'sadness': 0.1
        })
        result = emotion_detector('I love this')
        self.assertIn('anger', result)
        self.assertIn('disgust', result)
        self.assertIn('fear', result)
        self.assertIn('joy', result)
        self.assertIn('sadness', result)
        self.assertIn('dominant_emotion', result)


if __name__ == '__main__':
    unittest.main()
