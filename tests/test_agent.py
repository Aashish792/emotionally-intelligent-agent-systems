from src.agent import Agent

def test_emotion_response():
    agent = Agent("Test")
    assert agent.receive_input("happy") == "joy"
    assert agent.respond() == "Test smiles warmly and nods."
    agent.reset()
    assert agent.emotion == "neutral"
    assert len(agent.history) == 0

if __name__ == "__main__":
    test_emotion_response()
    print("All agent tests passed.")
