from agent import Agent
from interaction_manager import InteractionManager

def main():
    agent_1 = Agent("Maya")
    agent_2 = Agent("Leo")
    manager = InteractionManager([agent_1, agent_2])

    print("Emotion Simulation Started")
    print("Type 'exit' to stop.\n")

    while True:
        stimulus_1 = input("Input for Maya: ")
        if stimulus_1.lower() == "exit":
            break
        stimulus_2 = input("Input for Leo: ")

        result = manager.run_turn({
            "Maya": stimulus_1,
            "Leo": stimulus_2
        })

        print("\n--- Round Output ---")
        for line in result:
            print(line)
        print("--------------------\n")

if __name__ == "__main__":
    main()
