from dataclasses import dataclass


@dataclass
class EmotionResult:
    emotion: str
    confidence: float
    sentiment: str


EMOTION_KEYWORDS = {
    "joy": ["happy", "joy", "excited", "grateful", "proud", "relieved"],
    "sadness": ["sad", "down", "lonely", "tearful", "hopeless", "tired"],
    "anger": ["angry", "mad", "furious", "irritated", "frustrated"],
    "anxiety": ["anxious", "nervous", "worried", "panic", "overwhelmed"],
    "stress": ["stressed", "burned out", "pressure", "exhausted"],
    "fear": ["afraid", "scared", "fear", "terrified"],
}

POSITIVE_WORDS = {"good", "great", "better", "love", "calm", "okay", "safe"}
NEGATIVE_WORDS = {"bad", "awful", "terrible", "hurt", "unsafe", "hate", "lost"}


def detect_emotion(text: str) -> EmotionResult:
    lowered = text.lower()
    best_emotion = "neutral"
    best_score = 0

    for emotion, keywords in EMOTION_KEYWORDS.items():
        score = sum(1 for keyword in keywords if keyword in lowered)
        if score > best_score:
            best_score = score
            best_emotion = emotion

    positive_hits = sum(1 for word in POSITIVE_WORDS if word in lowered)
    negative_hits = sum(1 for word in NEGATIVE_WORDS if word in lowered)

    if positive_hits > negative_hits:
        sentiment = "positive"
    elif negative_hits > positive_hits:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    confidence = min(0.95, 0.2 + best_score * 0.2)

    return EmotionResult(emotion=best_emotion, confidence=confidence, sentiment=sentiment)


def build_empathic_response(result: EmotionResult, user_text: str) -> str:
    if result.emotion == "joy":
        return (
            "It sounds like you're feeling uplifted. "
            "What’s been supporting that positive energy for you lately?"
        )
    if result.emotion == "sadness":
        return (
            "I’m really sorry you’re feeling this way. "
            "Do you want to share what’s been weighing on you?"
        )
    if result.emotion == "anger":
        return (
            "That sounds frustrating, and it makes sense to feel upset. "
            "Would it help to talk through what sparked this?"
        )
    if result.emotion == "anxiety":
        return (
            "That sounds overwhelming. "
            "If you’d like, we can slow it down together and name what feels most urgent."
        )
    if result.emotion == "stress":
        return (
            "You’re carrying a lot right now. "
            "What’s one small thing that could take a little pressure off today?"
        )
    if result.emotion == "fear":
        return (
            "Feeling scared can be really heavy. "
            "Would you like to share what feels most uncertain right now?"
        )

    if result.sentiment == "positive":
        return "I’m glad to hear that. Want to tell me more about what’s going well?"

    if result.sentiment == "negative":
        return "That sounds tough. I’m here with you—what feels hardest at the moment?"

    return "Thanks for sharing. What’s been on your mind the most recently?"
