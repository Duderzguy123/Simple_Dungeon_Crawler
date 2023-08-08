from cmu_graphics import *
import random
app.stepsPerSecond = 10
# Write your code here
# Not sure where to start?
# Check out README.md under "Files"



# Dungeon Crawler

#Room Class
class room:
  #Room Constructor
  def __init__(self):
      app.background = "dimGrey"
      self.portal = portal()
      self.isTreasure = False
      self.isBoss = False
      self.isMonster = False
      self.isMimic = False
      self.playerItems = []
      
  #Makes Room Treausre Room
  def treasureRoom(self):
    self.isTreasure = True
    
  #Makes Room Boss Room
  def bossRoom(self):
    self.isBoss = True
    
  #Makes Room Monster Room
  def monsterRoom(self):
    self.isMonster = True
    
  #Makes Room Mimic Room
  def mimicRoom(self):
    self.isMimic = True

  #checks to see what room type a room object is
  def checkRoom(self):
    if currentRoom.isMonster == True:
      monster.monsterBody.opacity = 100
      boss.bossBody.opacity = 0
      chest.chestBody.opacity = 0
      mimic.mimicBody.opacity = 0
        
    elif currentRoom.isTreasure == True:
      monster.monsterBody.opacity = 0
      boss.bossBody.opacity = 0
      chest.chestBody.opacity = 100
      mimic.mimicBody.opacity = 0
        
    elif currentRoom.isBoss == True:
      chest.chestBody.opacity = 0
      boss.bossBody.opacity = 100
      monster.monsterBody.opacity = 0
      mimic.mimicBody.opacity = 0
        
    elif currentRoom.isMimic == True:
      monster.monsterBody.opacity = 0
      boss.bossBody.opacity = 0
      chest.chestBody.opacity = 0
      mimic.mimicBody.opacity = 100
    
      
#Portal Object
class portal:
  def __init__(self):
    self.portal = Oval(320, 260, 25, 35, fill = 'purple')
    
#Player Object
class player:
  def __init__(self):
    self.playerBody = Circle(200, 200, 10, fill = "white")
    self.playerHealth = 200
    self.playerAttack = 20
    self.playerArmor = 0

  #player position reset after portal use
  def setMiddle(self):
    self.playerBody.centerX = 200
    self.playerBody.centerY = 200
  
        
#Monster Object
class monster:
    def __init__(self):
      self.monsterBody = Circle(50, 300, 15, fill = "red", opacity = 0)
      self.monsterHealth = 100
      self.monsterAttack = 40
      self.monsterHeal = 10
      
    #Monster position reset after portal use
    def monsterReset(self):
      self.monsterBody.centerX = 50
      self.monsterBody.centerY = 300
      
#Boss Object
class boss:
  def __init__(self):
    self.bossBody = Star(200, 350, 30, 5, fill = "indigo", opacity = 0)
    self.bossHealth = 200
    self.bossAttack = 80
    self.bossHeal = 30
    
#Boss position reset after portal use
  def bossReset(self):
    self.bossBody.centerX = 200
    self.bossBody.centerY = 350


#Chest Object
class chest:
  def __init__(self):
    self.chestBody = Rect(160, 40, 60, 50, fill ="saddleBrown", opacity = 0)
    
#Mimic Object
class mimic:
    def __init__(self):
        self.mimicBody = Rect(300, 40, 80, 50, fill ="saddleBrown", opacity = 0)
        self.mimicHealth = 50
        self.mimicAttack = 70
        self.mimicHeal = 10 
    
    
    
#Items class
class items:
  def __init__(self):
    self.weapons = ["stick", "club", "sword", "spear"]
    self.armor = ["leatherArmor", "chainMailArmor", "ironArmor", "diamondArmor"]
    

#Start Screen
class startScreen:
  def __init__(self):
      self.backScreen = Rect(0 , 0, 400, 400, fill = "white", opacity = 100)
      self.title = Label("Dungeon Crawler", 200, 100, size = 50, opacity = 100)
      self.startButton = Label("START", 200, 300, size = 40, opacity = 100)
      self.commands = Label("Movement = Arrow Keys     Move Player into Objects to Interact", 200, 380,opacity = 100)
  
    
#End Screen
class endScreen:
  def __init__(self):
    self.endScreen = Rect(0 , 0, 400, 400, fill = "black", opacity = 0)
    self.winMessage = Label("You Won! Thanks For Playing!", 200, 200, size = 20, opacity = 0, fill = "white")
    self.deathMessage = Label("You Died! Better Luck Next Time!", 200, 200, size = 20, opacity = 0, fill = "white")

#Room Objects Initilization

#Level 1
roomOne = room()
roomTwo = room()
roomTwo.treasureRoom()
roomThree = room()
roomThree.monsterRoom()
roomFour = room()
roomFour.bossRoom()

#Level 2
roomFive = room()
roomFive.monsterRoom()
roomSix = room()
roomSix.treasureRoom()
roomSeven = room()
roomSeven.monsterRoom()
roomEight = room()
roomEight.treasureRoom()
roomNine = room()
roomNine.mimicRoom()
roomTen = room()
roomTen.monsterRoom()
roomEleven = room()
roomEleven.monsterRoom()
roomTwelve = room()
roomTwelve.treasureRoom()
roomThirteen = room()
roomThirteen.bossRoom()

#Iteractable Objects
chest = chest()
monster = monster()
boss = boss()
mimic = mimic()

#Items list object
items = items()

#Player Object Initialization
player = player()

#Start Screen
startScreen = startScreen()

#End Screen
endScreen = endScreen()
#Preset Levels (lists of rooms)
level = [roomOne, roomTwo,
            roomThree, roomFour,roomFive, roomSix, roomSeven, 
            roomEight, roomNine, roomTen, 
            roomEleven, roomTwelve, roomThirteen]
index = 0
currentRoom = level[0]


#Player interactions with objects     
def interact():
      global currentRoom
      global index
      global level
      treasure()
      fight()
  
      if player.playerBody.hitsShape(currentRoom.portal.portal) == True:
        if index == len(level)-1:
          endScreen.endScreen.opacity = 100
          endScreen.winMessage.opacity = 100
        elif index < len(level)-1:
          index += 1
          currentRoom = level[index]
          player.setMiddle()
        boss.bossReset()
        monster.monsterReset()
      
        
       
        
        
        currentRoom.checkRoom()
#Chest function
def treasure():
  number = randrange(4)
  #Weapon Give
  if player.playerBody.hitsShape(chest.chestBody) == True and (chest.chestBody.opacity == 100):
    if items.weapons[number] == "spear":
      print("You got a spear! Attack increased by 50!")
      player.playerAttack += 50
    elif items.weapons[number] == "sword":
      print("You got a sword! Attack increased by 50!")
      player.playerAttack += 50
    elif items.weapons[number] == "stick":
      print("You got a stick! Attack increased by 1!")
      player.playerAttack += 1
    elif items.weapons[number] == "club":
      print("You got a club! Attack increased by 30!")
      player.playerAttack += 30
    #Armor Give
    if items.armor[number] == "leatherArmor":
      print("You got a set of Leather Armor! Defense Increased by 20!")
      player.playerArmor += 20
    elif items.armor[number] == "chainMailArmor":
      print("You got a set of Chain Mail Armor! Defense Increased by 40!")
      player.playerArmor += 40
    elif items.armor[number] == "ironArmor":
      print("You got a set of Iron Armor! Defense Increased by 60!")
      player.playerArmor += 60
    elif items.armor[number] == "diamondArmor":
      print("You got a set of Diamond Armor! Defense Increased by 80!")
      player.playerArmor += 80

    player.setMiddle()
    chest.chestBody.opacity = 0
    
#Player Movement
def onKeyPress(key):
    if key == "left":
      if player.playerBody.centerX > 0:
        player.playerBody.centerX -= 20
      
    elif key == "right":
      if player.playerBody.centerX < 400:
        player.playerBody.centerX += 20
      
    elif key == "down":
      if player.playerBody.centerY < 400:
        player.playerBody.centerY += 20
    
    elif key == "up":
      if player.playerBody.centerY > 0:
        player.playerBody.centerY -= 20

#Combat System Function
def fight():
    choice = ""
    
  
  #Boss Combat
    if player.playerBody.hitsShape(boss.bossBody) == True and (boss.bossBody.opacity == 100):
      player.playerHealth = 200
      boss.bossHealth = 200
      while player.playerHealth > 0 and boss.bossHealth > 0:
        print("Player Current Health: " + str(player.playerHealth))
        print("Boss Current Health: " + str(boss.bossHealth))
        print("Press Enter to Continue: ")
        print()
        choice = input("Choose an option: attack, heal: ")
        if choice == "attack":
          boss.bossHealth -= player.playerAttack 
          if boss.bossHealth <= 0:
            boss.bossReset()
            boss.bossBody.opacity = 0
        elif choice == "heal":
          player.playerHealth += 40
        number = randrange(1,3)

        if number == 1:
          boss.bossHealth += boss.bossHeal
          print("Boss Healed!")
        elif number == 2:
          if boss.bossAttack <= player.playerArmor:
            player.playerHealth -= 0
          else:
            player.playerHealth -= (boss.bossAttack - player.playerArmor)
          print("Boss Attacked!")

        if player.playerHealth <= 0:
          endScreen.backScreen.opacity = 100
          endScreen.deathMessage.opacity = 100
          
    #mimic combat
    player.playerHealth = 200
    mimic.mimicHealth = 50
    if player.playerBody.hitsShape(mimic.mimicBody) == True and (mimic.mimicBody.opacity == 100):
      while player.playerHealth > 0 and mimic.mimicHealth > 0:
        print("Player Current Health: " + str(player.playerHealth))
        print("Boss Current Health: " + str(mimic.mimicHealth))
        print("Press Enter to Continue: ")
        choice = input("Choose an option: attack or heal: ")
        if choice == "attack":
          mimic.mimicHealth -= player.playerAttack 
          if mimic.mimicHealth <= 0:
            mimic.mimicBody.opacity = 0
        elif choice == "heal":
          player.playerHealth += 40
        number = randrange(1,3)
        if number == 1:
          mimic.mimicHealth += mimic.mimicHeal
          print("Mimic Healed!")
        elif number == 2:
          if mimic.mimicAttack <= player.playerArmor:
            player.playerHealth -= 0
          else:
            player.playerHealth -= mimic.mimicAttack - player.playerArmor
          print("Mimic Attacked!")
        

        if player.playerHealth <= 0:
          endScreen.backScreen.opacity = 100
          endScreen.deathMessage.opacity = 100
          
    #Monster Combat
    player.playerHealth = 200
    monster.monsterHealth = 100
    if player.playerBody.hitsShape(monster.monsterBody) == True and (monster.monsterBody.opacity == 100):
      
      while player.playerHealth > 0 and monster.monsterHealth > 0:
        print("Player Current Health: " + str(player.playerHealth))
        print("Monster Current Health: " + str(monster.monsterHealth))
        print("Press Enter to Continue: ")
        choice = input("Choose an option: attack, heal: ")
        
        if choice == "attack":
          monster.monsterHealth -= player.playerAttack 
          if monster.monsterHealth <= 0:
            player.setMiddle()
            monster.monsterBody.opacity = 0
        elif choice == "heal":
          player.playerHealth += 40
          
        number = randrange(1,3)
        if number == 1:
          monster.monsterHealth += boss.bossHeal
          print("Monster Healed!")
        elif number == 2:
          if monster.monsterAttack <= player.playerArmor:
            player.playerHealth -= 0
          else:
            player.playerHealth -= monster.monsterAttack - player.playerArmor
          print("Monster Attacked!")
        
          
        if player.playerHealth <= 0:
          endScreen.backScreen.opacity = 100
          endScreen.deathMessage.opacity = 100
    
            
#To get out of the start screen
def onMousePress(mouseX, mouseY):
    if mouseX > 80 and mouseX < 280:
        if mouseY > 150 and mouseY < 350:
            startScreen.backScreen.opacity = 0
            startScreen.title.opacity = 0
            startScreen.startButton.opacity = 0
            startScreen.commands.opacity = 0
            
#Constantly running function that allows for enemy movements                       
def onStep():
  
  interact()
  if currentRoom.isBoss == True:    
    if boss.bossBody.centerX <= 310 and boss.bossBody.centerX >= 100:
      boss.bossBody.centerX += 20
      if boss.bossBody.centerX <=160:
        boss.bossBody.centerX += 10
        if boss.bossBody.centerX >=300:    
          boss.bossBody.centerX -= 10

  if currentRoom.isMonster == True:    
    if monster.monsterBody.centerY <= 350 and monster.monsterBody.centerY >= 200:
      monster.monsterBody.centerY -= 20
      if monster.monsterBody.centerY >=250:
        monster.monsterBody.centerY -= 10
        if monster.monsterBody.centerY <=240:    
          monster.monsterBody.centerY += 10

  
   
cmu_graphics.run()
