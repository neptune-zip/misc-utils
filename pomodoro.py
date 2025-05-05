import datetime as dt
import ctypes
import time

print("Pomodoro alarm by Kyle N - 5th May 2025\n\n\n\n")

try:
    pomodoro= {} 
    pomodoro["setLongBreakAfter3Cycles"] = True
    pomodoro["counter"] = 0  
    validated = False
    
    while (not validated):
        longBreakAnswer = input("Do you want a long break after 4 cycles? (Y/N): ").upper()
        validateSet = {"Y","N"}
        if longBreakAnswer not in validateSet:
            print("You did not enter 'Y' or 'N', please start again")
            continue
        elif longBreakAnswer == "N":
            pomodoro["setLongBreakAfter3Cycles"] = False

        
        try:
            pomodoro["workTime"] = int(input("How long (minutes) would you like to work: "))
            pomodoro["shortBreak"] = int(input("How long (minutes) would you like the short break: "))
            if pomodoro["setLongBreakAfter3Cycles"]:
                pomodoro["longBreak"] = int(input("How long (minutes) would you like the long break: "))
        except:
            print("You did not enter a number, please start again.\n\n")
            continue
        validated = True

    while True:
        pomodoro["counter"] += 1
        now = dt.datetime.now()
        breakTimeEnd = now #I hope this initialises the variable...
        
        workTimeEnd = now + dt.timedelta(0,0,0,0,pomodoro["workTime"])
                
        if pomodoro["setLongBreakAfter3Cycles"] == False or (pomodoro["setLongBreakAfter3Cycles"] and pomodoro["counter"]%4 != 0):
            breakTimeEnd = workTimeEnd + dt.timedelta(0,0,0,0,pomodoro["shortBreak"])
        
        elif pomodoro["setLongBreakAfter3Cycles"] and pomodoro["counter"]%4 == 0:
            breakTimeEnd = workTimeEnd + dt.timedelta(0,0,0,0,pomodoro["longBreak"])
        
        else:
            raise Exception("Time delta error occurred...")
        
        
        print("\n\nThe work time will end at ", workTimeEnd, "and the break time will end at ", breakTimeEnd,"this is cycle number",pomodoro["counter"],"\n\n")

        while workTimeEnd > dt.datetime.now():
            print("Your work time will end in", round((workTimeEnd - dt.datetime.now()).total_seconds()/60),"minutes...")
            time.sleep(60)

        ctypes.windll.user32.MessageBoxW(0, "\n\n\nWork time is finished!! Please take a break!\n\n\n", "==================Pomodoro Alarm==================", "MB_TOPMOST")
        
        while breakTimeEnd > dt.datetime.now():
            print("Your break time will end in", round((breakTimeEnd - dt.datetime.now()).total_seconds()/60),"minutes...")
            time.sleep(60)

        ctypes.windll.user32.MessageBoxW(0, "\n\n\nBreak time is finished!! Please get back to work!\n\n\n", "==================Pomodoro Alarm==================", "MB_TOPMOST")

except Exception as e:
    ctypes.windll.user32.MessageBoxW(0, "\n\n\nThere has been an error, please restart the alarm\n\n\n", "==================Pomodoro Alarm==================", "MB_TOPMOST")
    print (e)


