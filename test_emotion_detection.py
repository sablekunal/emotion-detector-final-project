"""Unit tests for the emotion detector."""

from EmotionDetection.emotion_detection import emotion_detector


def test_emotion_detector_handles_blank_input():
    """Blank input must return a 400 code."""
    result = emotion_detector("   ")
    assert result["status_code"] == 400
    assert result["error"] == "Text is blank"


def test_emotion_detector_uses_dominant_emotion():
    """The dominant emotion should be returned as part of the response."""
    result = emotion_detector("I am incredibly happy today.")
    assert "dominant_emotion" in result
    assert result["dominant_emotion"] == "joy"
    assert result["status_code"] == 200


def test_emotion_detector_returns_expected_keys():
    """All emotion score keys should be present."""
    result = emotion_detector("I feel nervous but hopeful.")
    assert set(result.keys()) >= {
        "anger",
        "disgust",
        "fear",
        "joy",
        "sadness",
        "dominant_emotion",
        "status_code",
    }
