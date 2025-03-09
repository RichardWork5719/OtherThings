import os
import requests
from urllib.request import urlopen
# https://store.steampowered.com/search/?maxprice=free&supportedlang=english&specials=1&ndl=1 # this encludes an "english games" filter but i wanna use one that doesnt have that


def WriteToTxt(gameLinks):
    if DEBUG:
        print("Writing down new games...")
    with open(f"LastCheckedGames.txt", 'wb') as f:
        f.write(gameLinks)
    if DEBUG:
        print("Done")


DEBUG = False

url = "https://store.steampowered.com/search/?maxprice=free&specials=1&ndl=1"
htmll = requests.get(url)
# format the URL into the games that exist=========================================================================================================================================
startOfGamesList = b"<!-- List Items -->"
endOfGamesList = b"<!-- End List Items -->"
gamesSection = (htmll.content[htmll.content.find(startOfGamesList):htmll.content.find(endOfGamesList)])
gamesSection = gamesSection.split(b'<a href=')
gamesCount = len(gamesSection)
gameLinks = b''

if DEBUG:
    print()

for game in range(1, gamesCount):
    gameLink = gamesSection[game].split(b'"')[1]
    gameLinks += gameLink + b'\n'

    if DEBUG:
        print()
        print(gameLink)

gameLinks = gameLinks.removesuffix(b'\n')
# check is list of new games is the same as the other list of games=========================================================================================================================
sameGamesAsLastTime = False
try:
    if DEBUG:
        print("Checking list of games that were last checked...")
    with open(f"LastCheckedGames.txt", 'rb') as f:
        lastCheckedGames = f.read()
        if lastCheckedGames == gameLinks:
            sameGamesAsLastTime = True
            if DEBUG:
                print("Same games as last time")
        else:
            sameGamesAsLastTime = False
            if DEBUG:
                print("Different games from last time")
except Exception as e:
    if DEBUG:
        print(e)
        print("List of previously free games doesnt exist so creating a new one")
        WriteToTxt(gameLinks)
    sameGamesAsLastTime = False
# check which games are new on the list of free games and then print out the new ones======================================================================================================================
gamesNotInOldList = b''
if not sameGamesAsLastTime:
    with open(f"LastCheckedGames.txt", 'rb') as f:
        lastCheckedGames = f.read()
        lastCheckedGames = lastCheckedGames.splitlines()
        gameLinksButSplit = gameLinks.splitlines()
        for gameLinkk in gameLinksButSplit:
            sameGame = False
            for lastCheckedGame in lastCheckedGames:
                if gameLinkk == lastCheckedGame:
                    sameGame = True
            if not sameGame:
                gamesNotInOldList += gameLinkk + b'\n'
        gamesNotInOldList = gamesNotInOldList.removesuffix(b'\n')

    os.system('cls')
    print(f"New Free Games On Steam:\n{gamesNotInOldList.decode()}")
    os.system('pause > nul')

# overwrite the list with a new one if its differnt================================================================================================================================
if not sameGamesAsLastTime:
    WriteToTxt(gameLinks)
