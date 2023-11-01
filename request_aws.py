import openai

# Define your OpenAI API key
api_key = "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"  # Replace with your API key

# Initialize the OpenAI API client
openai.api_key = api_key

# Function to interact with the chatbot
def chat_with_bot(user_input):
    # Define a system message to set the bot's behavior
    system_message = "You are a helpful shopping assistant named Pepper."

    # Create a conversation with a user prompt
    conversation = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_input}
    ]

    # Send the conversation to the chatbot
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
        temperature=0.7,
        max_tokens=150
    )

    # Extract and return the bot's response
    bot_response = response['choices'][0]['message']['content']
    print(bot_response)
    return bot_response
def req(user_input):
	return chat_with_bot("User: " + user_input)
