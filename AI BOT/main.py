print("Namaste! What's on ypur mind today?")
print("Type 'bye' to exit.")

#chatbot memory

response = {
    'hello': 'Hello, How can i help you today?',
    'how are you': 'I am Very good. Thank you! ',
    'who are you': 'I am a simple bot made by TK',
    'What is today': 'Today is your day!',
    'motivate me': 'You are the best! Nobody can defeat you.'

}

#function to get response

def getResponse(userQuestion):
    userQuestion = userQuestion.lower()
    for eachKey in response:
        if eachKey in userQuestion:
            return response[eachKey]
    return "Currently I am unable to answer this. Ask another question." 
   

# user input

while True:
    userInput = input("Please ask your question:")
    reply = getResponse(userInput)
    print(reply)

    if "Bye" in userInput.lower():
        break