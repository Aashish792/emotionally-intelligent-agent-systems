# src/agent.py

class Agent:
    def __init__(self, name):
        self.name = name
        self.emotion = "neutral"
        self.history = []

    def receive_input(self, stimulus: str):
        """
        Updates emotional state based on stimulus.
        """
        if "happy" in stimulus:
            self.emotion = "joy"
        elif "angry" in stimulus:
            self.emotion = "anger"
        elif "sad" in stimulus:
            self.emotion = "sadness"
        else:
            self.emotion = "neutral"
        
        self.history.append((stimulus, self.emotion))
        return self.emotion

    def respond(self):
        """
        Generates a response based on current emotion.
        """
        responses = {
            "joy": "smiles warmly and nods.",
            "anger": "frowns and steps back.",
            "sadness": "looks down quietly.",
            "neutral": "remains attentive."
        }
        return f"{self.name} {responses.get(self.emotion, 'has no response')}"

    def reset(self):
        self.emotion = "neutral"
        self.history.clear()
