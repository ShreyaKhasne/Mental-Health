from flask import Flask, jsonify, request, send_from_directory
from emotion import build_empathic_response, detect_emotion

app = Flask(__name__, static_folder="../frontend", static_url_path="")


@app.get("/")
def index():
    return send_from_directory(app.static_folder, "index.html")


@app.get("/api/health")
def health_check():
    return jsonify({"status": "ok"})


@app.post("/api/analyze")
def analyze_text():
    payload = request.get_json(silent=True) or {}
    text = payload.get("text", "").strip()

    if not text:
        return jsonify({"error": "Text is required."}), 400

    result = detect_emotion(text)
    response = build_empathic_response(result, text)

    return jsonify(
        {
            "emotion": result.emotion,
            "confidence": result.confidence,
            "sentiment": result.sentiment,
            "response": response,
        }
    )


@app.post("/api/voice")
def analyze_voice():
    payload = request.get_json(silent=True) or {}
    transcript = payload.get("transcript", "").strip()

    if not transcript:
        return jsonify({"error": "Transcript is required."}), 400

    result = detect_emotion(transcript)
    response = build_empathic_response(result, transcript)

    return jsonify(
        {
            "emotion": result.emotion,
            "confidence": result.confidence,
            "sentiment": result.sentiment,
            "response": response,
            "transcript": transcript,
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
