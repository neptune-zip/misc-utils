import datetime as dt
import ctypes
import time

print("Meeting alarm by Kyle N - 14th October 2024\n\n\n\n")

try:
    meeting= {}
    meeting["name"] = input("Please enter the name of the meeting: ")
    validated = False
    
    while (not validated):
        try:
            meeting["hour"] = int(input("What is the hour of the meeting: "))
            meeting["minute"] = int(input("What is the minute of the meeting: "))
        except:
            print("You did not enter a number, please start again.\n\n")
            continue
        validated = True

    today = dt.datetime.now()
    meetingDT = dt.datetime(today.year, today.month, today.day, meeting["hour"], meeting["minute"])
    print("The alarm will be set for", meeting["name"], "at", meetingDT)

    while meetingDT > dt.datetime.now():
        print("Your meeting will take place in", round((meetingDT - dt.datetime.now()).total_seconds()/60),"minutes...")
        time.sleep(60)

    ctypes.windll.user32.MessageBoxW(0, "\n\n\nPlease join your meeting: " + meeting["name"] + "\n\n\n", "==================Meeting Alarm==================", "MB_TOPMOST")
    time.sleep(60)
    
    while meetingDT < dt.datetime.now():
        ctypes.windll.user32.MessageBoxW(0, "\n\n\nPlease join your meeting: " + meeting["name"] + " you are running late.\n\n\n", "==================Meeting Alarm==================", "MB_TOPMOST")

except Exception as e:
    ctypes.windll.user32.MessageBoxW(0, "\n\n\nThere has been an error, please restart the alarm\n\n\n", "==================Meeting Alarm==================", "MB_TOPMOST")
    print (e)


