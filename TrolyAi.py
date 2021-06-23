import speech_recognition
import pyttsx3
from datetime import date
from datetime import datetime

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""

while True:
	with speech_recognition.Microphone() as mic:
		print("Robot: I'm Listening")
		audio = robot_ear.listen(mic)

	print ("Robot: ...")

	try:
	    you = robot_ear.recognier_google(audio)
	except:
		you =""

	print("You:" + you)

	if you =="":
		robot_brain = "I can't hear you, try again"
	elif you == "hello":
		robot_brain = "Hello Cuong"
	elif you == "school" :
		robot_brain = "Vinh University"
	elif you =="home" :
	    robot_brain = "thanh chuong"
	elif you =="today":
	    today = date.today()
	    robot_brain = today.strftime("%B month %d day %Y year")
	elif you == "clock":
	    now = datetime.now()
	    robot_brain = now.strftime("%H hours %M minutes %S seconds")
	elif you =="bye":
		robot_brain ="Bye Cuong"
		print("Robot:" + robot_brain)
		robot_mouth.say(robot_brain)
		robot_mouth.runAndWait() 
		break
	else:
	    robot_brain = "I'm fine thank you and you"
	print("Robot:" + robot_brain)
	robot_mouth.say(robot_brain)
	robot_mouth.runAndWait() 