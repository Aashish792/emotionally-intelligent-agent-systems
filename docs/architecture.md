# Project Architecture

## Overview
This project simulates emotionally intelligent agent interactions using modular Python code. It is structured to allow:
- Easy extensibility for new emotions and agents
- Integration with visualization tools
- Use in co-design research studies

## Modules
- `agent.py` — maintains internal emotional state
- `emotion_model.py` — maps stimuli to emotional states
- `interaction_manager.py` — coordinates interaction logic
- `visualizer.py` — provides graphical feedback

## Flow Diagram (Conceptual)
User Stimulus → Emotion Mapping → Agent State Update → Agent Response → Visualization
