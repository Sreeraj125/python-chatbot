


def chatbot():

    
    print("Hello! I am a simple chatbot.")
    print("You can talk to me. Type 'quit' to exit.")
    print("-" * 40)  

    
    while True:


        
        user_message = input("You: ")

        user_message = user_message.lower()

        
        if user_message == "quit":
            print("Bot: Goodbye! Have a nice day!")
            break  

        
        elif "hello" in user_message or "hi" in user_message:
            print("Bot: Hey there! How are you doing?")

        
        elif "how are you" in user_message:
            print("Bot: I am just a program, but I am doing great! Thanks for asking.")

        
        elif "your name" in user_message or "who are you" in user_message:
            print("Bot: I am PyBot, your simple Python chatbot!")

        
        elif "thank" in user_message:
            print("Bot: You're welcome! Happy to help.")

        
        elif "help" in user_message:
            print("Bot: Sure! You can say hello, ask my name, or just chat.")

        
        else:
            print("Bot: Hmm, I didn't understand that. Try saying hello or asking for help!")


if __name__ == "__main__":
    chatbot()