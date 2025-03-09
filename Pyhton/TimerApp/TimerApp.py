
import os
import sys
import time
import winsound


def Stopwatch():
    os.system('cls')
    Input = input("Press [Enter] to start the stopwatch\n")
    os.system('cls')
    Start = time.perf_counter()
    Input = input("Timer started\nPress [Enter] to stop the stopwatch\n")
    Elapsed = time.perf_counter() - Start
    Input = input(f'Timer stopped with: {Elapsed:.03f}s')

def Alarm():
    repeat = True
    while repeat:
        try:
            winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
            time.sleep(1)
        except KeyboardInterrupt as keyInterrupt:
            print(keyInterrupt)
            repeat = False

def Countdown():
    #os.system('cls')
    repeat = True
    timer = 0
    os.system('cls')
    while repeat:
        try:
            Input1 = input("Input countdown time (in hours)\n-> ")
            os.system('cls')
            Input2 = input("Input countdown time (in minutes)\n-> ")
            os.system('cls')
            Input3 = input("Input countdown time (in seconds)\n-> ")
            # Input = input("Input countdown time\n================================================================================================================================================================\nmust be formatted like: \nnumberOfHours numberOfMinutes numberOfSeconds or numberOfHours:numberOfMinutes:numberOfSeconds \nseparate by either space ' ' or colon ':'\n\nand if you leave out a number or more it will leave out hours first, then minutes \nExample: '1 2 3' will be a timer for 1 hour 2 minutes and 3 seconds\nExample2: '1:3' will be a timer for 1 minute and 3 seconds\nExample3: '1:3:2' will be a timer for 1 hour 3 minutes and 2 seconds\nmake sure to use only one of the two separators when typing a timer number\n\nNo zeroes infront of integers\nlike: '01' '011' '0110101'\njust type:  '1' '11' '110101' insead\n================================================================================================================================================================\n-> ")

            Input1 = Input1.replace(" ", "")
            Input2 = Input2.replace(" ", "")
            Input3 = Input3.replace(" ", "")

            if Input1 == "" or Input1 == " ":
                Input1 = "0"
            if Input2 == "" or Input2 == " ":
                Input2 = "0"
            if Input3 == "" or Input3 == " ":
                Input3 = "0"

            hoursToMins = 0
            minutesToSecs = 0
            seconds = 0

            try:
                hoursToMins = (int(Input1) * 60)
            except:
                hours = 0

            try:
                minutesToSecs = (int(Input2) * 60)
            except:
                minutes = 0

            try:
                seconds = int(Input3)
            except:
                seconds = 0

            if hoursToMins != 0:
                minutesToSecs += (hoursToMins * 60)

            if minutesToSecs != 0:
                seconds += minutesToSecs

            timer = seconds
            seconds = 0
            repeat = False

        except Exception as e:
            print(e)

    os.system('cls')
    for x in range(timer, 0, -1):
        seconds = x % 60
        minutes = int(x / 60) % 60
        hours = int(x / 3600)
        # print(f"{hours:02}:{minutes:02}:{seconds:02}")
        sys.stdout.write(f"""\r{hours:02}:{minutes:02}:{seconds:02}""")
        time.sleep(1)

    print("\r=============Timer finished=============")
    print("Press Ctrl+C to silence the alarm")
    Alarm()


os.system('title Timer')
os.system('cls')

arg = ""

while arg == "":
    arg = input("Select your type of timer (stopwatch = [sw] / countdown timer = [cd]): ")

    if arg == "sw":
        Stopwatch()
        arg = ""

    elif arg == "cd":
        Countdown() # winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
        arg = ""

    elif arg == "quit" or arg == "stop" or arg == "exit" or arg == "close" or arg == "end":
        print("Closing app...")
        arg = " "

    else:
        print(f"Unknown command {arg}")
        arg = ""

    #winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
