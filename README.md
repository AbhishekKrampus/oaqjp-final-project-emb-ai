# Emotion Detector – IBM AI Applications with Python and Flask Final Project

## Overview
An AI-powered web application that analyzes customer feedback text using embedded Watson NLP libraries to detect nuanced emotions: **joy, sadness, anger, disgust, and fear**, along with identifying the **dominant emotion**.

## Project Structure
```
oaqjp-final-project-emb-ai/
├── EmotionDetection/
│   ├── __init__.py           # Package init – exports emotion_detector
│   └── emotion_detection.py  # Watson NLP emotion detection function
├── static/
│   └── mywebscript.js        # Frontend JavaScript
├── templates/
│   └── index.html            # Flask HTML template
├── server.py                 # Flask web application
├── test_emotion_detection.py # Unit tests (unittest)
└── README.md
```

## Setup & Installation

```bash
pip install flask requests pylint
```

## Running the Application

```bash
python server.py
```

Then open your browser at: [http://localhost:5000](http://localhost:5000)

## Running Unit Tests

```bash
python -m unittest test_emotion_detection.py -v
```

## Static Code Analysis

```bash
python -m pylint server.py
```

## Watson NLP API

- **Endpoint:** `https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict`
- **Method:** POST
- **Header:** `grpc-metadata-mm-model-id: emotion_aggregated-workflow_lang_en_stock`

> **Note:** The Watson NLP endpoint is only accessible from within the IBM Skills Network lab environment.

## Emotions Detected
- Anger
- Disgust
- Fear
- Joy
- Sadness

## License
This project is part of the IBM Full Stack Software Developer Professional Certificate.
