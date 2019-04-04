from pyttsx3 import *
import datetime
import webbrowser as wb

engine = init()

name = input("Enter your name:\n")

engine.say("Initiating Jarvis command sequence")
engine.say("Connecting to the server")
engine.say("Initiating Database")
engine.say("Establishing all connections")
engine.say("All commands online")
engine.say("Your Jarvis is online")

if name.lower() == "kartik":

    data = input("What is my task sir:\n")

    if data.lower() == "date":
        engine.say("Today's date is: " + str(datetime.date.today()))

    elif data.lower() == "time":
        engine.say("Current time is: "+str(datetime.datetime.today().strftime("%H: %M")))

    elif data.lower() == "intro":
        engine.say("Hello sir, i'm Jarvis and my version is 1.0")

    elif data.lower() == "hi":
        engine.say("Hello")

    elif data.lower() == "facebook":
        engine.say("Opened Facebook on your browser")
        wb.open_new_tab("www.facebook.com")

    elif data.lower() == "instagram":
        engine.say("Opened Instagram on your browser")
        wb.open_new_tab("www.instagram.com")

    elif data.lower() == "youtube":
        engine.say("Opened Youtube on your browser")
        wb.open_new("www.youtube.com")

    elif data.lower() == "your age":
        engine.say("I was made on April 04 2019, for an experiment")

    elif data.lower() == "exit":
        engine.say("It's a pleasure to meet you sir")
        engine.say("Have a good day sir")
        engine.say("Disconnecting from the server")
        engine.say("De-initializing Jarvis command sequence")
        engine.say("Jarvis is offline")

    else:
        engine.say("Sorry, I am not programmed yet to carryout that task, Thank you")

else:
    engine.say("Sorry, you don't have the permission to access me")
    engine.say("Please contact Mr. Kartik for more details")

engine.runAndWait()
