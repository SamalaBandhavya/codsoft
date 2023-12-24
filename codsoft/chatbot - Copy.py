import random

# File path to store the conversation history
conversation_file = "conversation_history.txt"

# Load conversation history from file
def load_conversation_history():
    try:
        with open(conversation_file, "r") as file:
            return file.read()
    except FileNotFoundError:
        return ""

# Save conversation history to file
def save_conversation_history(conversation):
    with open(conversation_file, "a") as file:
        file.write(conversation + "\n")

# Dictionary of predefined questions and answers
conversations = {
    "hi": ["Hello!", "Hi there!", "Greetings!"],
    "how are you?": ["I'm good, thank you!", "I'm doing well! How about you?", "All good!"],
    "what's your name?": ["I am a Chatbot.", "You can call me Chatbot.", "I don't have a specific name."],
    "default": ["I'm sorry, I didn't understand that.", "Could you please rephrase that?", "I'm still learning. Can you ask something else?"]
}

# Function to generate responses
def generate_response(user_input):
    user_input = user_input.lower()
    for key in conversations:
        if key in user_input:
            return random.choice(conversations[key])
    return random.choice(conversations["default"])

# Main program loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    else:
        response = generate_response(user_input)
        print("Chatbot:", response)
        conversation = f"You: {user_input}\nChatbot: {response}"
        save_conversation_history(conversation)
        