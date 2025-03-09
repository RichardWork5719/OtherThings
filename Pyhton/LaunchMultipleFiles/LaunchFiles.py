import subprocess # TODO: well ill basically put this on perma hold cuz i wanted to use some UI but ill honestly rather just not fuck with it THAT much else its basically finished
import pathlib
from pathlib import Path



content = ""
AppsToRun = []
fileToRead = "AppsToRun.txt"


def DewIt():
    try:
        content = open(fileToRead, 'r')
        content = content.read()
        content = content.split("\n")
        print(content)

        for app in content:
            subprocess.Popen(f'explorer "{Path(app)}"')


    except:
        content = open(fileToRead, 'w')
        content.write(""""R:\Apps or Games that arent programs\VSeeFace\VSeeFace.exe"\n"R:\Programs\Streamlabs OBS\Streamlabs OBS.exe"\n"R:\Programs\Chatterino StreamApp\Chatterino\chatterino.exe" """)
        #content = content.read()
        print(content)



DewIt()

# BTW dont forget TODO: pip install pyinstaller
# to get the installer that exports the python file into a single .exe