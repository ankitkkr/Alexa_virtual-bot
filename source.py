import speech_recognition as sr
import pyttsx3
import kit
# import pywhatkit as kit
import datetime
import dt


listner = sr.Recognizer()
engine = pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def talk(text):
	engine.say(text)
	engine.runAndWait()


def listen():
	try:
		with sr.Microphone() as source:
			print('listning.....')
			voice=listner.listen(source)
			command=listner.recognize_google(voice)
			command=command.lower()
			print(command)
			return command
		

	except:
		pass

def perform(data):
	if 'play' in data:
		kit.play(data)

	elif 'search' in data:
		kit.search(data)

	elif 'who is' in data:
		kit.who_is(data)

	elif 'write' in data:
		talk('tell me what to write')
		string=str(listen())
		kit.write(string)

	elif 'tutorial' in data:
		kit.tutorial()

	elif 'day' in  data:
		talk(str(dt.day()))

	elif 'year' in data: 
		talk(dt.year())

	elif 'month' in data:
		talk(dt.month)
	




def runalexa():
	talk('hello there, how can i help you')
	command = listen()
	if 'alexa' in command:
		command=command.replace('alexa','')
		perform(command)

runalexa()