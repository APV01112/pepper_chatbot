import urllib2
import json

# Define the URL of your Flask API
api_url = "http://13.42.27.138:8080/ask"  # Replace with your Flask API URL

def question(user_input):

    # Create a dictionary with the question
    data = {}
    data["question"] = user_input

    # Encode the data as JSON
    data_json = json.dumps(data)

    # Send a POST request to the API to ask the question
    req = urllib2.Request(api_url, data_json, headers={'Content-Type': 'application/json'})
    response = urllib2.urlopen(req)
    result = json.loads(response.read())

    # Print the answer
    return result.get("answer")

