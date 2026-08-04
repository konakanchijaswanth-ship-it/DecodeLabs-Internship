import random
import datetime

# -----------------------------
# Rule-Based Chatbot
# -----------------------------

def greet():
    print("=" * 50)
    print("🤖 Welcome to Decode Labs Rule-Based Chatbot")
    print("Type 'help' to see available commands.")
    print("Type 'exit' to end the chat.")
    print("=" * 50)

def show_help():
    print("\nAvailable Commands:")
    print("1. hi / hello")
    print("2. how are you")
    print("3. what is your name")
    print("4. time")
    print("5. date")
    print("6. python")
    print("7. internship")
    print("8. help")
    print("9. exit\n")

def chatbot():
    greetings = [
        "Hello! Nice to meet you.",
        "Hi! How can I help you today?",
        "Welcome! Hope you're having a great day!"
    ]

    while True:
        user = input("You : ").strip().lower()

        if user in ["hi", "hello", "hey"]:
            print("Bot :", random.choice(greetings))

        elif user == "how are you":
            print("Bot : I'm doing great! Thanks for asking.")

        elif user == "what is your name":
            print("Bot : My name is DecodeBot.")

        elif user == "time":
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            print("Bot : Current Time:", current_time)

        elif user == "date":
            current_date = datetime.datetime.now().strftime("%d-%m-%Y")
            print("Bot : Today's Date:", current_date)

        elif user == "python":
            print("Bot : Python is a powerful programming language used for AI, Web Development, Data Science, and Automation.")

        elif user == "internship":
            print("Bot : Decode Labs provides practical projects to improve your programming skills.")

        elif user == "help":
            show_help()

        elif user in ["exit", "bye", "quit"]:
            print("Bot : Thank you for chatting. Have a wonderful day!")
            break

        else:
            print("Bot : Sorry, I don't understand that. Type 'help' to see available commands.")

# Main Program
greet()
chatbot()