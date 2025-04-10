from src.emotion_model import interpret_emotion

def test_emotion_mapping():
    assert interpret_emotion("encouragement") == "joy"
    assert interpret_emotion("conflict") == "anger"
    assert interpret_emotion("loss") == "sadness"
    assert interpret_emotion("silence") == "neutral"
    assert interpret_emotion("randomword") == "neutral"

if __name__ == "__main__":
    test_emotion_mapping()
    print("All emotion model tests passed.")
