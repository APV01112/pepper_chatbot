# pepper_chatbot

   +---------------------+                     +------------------------+  
   |    Your Pepper      |                     |   Your EC2 Instance   |  
   |  (Python 2.7 Env)  |                     |  (Python 3.x & Flask)  |  
   +---------------------+                     +------------------------+  
              |                                          |  
              | HTTP Requests                           |  
              |                                          |  
              v                                          v  
   +---------------------+                     +------------------------+  
   |   Python 2.7 Code  |  HTTP Requests       |   Flask Application   |  
   |  Sending User Input|---------------------> |  Receives User Input, |  
   |   to EC2 Endpoint  |  Bot's Response      |  Communicates with    |  
   |                    <---------------------> |  OpenAI's API         |  
   +---------------------+  Bot's Response      +------------------------+  
                                    |                           
                                    | HTTP Responses             
                                    |                           
                                    v                           
                           +----------------------+              
                           |   Python 2.7 Code   |              
                           |  on Pepper Receives |              
                           |    Bot's Response   |              
                           +----------------------+              
