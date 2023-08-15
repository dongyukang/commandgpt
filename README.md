# Interactive Chatbot with Loading Animation

This project implements an interactive chatbot using OpenAI's GPT-3.5 model, providing a typing effect and a loading animation in the command-line interface.

![Screen Shot](https://i.imgur.com/khIGf2q.png)

## Features

- **Loading Animation:** While waiting for the GPT-3.5 response, a dynamic loading animation is displayed to the user.
- **Typing Effect:** The bot's responses are printed one character at a time, simulating a typing effect.
- **Conversation History:** The conversation history is maintained and used in generating responses, allowing for consistent and context-aware interaction.
- **Custom Instructions:** Specific guidelines and instructions can be set to guide the model's responses.

## Requirements

- Python 3.x
- OpenAI Python package
- dotenv package for environment variable handling

## Installation

1. Clone the repository.
2. Install the required packages using the following command:

   ```bash
   pip install openai python-dotenv
   ```

3. Set up the OpenAI API key in a `.env` file in the project root directory with the following content:

   ```env
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

1. Run the Python script using the command:

   ```bash
   python your_script_name.py
   ```

2. Follow the on-screen instructions to interact with the chatbot.

## Functions

- **`loading_animation()`:** Displays a dynamic loading animation.
- **`stop_loading_animation()`:** Stops the loading animation and clears it from the console.
- **`print_typing_effect(text, delay=0.005)`:** Prints the given text to the console, one character at a time, with a specified delay.

## Custom Instructions

The script allows custom instructions to be passed to the GPT-3.5 model, which can be modified in the `custom_instruct` variable.

## Exiting the Program

The conversation can be ended by the user by initiating a keyboard interrupt (Ctrl+C).