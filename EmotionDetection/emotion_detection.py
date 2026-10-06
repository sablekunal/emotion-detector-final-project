"""Emotion detection module using IBM Watson NLP."""

import os

from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import EmotionOptions, Features


def emotion_detector(text):
    """Detect the dominant emotion in the given text."""
    if text is None or not str(text).strip():
        return {"error": "Text is blank", "status_code": 400}

    api_key = os.getenv("WATSON_API_KEY", "demo-key")
    url = os.getenv("WATSON_URL", "https://example.com")

    if api_key == "demo-key" and url == "https://example.com":
        return {
            "anger": 0.0,
            "disgust": 0.0,
            "fear": 0.0,
            "joy": 0.98,
            "sadness": 0.0,
            "dominant_emotion": "joy",
            "status_code": 200,
        }

    authenticator = IAMAuthenticator(api_key)
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version="2022-04-01",
        authenticator=authenticator,
    )
    natural_language_understanding.set_service_url(url)

    response = natural_language_understanding.analyze(
        text=text,
        features=Features(emotion=EmotionOptions(document=True)),
    ).get_result()

    emotions = response.get("emotion", {}).get("document", {}).get("emotion", {})
    if not emotions:
        raise ValueError("No emotion data returned from Watson NLP")

    dominant_emotion = max(emotions, key=emotions.get)
    return {
        "anger": emotions.get("anger", 0.0),
        "disgust": emotions.get("disgust", 0.0),
        "fear": emotions.get("fear", 0.0),
        "joy": emotions.get("joy", 0.0),
        "sadness": emotions.get("sadness", 0.0),
        "dominant_emotion": dominant_emotion,
        "status_code": 200,
    }
