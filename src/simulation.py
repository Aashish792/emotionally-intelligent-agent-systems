from agent import Agent
from emotion_model import emotional_response

if __name__ == "__main__":
    agent = Agent("Eva")
    print("Emotion Simulation")
    while True:
        user_input = input("Enter emotion input (happy/sad/neutral): ")
        if user_input == "exit":
            break
        state = agent.respond(user_input)
        print(emotional_response(state))
