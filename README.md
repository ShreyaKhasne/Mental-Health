# AI-Powered Mental Health Companion

A lightweight full-stack prototype that detects emotions from text or voice transcripts and replies with empathetic guidance.

## Features
- NLP-inspired keyword emotion detection
- Sentiment analysis (positive/negative/neutral)
- Empathetic chatbot responses
- Frontend dashboard with text + voice check-ins

## Tech Stack
- **Backend:** Flask API
- **Frontend:** Vanilla HTML/CSS/JS

## Running locally

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then open [http://localhost:5000](http://localhost:5000) in your browser.

## Next steps
- Replace keyword heuristics with transformer-based embeddings.
- Add speech-to-text for live voice input.
- Persist conversation history for longer support sessions.
