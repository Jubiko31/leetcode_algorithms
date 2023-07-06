# Random 16bit number generator with voice controll
# Commands: 
# 	Say "random number" to generate random number
#   Say "turn off" to stop the program
# @JubaMatsaberidze

import sys
import speech_recognition as sr
import pyttsx3
from random import getrandbits

r = sr.Recognizer()

def getRandom16Bit(cmd):
    if cmd == "random number":
        print(f"Random 16-bit number: {getrandbits(16)}")

def speak(command):
    if text == "turn off":
        sys.exit()
    getRandom16Bit(command)    
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
        
while 1:
	try:
		with sr.Microphone() as source2:
			r.adjust_for_ambient_noise(source2, duration=0.2)
			audio2 = r.listen(source2)
			text = r.recognize_google(audio2)
			text = text.lower()
			speak(text)   
			
	except sr.RequestError as e:
		print("Could not request results")	
  
	except sr.UnknownValueError:
		print("Something went wrong...UnknownValueError")
