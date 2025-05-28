# Basic Chatbot in Python using if-elif-else

print("Hi, I'm a chatbot. How can I help you?")

while True:
    user_input = input("You: ").lower()

    if user_input == "bye":
        print("Goodbye, have a nice day!")
        break

    elif user_input == "hello":
        print("Hi! How are you?")

    elif "your name" in user_input:
        print("I'm Alex, your chatbot.")

    elif "how are you" in user_input:
        print("I'm doing great!")

    elif "what can you do" in user_input:
        print("I can answer a few basic questions like my name or how I am.")

    elif "who made you" in user_input:
        print("I was created by Nasim.")

    elif "thank you" in user_input:
        print("You're welcome!")

    else:
        print("I'm not sure how to respond to that.")


