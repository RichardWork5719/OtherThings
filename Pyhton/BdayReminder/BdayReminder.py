import os
import csv
import pathlib
import datetime

class Bday:
    def __init__(self, name, date):
        self.NAME = name
        self.DATE = date

    def BdayCheck(self):
        today = datetime.datetime.today().date() # get the current date
        today = str(today).split("-") # split the date into numbers
        today.reverse() # reverse the order suz for some reason its year-month-day so we convert it to day-month-year
        #print(today)

        bDayDate = ""
        if date.endswith('.'): # checking is i forgot to add the . dot at the end of a date
            bDayDate = self.DATE.removesuffix('.')
        else:
            bDayDate = self.DATE

        bDayDate = bDayDate.split(".") # split the date in the 2 numbers (day-month)

        if int(bDayDate[0]) < 10: # if the day or month are single digit then add a '0' infront of the number cuz the date numbers have it like that for fucks knows why
            bDayDate[0] = "0" + bDayDate[0]
        if int(bDayDate[1]) < 10:
            bDayDate[1] = "0" + bDayDate[1]
        #print(bDayDate)

        if bDayDate[0] == today[0] and bDayDate[1] == today[1]: # if the dates align then then return a True with a message
            print(f"Its {self.NAME}s birthday today!")
            return True
        else:
            return False


    def __str__(self):
        return f"Name: {'{:<50}'.format(self.NAME)}\t|\t{self.DATE}"


CGBdays = pathlib.Path("D:\Desktop\Crowbar Gang Bdays List.csv")

CGMembers = []
with open(CGBdays, 'r') as csvfile: # open the .csv file and read the data inside
    csvreader = csv.reader(csvfile) # use the csv formatter to read it
    for row in csvreader: # for each row in the data
        #print(row)
        for member in row: # for each tile in that row
            if len(member.split(" ")) > 1: # if the data in the tile is splitable
                info = member.split(" ") # split the data by spaces
                #print(f"info: {info}")
                name = ""
                date = ""
                if len(info) > 2: # if the name is multi-worded like Sarah marie
                    name = info[0:-1] # the name is everything except the last data
                    date = info[-1] # the last data is the date
                    fullName = ""
                    for namePart in name: # use a for loop to create the full name in a single string and not a list
                        fullName += namePart + " "
                    fullName = fullName.removesuffix(" ")
                    name = fullName # override the name with the proper fullName string
                else:
                    name = info[0] # grab the name which should be the first item in the list of data
                    date = info[-1] # grab the date which should be the last item in the list of data
                newBday = Bday(name, date) # create a class with the name and date
                CGMembers.append(newBday) # add the newly created class to the list of members

#print(CGMembers)
for CGMember in CGMembers:
    #print(CGMember)
    CGMember.BdayCheck()

BdayBoyz = []
for CGMember in CGMembers:
    #print(CGMember)
    if CGMember.BdayCheck():
        BdayBoyz.append(CGMember)

os.system('cls')
if len(BdayBoyz) > 0:
    for bdayBoy in BdayBoyz:
        #print(f"Its {bdayBoy.NAME}s bday - {bdayBoy.DATE}")
        stopper = input(f"Its {bdayBoy.NAME}s bday today -> {bdayBoy.DATE}")
else:
    exit()
