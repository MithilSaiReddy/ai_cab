# AiCab Crew

## Installation (Use python virtual environment)

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install crew:

```bash
pip install crewai
```
```bash
pip install 'crewai[tools]'
```
```bash
pip install chainlit
```
### Customizing

**Add your AI to `AI_API_KEY` into the `.env` file**

## Running the Project

Next, navigate to your project directory and run it using main python file

```bash
cd ai_cab
chainlit run  src/ai_cab/main.py
```

This command initializes the ai_cab Crew, assembling the agents and assigning them tasks as defined in your configuration.
This will give a localhost 

## Understanding Your Crew

The ai_cab Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

