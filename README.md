# pepper_chatbot

Certainly, here's a textual description of the architecture:

Your Pepper device, which runs a Python 2.7 environment, serves as the primary interface for user interaction. When a user makes a request or query, the Python 2.7 code on Pepper initiates an HTTP request to an endpoint hosted on your Amazon EC2 (Elastic Compute Cloud) instance. This EC2 instance runs a Flask web application, which is built using Python 3.x. This Flask application receives the user's input, relays it to OpenAI's API for processing, and waits for the response. Once the response is received from OpenAI, the Flask application sends it back to the Python 2.7 code running on Pepper through the same HTTP channel. This architecture allows your Pepper to interact with the GPT-3.5 Turbo model via the intermediary Flask application, facilitating seamless communication between the older Python 2.7 environment and modern Python 3.x infrastructure.
