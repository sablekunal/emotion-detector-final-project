"""Flask web deployment for the emotion detector application."""

from flask import Flask, jsonify, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def home():
    """Home route for the API."""
    return "Emotion Detector API is running."


@app.route("/emotion", methods=["GET"])
def detect_emotion():
    """Detect emotions from a text query parameter."""
    text = request.args.get("text", "")
    if not text or not text.strip():
        return jsonify({"error": "Text is blank", "status_code": 400}), 400

    result = emotion_detector(text)
    status_code = result.get("status_code", 200)

    if status_code >= 400:
        return jsonify({
            "error": result.get("error", "Unknown error"),
            "status_code": status_code
        }), status_code

    return jsonify(result), status_code


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
