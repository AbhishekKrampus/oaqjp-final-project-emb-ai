# Emotion Detector — IBM AI Applications with Python and Flask Final Project

## Overview
An AI-based web application that detects emotions in user-provided text using the Watson NLP Embeddable AI EmotionPredict service. Built with Python and Flask as part of the IBM Skills Network "Developing AI Applications with Python and Flask" course.

## Features
- Detects five core emotions: **anger**, **disgust**, **fear**, **joy**, and **sadness**
- Identifies the **dominant emotion** in any given text
- Clean web interface for real-time emotion analysis
- Robust error handling for blank/invalid input and service errors

## Project Structure
```
emotion-detector/
├── EmotionDetection/
│   ├── __init__.py          # Package initializer
│   └── emotion_detection.py # Core emotion detection logic
├── static/
│   └── mywebscript.js       # Frontend JavaScript
├── templates/
│   └── index.html           # Flask HTML template
├── server.py                # Flask web server
├── test_emotion_detection.py# Unit tests
├── requirements.txt         # Python dependencies
└── README.md                # This file
```

## Setup & Installation
```bash
pip install -r requirements.txt
```

## Running the Application
```bash
python server.py
```
Then open your browser at: http://localhost:5000

## Running Unit Tests
```bash
python -m pytest test_emotion_detection.py -v
# or
python -m unittest test_emotion_detection.py -v
```

## Static Code Analysis
```bash
pylint server.py
```

## Watson NLP Endpoint
The application calls:
```
https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict
```

## Course
IBM Skills Network — Developing AI Applications with Python and Flask
