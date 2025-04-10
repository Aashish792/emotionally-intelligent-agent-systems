class Agent:
    def __init__(self, name):
        self.name = name
        self.state = "neutral"

    def respond(self, input_signal):
        # Placeholder emotional response logic
        if "happy" in input_signal:
            self.state = "positive"
        elif "sad" in input_signal:
            self.state = "negative"
        else:
            self.state = "neutral"
        return self.state
