const textInput = document.getElementById("text-input");
const voiceInput = document.getElementById("voice-input");
const analyzeTextButton = document.getElementById("analyze-text");
const analyzeVoiceButton = document.getElementById("analyze-voice");

const emotion = document.getElementById("emotion");
const sentiment = document.getElementById("sentiment");
const confidence = document.getElementById("confidence");
const response = document.getElementById("response");

const updateResults = (payload) => {
  emotion.textContent = payload.emotion ?? "—";
  sentiment.textContent = payload.sentiment ?? "—";
  confidence.textContent =
    payload.confidence !== undefined ? `${Math.round(payload.confidence * 100)}%` : "—";
  response.textContent = payload.response ?? "Share a check-in to see a supportive response.";
};

const handleError = (message) => {
  updateResults({
    emotion: "—",
    sentiment: "—",
    confidence: undefined,
    response: message,
  });
};

const postJson = async (url, payload) => {
  const response = await fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  const data = await response.json();
  if (!response.ok) {
    throw new Error(data.error || "Something went wrong.");
  }

  return data;
};

analyzeTextButton.addEventListener("click", async () => {
  const text = textInput.value.trim();
  if (!text) {
    handleError("Please add some text so I can check in with you.");
    return;
  }

  try {
    const data = await postJson("/api/analyze", { text });
    updateResults(data);
  } catch (error) {
    handleError(error.message);
  }
});

analyzeVoiceButton.addEventListener("click", async () => {
  const transcript = voiceInput.value.trim();
  if (!transcript) {
    handleError("Please add a transcript so I can listen in.");
    return;
  }

  try {
    const data = await postJson("/api/voice", { transcript });
    updateResults(data);
  } catch (error) {
    handleError(error.message);
  }
});
