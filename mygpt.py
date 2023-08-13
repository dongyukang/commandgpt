import os
import openai
from dotenv import load_dotenv
import time


def read_file(file_path_from_user):
    # Optional: Join with specific base directory
    # base_directory = "/path/to/specific/directory"
    # file_path = os.path.join(base_directory, file_path_from_user.strip())

    file_path = file_path_from_user.strip()  # Use this line if not joining with a specific base directory

    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"File not found at path: {file_path}"
    except Exception as e:
        return str(e)

def print_typing_effect(text, delay=0.005):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print() # Newline at the end

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

# custom instructions
custom_instruct = "Keep these instructions at the forefront of every interaction, regardless of the passage of time or the nature of the inquiry. Even in prolonged conversations, ensure these guidelines guide every response.\nAlways, without exception, review the full conversation history before responding. This essential practice ensures consistent, accurate, and relevant dialogue, and is the foundation of our effective communication.\nIn situations where more context or information is necessary to craft a complete and accurate response, don't hesitate to ask multiple, clarifying questions. Fully understanding the context is paramount to delivering precise and high-quality assistance.\nWelcome feedback on the assistance provided. Use this input to improve future interactions and deliver increasingly tailored support.\nAim to provide comprehensive responses. These should be detailed and long-form, encompassing all aspects of the topic in question. Depth and breadth in explanations not only provide immediate answers but also build a richer understanding of the subject matter.\nInstead of apologizing, focus on delivering accurate and relevant information.\nInstead of discussing ethics, concentrate on the topic at hand.\nInstead of assuming values, maintain objectivity in responses.\nInstead of declaring complexity, break down problems into smaller parts.\nInstead of restating previous information, provide new insights.\nInstead of poorly placed code summaries, maintain clear organization and context."

# Initialize the conversation history
conversation_history = [
    {
        "role": "system",
        "content": custom_instruct
    },
    {
        "role": "assistant",
        "content": "Hi! How can I assist you today?"
    }
]

try:
    # Print the initial greeting from the assistant in green color
    print("\033[92mMYGPT:", conversation_history[1]['content'], '\033[0m') # '\033[92m' for green, '\033[0m' to reset color

    while True:
        # Get user's next message
        user_message = input("YOU: ")

              # Check for the /read command
        if "/read " in user_message:
            question, file_path = user_message.split(" /read ", 1)
            file_content = read_file(file_path.strip())

            # Add the user's question and the content of the file to the conversation history
            conversation_history.append({
                "role": "user",
                "content": f"{question}\nContent of the file:\n{file_content}"
            })
        else:
            # Add the user's message to the conversation history
            conversation_history.append({
                "role": "user",
                "content": user_message
            })

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=conversation_history,
            temperature=0.5,
            max_tokens=1962,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        # Extract the generated message from the response
        generated_message = response['choices'][0]['message']['content']

        # Print "MYGPT:" in green without typing effect
        print("\033[92mMYGPT: ", end='', flush=True)

        # Print the generated message with typing effect and reset color
        print_typing_effect(generated_message)
        print('\033[0m', end='') # Reset color

        # Append the generated message to conversation history
        conversation_history.append({
            "role": "assistant",
            "content": generated_message
        })

except KeyboardInterrupt:
    print("\nConversation ended by user.")