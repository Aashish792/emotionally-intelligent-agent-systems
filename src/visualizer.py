import matplotlib.pyplot as plt

def plot_emotions(agent_list):
    """
    Plots a bar chart showing the current emotion of each agent.
    """
    names = [agent.name for agent in agent_list]
    emotions = [agent.emotion for agent in agent_list]
    colors = {
        "joy": "yellowgreen",
        "anger": "orangered",
        "sadness": "skyblue",
        "neutral": "gray"
    }
    bar_colors = [colors.get(e, "gray") for e in emotions]

    plt.figure(figsize=(6, 4))
    plt.bar(names, [1]*len(names), color=bar_colors)
    plt.title("Agent Emotional States")
    plt.ylabel("Emotion Intensity (1=Current)")
    plt.ylim(0, 1.5)
    for i, emotion in enumerate(emotions):
        plt.text(i, 1.1, emotion, ha='center')
    plt.tight_layout()
    plt.show()
