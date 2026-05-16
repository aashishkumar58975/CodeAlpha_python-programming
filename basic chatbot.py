# Simple Rule-Based Chatbot in Python

# Function to reply to user messages
def chatbot_reply(user_message):

    # Convert message to lowercase
    # so "Hello" and "hello" both work
    user_message = user_message.lower()

    # Different chatbot replies
    if user_message == "hello":
        return "Hiiii !"

    elif user_message == "how are you":
        return "I am fine thanks !"

    elif user_message == "bye":
        return "Goodbye !"

    else:
        return "Sorry, I don't understand that."


# Start chatbot
print("Simple Chatbot")
print("Type 'bye' to end the chat.\n")

# Run chatbot continuously
while True:

    # Take input from user
    user_input = input("You: ")

    # Get bot reply
    response = chatbot_reply(user_input)

    # Print bot reply
    print("Bot:", response)

    # Stop chatbot if user says bye
    if user_input.lower() == "bye":
        break