# Debate Simulation with GPT-4

## Project Description
This project leverages OpenAI's GPT-4 to simulate a debate between two bots, each taking opposing stances on a given topic. The simulation allows for dynamic interactions, with each bot responding to the other's arguments in a structured and assertive manner. This can serve as a tool for understanding multiple perspectives on a topic or for entertainment purposes.

## Features
- **Dynamic Debate Simulation:** Engages two instances of GPT-4 in a debate, with one taking the "Pro" stance and the other the "Con" stance on any given topic.
- **Customizable Topics:** Users can input any topic for debate, providing flexibility in the scope of discussions.
- **Structured Interactions:** Ensures that each bot's response is direct and relevant to the ongoing discussion, maintaining a coherent flow of debate.

## Installation

### Prerequisites
- Python 3.8 or later
- Jupyter
- An OpenAI API key

### Setup
1. Clone this repository to your local machine.
2. Install the required Python packages:

```bash
pip install openai dotenv jupyter
```

3. Create a `.env` file in the root directory of the project and add your OpenAI API keys:

```plaintext
OPENAI_API_KEY_1=your_api_key_here
OPENAI_API_KEY_2=your_second_api_key_here
```

## Usage

To run the debate simulation, navigate to the file directory execute the following command in the terminal:

```bash
jupyter notebook
```

And open the Debate.ipynb file
