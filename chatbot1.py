from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from playsound import playsound
from gtts import gTTS
import os
chatbot = ChatBot('Sara')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")

# Get a response to an input statement
print('Enter Text and Wait')
x = input()


def speak(text):  # this defines the function SPEAK and creates the command for its use
    tts = gTTS(text=text, lang="en")
    filename = "textaudio.mp3"
    tts.save(filename)  # saves the audio file
    playsound(filename)
    os.remove(filename) #to avoid permission deined error when overwriting file our file becomes
                        # temp placeholder for the text
    return playsound

def record():
    f = open('text.txt', 'w') #opens file in write mode
    b = chatbot.get_response(str(x)) #gets respounce relating to input x
    f.write(str(b))#writes string to file
    return b

def read_responce():
    fr = open('text.txt', 'r')#reads file
    speak(fr.read())#reads from and paces the file to text
    return record()

def run():
        record()
        read_responce()
'''does all the above'''

'''problems gtts needs internet
and responce is very slow
'''
if __name__ == '__main__':
    while 2 > 1:
        if x != 'goodbye':# this only works at the start of the programe
            run()
        else:
            break
