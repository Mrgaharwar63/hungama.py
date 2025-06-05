def chatbot_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for case-insensitive matching

    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I didn't understand that."
def start_chat():
    print("🤖 Welcome to ChatBot!")
    print("Type something (type 'bye' to exit).")

    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Bot:", response)

        if user_input.lower() == "bye":
            break
# Start the chatbot
start_chat()
def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I didn't understand that."


def start_chat():
    print("🤖 Welcome to ChatBot!")
    print("Type something (type 'bye' to exit).")

    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Bot:", response)

        if user_input.lower() == "bye":
            break


# Start the chatbot
start_chat()

