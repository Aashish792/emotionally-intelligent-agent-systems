# Emotionally Intelligent Agent-Based Systems

> A Python-based framework for designing emotionally intelligent agent-based systems using co-design principles and motivational modeling.

This project simulates digital agents capable of responding to emotional cues, designed to reflect human emotional goals in interactive environments. Inspired by the research of Prof. Leon Sterling, the framework enables research and experimentation in agent-based simulation, emotional interaction logic, and human-centered computing.

---

## 💡 Key Features

- 🧠 Emotion-aware agents that update internal states based on user inputs or environmental triggers
- 🗣️ Text-based and visual simulation of agent responses
- 🛠️ Modular architecture for research extensibility
- 📊 Built-in visualization with `matplotlib` for emotional state tracking
- 📒 Jupyter notebooks for testing and demonstration
- ✅ Simple unit tests included for agent behavior and emotion mapping

---

## 📂 Project Structure

```
emotionally-intelligent-agent-systems/
├── src/                    # Core logic
│   ├── agent.py
│   ├── emotion_model.py
│   ├── interaction_manager.py
│   ├── simulation.py
│   └── visualizer.py
├── notebooks/              # Interactive demos
│   ├── 01_agent_demo.ipynb
│   └── 02_emotion_logic_test.ipynb
├── docs/                   # Project documentation
│   ├── architecture.md
│   └── emotion_mapping_reference.md
├── tests/                  # Unit tests
│   ├── test_agent.py
│   └── test_emotion_model.py
├── requirements.txt
└── README.md
```

---

## 🧪 How to Run

### ▶️ Interactive Simulation
```bash
python src/simulation.py
```

### 📊 Visual Demo in Jupyter Notebook
```bash
jupyter notebook notebooks/01_agent_demo.ipynb
```

---

## 🧠 Emotion Mapping

Basic stimuli → emotion logic is defined in `emotion_model.py`. You can customize the mapping in your experiments:

| Stimulus      | Emotion  |
|---------------|----------|
| encouragement | joy      |
| joke          | joy      |
| criticism     | anger    |
| conflict      | anger    |
| loss          | sadness  |
| silence       | neutral  |

---

## 🧪 Run Tests

```bash
python tests/test_agent.py
python tests/test_emotion_model.py
```

---

## 🎓 Academic Context

This project is being developed as part of a PhD research application to the University of Melbourne, under the guidance of research themes led by **Prof. Leon Sterling**. The aim is to explore emotionally intelligent computing through agent-based modeling and co-designed interaction frameworks.

---


## 🤝 Contributions

Coming soon: contribution guidelines, advanced modules (e.g., reinforcement learning, emotional feedback loops), and UI/UX components.

---

> Designed by Aashish K C • [GitHub](https://github.com/Aashish792)
```
