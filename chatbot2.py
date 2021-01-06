import pyttsx3
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
chatbot = ChatBot('Sam')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")

# Get a response to an input statement
print('Enter Text and Wait')
x = input()


def speak(text):  # this defines the function SPEAK and creates the command for its use
    engine = pyttsx3.init()
    engine.say(text=text)
    engine.runAndWait()


def record():
    f = open('text.txt', 'w') #opens file in write mode
    b = chatbot.get_response(str(x)) #gets respounce relating to input x
    f.write(str(b))#writes string to file
    return b

def read_responce():
    fr = open('text.txt', 'r')#reads file
    speak(fr.read())#reads from the file
    return record()

def run():
        record()
        read_responce()
'''does all the above'''

if __name__ == '__main__':
    while 2 > 1:
        if x != 'goodbye':
            run()
        else:
            break# this only works at the start of the programe




