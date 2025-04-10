# src/emotion_model.py

def interpret_emotion(trigger: str) -> str:
    """
    Maps an input trigger to an emotion.
    """
    mapping = {
        "encouragement": "joy",
        "criticism": "anger",
        "loss": "sadness",
        "silence": "neutral",
        "joke": "joy",
        "conflict": "anger"
    }
    return mapping.get(trigger.lower(), "neutral")
