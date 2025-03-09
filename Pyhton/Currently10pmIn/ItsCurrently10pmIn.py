import os
import math
import time
import random
import datetime
from urllib.request import urlopen


start = time.perf_counter()
elapsed = None


def ItsGonnaBe10pmIn(currentTimetime, particularHourWereLookingFor):
    tenPMcountdown = str(currentTimetime.time())
    tenPMcountdown = tenPMcountdown.split(":")

    #print(tenPMcountdown)

    tenPMcountdownHolder = []
    for tUnit in tenPMcountdown:
        tenPMcountdownHolder.append(int(tUnit.split(".")[0]))

    tenPMcountdown = tenPMcountdownHolder
    #print(tenPMcountdown)

    minutes = tenPMcountdown[0] * 60
    seconds = (minutes * 60) + (tenPMcountdown[1] * 60) + (tenPMcountdown[2])

    #print(f"minutes: {minutes}   seconds: {seconds}")

    minutes2 = int(particularHourWereLookingFor) * 60
    seconds2 = (minutes2 * 60)

    #print(f"minutes2: {minutes2}   seconds2: {seconds2}")

    past10pm = False

    tenPMcountdown = seconds2 - seconds

    if tenPMcountdown < 0:
        past10pm = True
        tenPMcountdown = -tenPMcountdown

    #print((((tenPMcountdown) / 60)) / 60)

    secondsLeft = float(tenPMcountdown)
    seconds3 = int(secondsLeft % 60)
    minutes3 = int(secondsLeft / 60) % 60
    hours3 = int(secondsLeft / 3600)

    if past10pm:
        return f"-{hours3:02}:{minutes3:02}:{seconds3:02}"
    else:
        return f"{hours3:02}:{minutes3:02}:{seconds3:02}"


class TIMEZONE:
    def __init__(self, path, CityName, time):
        self.PATH = path
        self.CITYNAME = CityName
        self.TIME = time
        #print(f"Created timezone: {self.PATH} | Time: {self.TIME}")

    def __str__(self):
        return f'''Timezone: {'{:<50}'.format(self.PATH)}\t|\t{self.TIME}'''


DEBUG = False
LOOP = False
CLEAR = False

particularHourInTheDay = "22"

url = "https://www.timeanddate.com/worldclock/full.html" # "https://www.timeanddate.com/worldclock/" # ah so it looks like timeanddate.com blocked my IP cuz they want me to pay to have access...niggers

timerName = "10pmUseTimer.txt"
currentDir = os.getcwd()
filePath = os.path.join(currentDir, timerName)

usageTime = 0

try:
    with open(filePath, "rb") as f:
        usageTime = f.read().decode() # .split(" ")[0] # keep that .split in if im gonna add timestamps of when it was last used else IDK just leave it
        if DEBUG:
            print(usageTime)

except Exception as e:
    if DEBUG:
        print(e)

arg = " "
while arg == " ":
    htmll = urlopen(url).read()
    htmll = str(htmll)

    htmll = htmll.replace("</a>", " ") #
    htmll = htmll.replace("</span></td>", " ")
    htmll = htmll.replace("</td></tr><tr><td>", " ")
    htmll = htmll.replace('''<a href="/worldclock/''', "\n") # this is the line that separates the time of one city to the new "path" of the next city
    htmll = htmll.replace('''</td><td>''', " ")

    htmll = htmll.splitlines()

    TimezonesList = []

    for line in htmll:
        line = line.replace('''">''', " ") # this is the new line that separates the "path" from the actual name and time of a city
        line = line.split(" ")
        line = [line[0], line[1], line[-2]]
        newTimezone = TIMEZONE(line[0], line[1], line[2])
        TimezonesList.append(newTimezone)
        #print(line)

    TenPMtzList = []

    for timeZ in TimezonesList:
        if str(timeZ.TIME).startswith(particularHourInTheDay):
            TenPMtzList.append(timeZ)
        #print(timeZ)

    for tenPMtz in TenPMtzList:
        if DEBUG:
            print(tenPMtz)
        else:
            pass

    if DEBUG:
        print()

    randomTenPMtz = TenPMtzList[random.randrange(0, len(TenPMtzList))]

    PathName = str(randomTenPMtz.PATH).split('/')
    formattedPathName = [] # formatting the country and city names so thetre capitalised
    for name in PathName:
        name = name.capitalize()
        formattedPathName.append(name)

    finalFormat = ""
    for formatName in formattedPathName:
        finalFormat += formatName + "/"

    finalFormat = finalFormat.removesuffix("/")

    randomTenPMtz.PATH = finalFormat # yup all that just for capitalised text

    currentTime = datetime.datetime.now() # and now for the small things that sparrow wants me to add as QoL stuff

    #usageTimeInDays = math.floor((math.floor(float(usageTime) / 3600)) / 24) # nah fuckit im not adding days cuz thats too much math for midnight me
    #usageTimeInHours = math.floor(float(usageTime) / 3600) # aight now time to format the usage timer to make it readable for sparrow
    #usageTimeInMinutes = math.floor(float(usageTime) / 60)
    #usageTimeInSeconds = float(usageTime) - (usageTimeInMinutes * 60) - (usageTimeInHours * 3600)
    x = float(usageTime)
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    days = 0
    if hours > 24:
        days = int(hours/24)
    # print(f"{hours:02}:{minutes:02}:{seconds:02}")
    #sys.stdout.write(f"""\r{hours:02}:{minutes:02}:{seconds:02}""")

    formattedUsageTime = f""
    if days != 0:
        formattedUsageTime = f"   {days:03}:{hours:02}:{minutes:02}:{seconds:.02f}"
    else:
        formattedUsageTime = f"   {hours:02}:{minutes:02}:{seconds:.02f}"

    tenPMcountdown = ItsGonnaBe10pmIn(currentTime, particularHourInTheDay)

    print(f"It's currently {randomTenPMtz.TIME} in {randomTenPMtz.PATH}")
    print(f"{str(currentTime).split('.')[0].replace(' ', '  ').rjust(235)}")
    if tenPMcountdown.startswith("-"):
        print(f"It was 10pm:   {tenPMcountdown}s ago".rjust(235))
    else:
        print(f"It will be 10pm in:   {tenPMcountdown}s".rjust(235))
    print(f"App usage time:{formattedUsageTime}s".rjust(235))



    arg = input()
    if arg.lower() == "debug":
        DEBUG = not DEBUG
        arg = " "
    elif arg.lower() == "loop" or arg.lower() == "repeat":
        LOOP = not LOOP
        arg = " "
    elif arg.lower() == "clear" or arg.lower() == "clean":
        CLEAR = not CLEAR
        arg = " "

    if CLEAR:
        os.system('cls')

    if LOOP:
        if arg.lower() == "quit" or arg.lower() == "exit" or arg.lower() == "close" or arg.lower() == "stop":
            arg = ""
        else:
            arg = " "

    elapsed = float(time.perf_counter() - start) + float(usageTime)
    #print(f'finished in:{elapsed:.02f}s')
    with open(filePath, "wb") as f:
        f.write(f"{elapsed:.02f}".encode())
        usageTime = f"{elapsed:.02f}"

    start = time.perf_counter()

print(f'Total usage time:{elapsed:.02f}s')