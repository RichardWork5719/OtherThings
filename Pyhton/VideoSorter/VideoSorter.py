
import os
import time
import shutil
import pathlib
import datetime
#from pathlib import Path

#os.chdir("D:\Desktop\ContentWarningGameplayRecordings")

'''
readFile = "StuffForTheAppToWork.txt"
readFilePath = ""
with open(readFile, "rb") as f:
    readFilePath = f.read().decode()

readFilePath = readFilePath.splitlines()
'''

DEBUG = False

def MoveFilesFromDesktop(path="D:\Desktop"):
    print("Moving all files starting with 'content_warning_' to the same location as this .exe...")
    desktopLoc = pathlib.Path(path)
    files = list(desktopLoc.rglob("*"))
    for file in files:
        try:
            if DEBUG:
                print(file)
                print(file.name)
            if file.name.startswith("content_warning_"):
                if DEBUG:
                    print(f"Moved file: {file.name} to {os.getcwd()}")
                shutil.move(file, os.getcwd())
                #os.chdir(file, os.getcwd())
                #os.rename(file, "REEEEEEEEEEEE.webm")

        except Exception as e:
            print(e)

    print("Done")

def RenameFilesWithCreationDate(Path=os.getcwd()):
    print("Renaming everything")
    location = pathlib.Path(Path)

    files = list(location.rglob("*"))

    #DateTimeStamp = None #  = None
    #dateStamp = None
    #timeStamp = None

    for file in files:
        try:
            if DEBUG:
                print(file)
            if file.name.startswith("content_warning_"):
                DateTimeStamp = datetime.datetime.fromtimestamp(os.path.getctime(file))
                dateStamp = DateTimeStamp.date()
                if DEBUG:
                    print(dateStamp)
                timeStamp = DateTimeStamp.time()
                if DEBUG:
                    print(timeStamp)
                    print(f"{dateStamp}={timeStamp.hour}-{timeStamp.minute}-{timeStamp.second}=GameClip")
                if DEBUG:
                    pass
                newFileName = (os.path.join(str(file).removesuffix(file.name), f"{dateStamp}={timeStamp.hour}-{timeStamp.minute}-{timeStamp.second}=GameClip{timeStamp.microsecond}"))
                print(os.path.join(str(file).removesuffix(file.name), f"{dateStamp}={timeStamp.hour}-{timeStamp.minute}-{timeStamp.second}=GameClip{timeStamp.microsecond}"))
                os.rename(file, os.path.join(str(file).removesuffix(file.name), f"{dateStamp}={timeStamp.hour}-{timeStamp.minute}-{timeStamp.second}=GameClip{timeStamp.microsecond}.{str(os.path.basename(file)).split('.')[-1]}"))
                #del DateTimeStamp
                #del datetime
                #del timeStamp


        except Exception as e:
            print(e)

    print("Finished")



MoveFilesFromDesktop()
#RenameFilesWithCreationDate("D:\Desktop\ContentWarningGameplayRecordings")
RenameFilesWithCreationDate()


'''
location = pathlib.Path("D:\Desktop\ContentWarningGameplayRecordings")# os.getcwd()) # "D:\Desktop\ContentWarningGameplayRecordings"

files = list(location.rglob("*"))

for file in files:
    try:
        print(file)
        #print(os.stat(file).st_ctime)
        timeStr = "created: %s" % time.ctime(os.path.getctime(file))
        print(timeStr) # "created: %s" % time.ctime(os.path.getctime(file)))
        #fortmattedTime = timeStr.removeprefix("created: ")
        #fortmattedTime = fortmattedTime.split(" ")
        DateTimeStamp = datetime.datetime.fromtimestamp(os.path.getctime(file))
        dateStamp = DateTimeStamp.date() # datetime.date.fromtimestamp(os.path.getctime(file)) # (fortmattedTime[1])
        print(dateStamp)
        timeStamp = DateTimeStamp.time() # datetime.datetime.fromtimestamp(os.path.getctime(file))  # (fortmattedTime[1])
        print(timeStamp) # timeStamp.hour, timeStamp.minute, timeStamp.second)
        print(f"{dateStamp}={timeStamp.hour}-{timeStamp.minute}-{timeStamp.second}=GameClip")
        #if file.name.startswith("content_warning_"):
            #pass
            #file.name = f"{dateStamp}={timeStamp.hour}-{timeStamp.minute}-{timeStamp.second}=GameClip"
            #file.rename(f"{dateStamp}={timeStamp.hour}-{timeStamp.minute}-{timeStamp.second}=GameClip")


    except Exception as e:
        print(e)

'''
