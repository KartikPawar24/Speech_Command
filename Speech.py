from pyttsx3 import *
import datetime
import webbrowser as wb

engine = init()

engine.say("Hello sir, i'm Jarvis and my version is 1.0")
engine.say("Initiating Jarvis command sequence")
engine.say("Connecting to the server")
engine.say("All commands online")
engine.say("Today's date is: "+str(datetime.date.today()))
engine.say("I can do any task that you tell me to handle on your computer sir")


data = input("What is my task sir:")

if data.lower() == "hi":
    engine.say("Hello")

elif data.lower() == "facebook":
    engine.say("Opening Facebook")
    wb.open_new_tab("www.facebook.com")

elif data.lower() == "instagram":
    engine.say("Opening Instagram")
    wb.open_new_tab("www.instagram.com")

elif data.lower() == "youtube":
    engine.say("Opening Youtube")
    wb.open_new("www.youtube.com")

else:
    engine.say("I have still not programmed for that sir, thank you")


engine.say("It's a pleasure to meet you sir")
engine.say("Have a good day sir")

engine.runAndWait()