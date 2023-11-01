import openai

# Define your OpenAI API key
api_key = "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"  # Replace with your API key

# Initialize the OpenAI API client
openai.api_key = api_key

# Function to interact with the chatbot
def chat_with_bot(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
    )
    return response.choices[0].text

def req(user_input):
	return chat_with_bot("User: " + user_input)