def chatbot_response(user_input):
    user_input = user_input.lower()
    
    if 'hello' in user_input:
        return "Hello! How can I help you?"
    elif 'how are you' in user_input:
        return "I am just a bot, but I'm doing great! How about you?"
    elif 'your goodname' in user_input:
        return "I am a simple rule-based chatbot."
    elif 'today weather report' in user_input:
        return "I can't check the weather, but you can ask weather reporters!"
    elif 'bye' in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to respond to that. Can you try asking something else?"

def main():
    print("Chatbot: Hello! I am a simple rule-based chatbot. How can I assist you?")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
