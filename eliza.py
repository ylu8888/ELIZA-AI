## NAME: Yang Lu

## NetID: 114607667

import re
import random
import string  

def eliza_chatbot():
    print("Hello! I'm ELIZA, your virtual therapist. How can I help you today? (Type 'quit' to exit.)")

    while True:
        user_input = input("> ")

        # Exit condition
        if user_input.lower() == 'quit':
            print("Goodbye! Take care.")
            break

        # Patterns and responses
        responses = {
            r"I need (.*)": [
                "Why do you need %1?",
                "Would obtaining %1 really help you?",
                "Are you sure you need %1?"   
            ],
            
            r"Why don't you (.*)\??": [
                "Do you really think I don't %1?",
                "Perhaps eventually I will %1.",
                "Do you want me to %1?"    
            ],
            
            r"Why can't I (.*)\??": [
                "Do you think you should be able to %1?",
                "If you could %1, what would you do?",
                "What would help you %1?"    
            ],
            
            r"I am (.*)": [
                "Did you come to me because you are %1?",
                "How long have you been %1?",
                "How do you feel about being %1?"
            ],   

            r"How do I (.*)\??": [ #1
                "Have you ever tried to %1?",
                "Why do you want to %1?",
                "What would you do after you %1?"
            ],

            r"Is it fun to (.*)\??": [ #2
                "Perhaps it is, you should try to %1",
                "Not sure, I have never tried to %1",
                "Yes absolutely! I love to %1"
            ],

            r"What happens when we (.*)\??": [ #3
                "It is a great mystery what happens when we %1",
                "I am certain when we %1, it is the best",
                "Life continues all the same when we %1"
            ],

            r"Is it possible to (.*)\??": [ #4
                "Of course its possible to %1",
                "Certainly not, it's impossible to %1",
                "Why do you want to %1?"
            ],

            r"I don't know if I should (.*)": [ #5
                "Why are you uncertain if you should %1?",
                "Why do you think you should %1?",
                "What would your family and friends think if you did %1"
            ],

            r"I'm addicted to (.*)": [ #6
                "What do you feel when you do %1?",
                "Do you feel guilt or pleasure when you do %1",
                "Perhaps seek a therapist to stop doing %1"
            ],

            r"Help me I am scared of (.*)": [ #7
                "Why are you scared of %1?",
                "Have you tried seeking protection from %1",
                "What happened the last time you encountered %1"
            ],

            r"Can I achieve (.*)\??": [ #8
                "Why do you want to achieve %1?",
                "I am certain you will achieve %1, reach for the stars",
                "Is it your best course of action to achieve %1?"
            ],

            r"Someone stole my (.*)": [ #9
                "Have you called the police to help get back your %1?",
                "You should have gotten security to protect your %1",
                "How important is your %1 to you?"
            ],

            r"My friends want me to (.*)": [ #10
                "Do you want to %1 with your friends?",
                "Have your friends wanted you to %1 before?",
                "It is up to you to decide if you want to %1"
            ]


            # Add more patterns here
        
            
        }

        # This is the default response if no pattern matches
        default_response = "Tell me more."

        # This checks each pattern and selecting a response
        for pattern, pattern_responses in responses.items():
            match = re.fullmatch(pattern, user_input, re.IGNORECASE)
            if match:
                # This removes punctuation from the captured group
                captured_group = match.group(1).translate(str.maketrans('', '', string.punctuation))
                response = random.choice(pattern_responses)
                # This replaces the placeholder with the cleaned captured group
                response = response.replace('%1', captured_group)
                break
        else:
            response = default_response

        print(response)

# Run the chatbot
eliza_chatbot()
