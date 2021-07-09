import pywhatkit as kit

def play (data):
	song=data.replace('play','')
	print('playing '+song)
	kit.playonyt(song)

def search (data):
	topic=data.replace('search','')
	print('searching '+topic)
	kit.search(topic)

def write (string):
	kit.text_to_handwriting(string)


def who_is(data):
	topic=data.replace('who is','')
	kit.info(topic,2)


def tutorial():
	kit.tutorial_english()