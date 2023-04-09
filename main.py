
import os
import openai


# Set up the OpenAI API credentials
openai.api_key = "openapikeyyours"

# Define a function to send a request to the OpenAI API
def ask_gpt3(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="",
        temperature=0.1,
        max_tokens=1010,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0

    )
    message = response.choices[0].text.strip()
    return message

# Define a function to handle the chatbot's responses
def chatbot():
    while True:
        user_input = input("You: ")
        prompt = f"User: {user_input}\nChatbot:"
        response = ask_gpt3(prompt)
        print("Chatbot:", response)

# Start the chatbot
chatbot()
