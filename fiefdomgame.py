import os
import time
import random

#global variables
loop = True
screen = "login"
currentUsername = 'default'
tempName = {}

#initial screen clear
os.system("clear")

#header() should be called on every page
def header():
    print('''
|----------------------------------------------------|
|---------------UNNAMED FIFEDOM GAME-----------------|
|----------------------------------------------------|
    ''')

#the fifedom class holds variables that define a player's stats
class Fifedom:
    name = 'Default Fifedom'
    ruler = 'Unclaimed'
    home = False
    defenders = 25
    workers = 25
    location = 1

    #take the current fifedom and write it to the /fifes directory
    def write(self):
        fifeFile = 'fifes/' + self.name + '.txt'
        
        #this part creates a file if it isn't made yet        
        try:
            with open(fifeFile, 'x') as f:

                f.write(self.name + '\n')
                f.write(self.ruler + '\n')
                f.write(str(self.home) + '\n')
                f.write(str(self.defenders) + '\n')
                f.write(str(self.workers) + '\n')
                f.write(str(self.location) + '\n')
        except:
            pass

        #write the class variables down line by line in the text file
        try:
            with open(fifeFile, 'w') as f:
                f.write(self.name + '\n')
                f.write(self.ruler + '\n')
                f.write(str(self.home) + '\n')
                f.write(str(self.defenders) + '\n')
                f.write(str(self.workers) + '\n')
                f.write(str(self.location) + '\n')
        except:
            pass

    #read class variables line by line
    def read(self):
        fifeFile = 'fifes/' + self.name + '.txt'
        try:
            with open(fifeFile, 'r') as f:
                self.name = f.readline().strip()
                self.ruler = f.readline().strip()
                self.home = f.readline().strip()
                self.defenders = f.readline().strip()
        except:
            self.write()
            print('file read fail, creating new fife file for current user')
                    


#create some default objects that we'll write over later
attackFife = Fifedom()
userFife = Fifedom()

#this begins the main game loop
#------------------------------------------------------------------------------
while (loop):
    
    #The login page takes a username, puts it into memory, and sends you to the
    #stronghold page. It also contains a small intro snippet
    #TO DO:
    # - Add user authentication, preferably in a secure way
    if screen == "login":
        os.system("clear")
        header()
        print("\n\n")
        print('''
Welcome to the Unnamed Fifedom Game!

This is a python programming project and multiplayer war game based on the classic
BBS door games of the 80s and 90s. In much the same way, this system uses a central
server to host the game to multiple users, who access it using a terminal emulator.

See more info at github.com/Sheeves11/UnnamedFifedomGame
        ''')
        print('\n\n')
        
        username = input("Enter your username\n(Note that usernames are not validated at the moment): ")
        currentUsername = username
        
        #if "username.txt" does not exist, create it. The file only contains a name for now.
        try:
            usernameFile = username + ".txt"
            with open(usernameFile, 'x') as f:
                f.write(username)
               # print('WRITING NEW USER FILE')
        except:
            time.sleep(1)
 
        print('\n\n')
        print("Logging in as: " + username)

        time.sleep(2)
        screen = "stronghold"

#The stronghold screen is homebase for players. The page also writes the current username
#into the userFife object.
#
#Each player gets a "home" stronghold that can't be overrun. This page displays the stats
#for that stronghold.
#
#TO DO:
# - Flesh this out a little more. Make it prettier.
# - Add a list of owned Fifedoms that aren't the home stronghold
#------------------------------------------------------------------------------
    if screen == "stronghold":
        os.system("clear")

        header()
        print("\n\n")
        print(username + "'s Stronghold")
        print("\n\n\n")
        
        userFife.name = username
        userFife.read()
        userFife.ruler = username
        userFife.defenders = str(userFife.defenders)
        userFife.write()

        if userFife.home != 'True':
            userFife.home = 'True'
            userFife.write()

        print('On a hilltop overlooking endless rolling fields, you see the only home you have ever known.')
        print('\n\nThe Fifedom is home to ' + str(userFife.defenders) + ' highly skilled warriors, and dozens of loyal citizens.')
        print('\nDo not let them down')
        print('\n\n\n\n')
        print('''\


       _   |~  _             
      [_]--'--[_]
      |'|""'""|'|           
      | | /^\ | |
   ---|_|_|I|_|_|---
         /   \ 

                ''')

        print("Avalible Commands:")
        print('-------------------------------------')
        print('{1}: View Nearby Fifedoms')
        print('{2}: About')
        print('-------------------------------------')
        print('\n')
        command = input("Enter your command: ")
        
        if command == "1":
            screen = "attack"

        if command == 'defaults':
            screen = 'createDefaults'

        if command == '2':
            screen = 'about'


#This is the about page for the game. Keep it updated
#------------------------------------------------------------------------------
    if screen == "about":
        os.system("clear")

        header()
        print('\n\n\n\n\n\n\n\n\n')

        print('''
        
Intro:
        
Unnamed Fifedome Game is a python programming project by Mike Quain (mquain@uark.edu)
The goal was to take on a project that was big enough to be challenging, but small enough to stay interesting.
This game looks simple, but it taught me the basics of reading and writing to a database, data persistance, and multi-user tools.

How to play:

Your goal is to control as many fifedoms as you can manage without spreading your army too thin and leaving yourself open to attack!
Your home stronghold will never fall, but any conquered fifedoms can be taken by opposing players. Make sure you can defend the
territory you claim!

Your Fifedom consists of soldiers and workers. The workers earn income and the soldiers both fight and defend your fifedoms.
Each worker produces 1 coin per hour. These coins will be used to purchace various upgrades and to recruit new fighters.

Additional Info is avalible at github.com/Sheeves11/UntitledFifedomGame

        ''')

        print('\n\n\n\n\n\n\n\n\n\n')
        print("Avalible Commands:")
        print('-------------------------------------')
        print('{1}: Return to Stronghold')
        print('-------------------------------------')
        print('\n')
        command = input("Enter your command: ")
        
        if command == "1":
            screen = "stronghold"

#The attack page contains a list of fifedoms generated from the /fifes directory
#
#To Do
# - add some sort of "next page" function so that the printout won't scroll
#   off the page as more players join.
# - add some sort of sorting on the list. 
#-------------------------------------------------------------------------------
    if screen == "attack":
        os.system("clear")
        
        header()
        
        print("\n")
        print("Nearby Fiefdoms: ")
        print("-------------------------------------------------------")
        print('\n')
        
        for filename in os.listdir('fifes'):
            with open(os.path.join('fifes', filename), 'r') as f:
                
                tempName = filename[:-4]
                tempName = Fifedom()
                tempName.name = filename[:-4]
                tempName.read()
                
                homeStatus = " "

                if tempName.home == "True":
                    homeStatus = "Home Stronghold"

                print ('Fifedom: ' + tempName.name + ' || Ruled by: ' + tempName.ruler)
                print ('Number of Warriors: ' + tempName.defenders + ' || ' + homeStatus)
                print ('\n')            

        print("Avalible Commands:")
        print('-------------------------------------')
        print('{1}: Return to stronghold')
        print('{Stronghold Name}: View Fifedom Details') 
        print('-------------------------------------')
        print('\n')
        command = input("Enter your command: ")
        
        if str(command) == '1':
            screen = "stronghold"
        
        if str(command) != '1':
            #search for file to open. If there, initialize it and load data
            #then, switch to a details screen

            fileFife = 'fifes/' + command + '.txt'
            print (fileFife + 'loading is happening')
            try:
                with open(fileFife, 'r') as f:
#                    print ('testing the file open: ')
#                    print (f.readline().strip())
                    attackFife.name = f.readline().strip()
#                    attackFife.ruler = f.readline().strip()

                    attackFife.read()
                    
                    if str(attackFife.ruler) == str(userFife.ruler):
                        screen = 'homeDetails'
                    
                    if str(attackFife.ruler) != str(userFife.ruler):
                        screen = "details"

            except:
                print ('the file open broke')

        os.system('clear')

#The homeDetails page gets called when a user tries to view their own Fifedom
#From this page, they'll be able to add and withdraw troops, make upgrades,
#etc
#
#To Do
# - make it prettier
# - add some sort of upgrade system for defenses
#------------------------------------------------------------------------------

    if screen == "homeDetails":
        os.system("clear") 
        header()
        
        print("\n\n")
        print('Now viewing the Fifedome of ' + attackFife.name)
        print('You rule this fifedom')
              
        time.sleep(2)
        print('\n\nStatus Report:')
        time.sleep(1)
        print(attackFife.name + ' has ' + attackFife.defenders + ' fighters.')
        time.sleep(3)

        print("\n\n\n\n\n\n\n\n\n")

        print("Avalible Commands:")
        print('-------------------------------------')
        print('{1}: Return to stronghold')
        print('{2}: View nearby fifedoms')
        print('{3}: Deploy or withdraw forces')
        print('-------------------------------------')
        print('\n')
        command = input("Enter your command: ")

        if command == "1":
            screen = "stronghold"

        if command == "2":
            screen = "attack"

        if command == "3":
            screen = 'deploy'

#The deploy screen allows players to deploy defenders to a Fifedom that they 
#currently control.
#
#To Do
# - add a "withdraw" page for pulling troops out of a Fifedom
# - verify that the player has the troops avalible for deployment
# - prevent negative numbers
#------------------------------------------------------------------------------
    if screen == 'deploy':
        os.system("clear")
        
        header()
        
        print("\n\n")
        print('Now viewing the Fifedome of ' + attackFife.name)
        time.sleep(1)
        print('\n\nStatus Report:')
        time.sleep(1)
        print(attackFife.name + ' has ' + attackFife.defenders + ' fighters.')
        time.sleep(1)
        print('You have ' + str(userFife.defenders) + ' ready to deploy.\n\n')
        deployNum = input('Enter the number of soldiers you would like to deploy: ')
        time.sleep(1)
        print('Deploying ' + str(deployNum) + ' soldiers to ' + str(attackFife.name))
        
        attackFife.defenders = str(int(attackFife.defenders) + int(deployNum))
        attackFife.write()
        attackFife.read()

        userFife.defenders = str(int(userFife.defenders) - int(deployNum))
        userFife.write()
        attackFife.read()

        print("\n\n\n\n\n\n\n\n\n")

        print("Avalible Commands:")
        print('-------------------------------------')
        print('{1}: Return to stronghold')
        print('-------------------------------------')
        print('\n')
        command = input("Enter your command: ")
        

        if command == "1":
            screen = "stronghold"


#This is the details page for enemy fifedoms
#
#To Do
# - Make it prettier
# - In the future, add a way to obscure exact numbers?
# - Add ability to attempt spying to gain info on defenses and upgrades
#------------------------------------------------------------------------------
    if screen == "details":
        os.system("clear")  
        header()
        
        print("\n\n")
        print('Now viewing the Fifedome of ' + attackFife.name)
        print('This Fifedome is ruled by ' + attackFife.ruler)
        time.sleep(2)
        print('\n\nYour scouts return early in the morning, bringing reports of the enemy Fifedom.')
        time.sleep(1)
        print(attackFife.name + ' looks to have ' + attackFife.defenders + ' fighters.')
        time.sleep(3)
        
        print("\n\n\n\n\n\n\n\n\n")
        
        print("Avalible Commands:")
        print('-------------------------------------')
        print('{1}: Return to stronghold')
        print('{2}: View nearby fifedoms')
        print('{3}: Attack')
        print('-------------------------------------')
        print('\n')
        
        command = input("Enter your command: ")
        
        if command == "1":
            screen = "stronghold"

        if command == "2":
            screen = "attack"

        if command == "3":
            screen = 'battle'


#The "battle" page simulates a battle between two fifedoms. This is currently the most
#complicated page and could use some cleaning up.
#
#To Do
# - add a better system for determining winners and casualties. The current system
#   is almost entirely random, which is bad. 
# - make it prettier
# 
#------------------------------------------------------------------------------
    if screen == "battle":
        os.system("clear")
        header()
        
        print("\n\n")
        print('This battle is between ' + attackFife.name + ' and ' + userFife.name)
        
        print('\n\nSimulating Battle...\n\n')
        if attackFife.home == 'True':
            print('You are unable to claim a player\'s home stronghold')
            time.sleep(3)
            screen = 'stronghold'
        
        if attackFife.home == 'False':
            
            #battle logic time!
            
            #assign some temp variables
            playerWins = True
            
            print('\n\n\n\n\nThe two great fifedoms of ' + userFife.name + ' and ' + attackFife.name + ' prepare for battle!')
            time.sleep(2)

            print('\n\n' + userFife.name + ' fires the first volley of arrows, catching the defenders unaware.')
            time.sleep(1)
            print('\n\n...\n\n')
            time.sleep(1)

            casualties = 1
            maxCasualties = int(attackFife.defenders)
            casualties = random.randint(0, maxCasualties)


            userCasualties = 1
            userCasualties = random.randint(0, int(userFife.defenders))
           


            #make sure that the fife has at least one guy left
            if int(attackFife.defenders) <= 0:
                attackFife.defenders = 1
            
            attackFife.defenders = int(attackFife.defenders) - casualties
            
            #make sure they have a guy left
            if int(attackFife.defenders) <= 0:
                attackFife.defenders = 1

            attackFife.write()

            print('\n\n' + attackFife.name + ' suffers ' + str(casualties) + ' casulaties.')
            
            time.sleep(2)
            print('\n\n' + 'Stunned by your attack, the enemy charges')
            time.sleep(1)
            print('\n\n...\n\n')
            time.sleep(1)
            print('You suffer ' + str(userCasualties) + ' casualties')

            userFife.defenders = int(userFife.defenders) - userCasualties

            if int(attackFife.defenders) <= 0:
                userFife.defenders = 1

            userFife.write()





            if (int(attackFife.defenders) >= int(userFife.defenders)):
                playerWins = False


            if playerWins == True:
                #this happens if the user wins the fight            
                attackFife.ruler = userFife.name
                attackFife.write()

                print(userFife.name + ' is the winner!')
                time.sleep(1)
                print('\n----------------------------\n')
                print('Crushed by their loss, some of ' + attackFife.name + " \'s fighters join you.")
                
                defectors = 1
                defectors = int(attackFife.defenders) - random.randint(0, int(attackFife.defenders))
                attackFife.defenders = int(attackFife.defenders) - defectors
                attackFife.write()

                userFife.defenders = int(userFife.defenders) + defectors


                print('You gain ' + str(defectors) + ' somewhat loyal soldiers')

            
            if playerWins == False:
                #this happens if the player loses
                
                print(userFife.name + ' has been defeted')


            print("\n\n\n\n\n\n\n\n\n")
            print("Type leave to return to your stronghold: ")
            command = input("Enter your command: ")

            if command == "leave":
                screen = "stronghold"

            if command == "attack":
                screen = "attack"


#This is a "secret" page that you can use to create default fifedoms
#to seed your installation with land that can be taken. 
#
#It should be taken out if you ever open this game up to many players
#----------------------------------------------------------------------------------
    if screen == "createDefaults":

        os.system("clear")
        print('Seeding the world with default Fifedoms')
            
        names = ['Razor Hills', 'Forest of Fado', 'Emerald Cove', 'Stormgrove', 'Aegirs Hall', 'Ashen Grove', 'Bellhollow']
        for x in names:
            currentFife = Fifedom()
            currentFife.name = x
            currentFife.defenders = random.randint(10, 50)
            currentFife.write()

        time.sleep(2)
        print('Seeding Complete')

        screen = input("Enter your command: ")