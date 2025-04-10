# src/interaction_manager.py

from agent import Agent
from emotion_model import interpret_emotion

class InteractionManager:
    def __init__(self, agents: list):
        self.agents = agents

    def run_turn(self, stimulus_map: dict):
        """
        Takes a stimulus_map {agent_name: trigger} and processes one turn.
        """
        outputs = []
        for agent in self.agents:
            stimulus = stimulus_map.get(agent.name, "silence")
            emotion = interpret_emotion(stimulus)
            agent.receive_input(stimulus)
            outputs.append(f"{agent.name} feels {emotion} and {agent.respond()}")
        return outputs
