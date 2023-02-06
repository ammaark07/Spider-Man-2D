###########################################################################
# Title: Spiderman 2D
# Programmer:  Ammaar Khan
# Last modified:  01/29/2023
# Purpose: Create a 2D Spiderman Game!
###########################################################################

#imports
from tkinter import*
from math import *  
from time import *
from random import *


root = Tk()
screen = Canvas(root, width=1200, height=1000, background="skyblue")


def setInitialValues():
  #Setting all global variables
  global score, time, xSpeedWebs, ySpeedWebs, gameOver
  global xSpidey, ySpidey, xSpeedSpidey, ySpeedSpidey, x1Webs, y1Webs, x2Webs, y2Webs
  global webDrawing, spideyDrawing, barDrawing, road, startPlat, xMouse, yMouse, mouseDown
  global webRadius, swingTimeCount, swing, swingDirec, lasers, xSpeedLasers, xLasers, yLasers, laserNum, size 
  global intro, introScreen, introBack, introLogo, introLogo2 , instructionHeader, instructions, dodge, dodgeBox, scoreStatment
  global endText, restartText, timeDrawing, finalTime, finalTimeDrawing, yourScoreIs, endScreen, skylineDrawing
  global skyline, spideyPNG, spideyLogoPNG, drawWeb, twoPNG, controlsPNG, instructPNG, dodgePNG, gameOverPNG, restartPNG
  
  #True and False Statements
  gameOver = False
  drawWeb = False
  mouseDown = False
  swing = False
  introScreen = True

  #Misc. Variables
  intro = 0
  introLogo2 = 0
  timeDrawing = 0
  finalTime = 0
  finalTimeDrawing = 0
  swingTimeCount = 0
  swingDirec = 0
  
  endScreen = 0
  yourScoreIs = 0
  dodgeBox = 0
  endText = 0
  restartText = 0
  instructions = 0
  
  score = 0
  time = 0
  
  x1Webs = 0
  y1Webs = 0
  x2Webs = 0
  y2Webs = 0
  xSpeedWebs = 0
  ySpeedWebs = 0
  
  xSpidey = 50
  ySpidey = 150
  xSpeedSpidey = 0
  ySpeedSpidey = 0

  xMouse = 0
  yMouse = 0
  
  spideyDrawing = 0
  webDrawing = 0
  webRadius = 0
  barDrawing = 0
  

  #PNG Images
  spideyPNG = PhotoImage(file = "spidey (1).png")

  spideyLogoPNG = PhotoImage(file = "spideylogo2.png")

  twoPNG = PhotoImage(file = "2DYellow.png")

  controlsPNG = PhotoImage(file = "controls.png")

  instructPNG = PhotoImage(file = "instruct.png")

  dodgePNG = PhotoImage(file = "Dodge.png")

  gameOverPNG = PhotoImage(file = "gameOver.png")

  restartPNG = PhotoImage(file = "restart.png")

  skyline = PhotoImage(file = "new-york-city-skyline.png")


  #Background Elements
  road = screen.create_rectangle(0,950,1200,1000,fill="black")

  barDrawing = screen.create_rectangle(0,0,1200,30,fill="orange")

  startPlat = screen.create_rectangle(0,200,150,225,fill="grey")

  skylineDrawing = screen.create_image(600,600,image = skyline)


  
  #Lasers!
  laserNum = 5

  
  #laser positions
  xLasers = []
  yLasers = []
  
  #Speed of lasers
  xSpeedLasers = []
  
  #Length of lasers
  size = []
  
  #All lasers
  lasers = []  

  #Fill empty arrays with values
  for i in range( laserNum ):
    size.append(randint(45, 65))
    xLasers.append(1200) 
    yLasers.append(randint(32,949))
    xSpeedLasers.append(uniform(-15,-10))
    lasers.append ( 0 )  
  

#Draw objects
def drawObjects():
  global webDrawing, spideyDrawing, spideyPNG, lasers, xLasers, yLasers, introScreen, time, timeDrawing

  #tine/score counter
  time = time + 0.1
  time = round(time,2)
  print("time: ", time)

  #Time/Score displayed on-screen
  timeDrawing = screen.create_text(200,50, text = time, font = "Arial 25",fill = "white")
  scoreStatement = screen.create_text(100,50, text = "Score:", font = "Arial 25" ,fill = "white")


  #Webs and spiderman
  webDrawing = screen.create_line( x1Webs, y1Webs, x2Webs, y2Webs, width = 3, fill = "white")
  spideyDrawing = screen.create_image( xSpidey, ySpidey, image = spideyPNG)


  #lasers
  for i in range( laserNum ):
    
    lasers[i] = screen.create_line(xLasers[i], yLasers[i], xLasers[i]+size[i], yLasers[i], fill="red",width=5)

  
#Animate everything
def updateObjects():
  #xSpeedPacman doesn't need to be listed here because we're not changing its value in this procedure
  global x1Webs, y1Webs, x2Webs, y2Webs, xSpidey, ySpidey, xSpeed, ySpeed, swingTimeCount, swing, swingDirec, xLasers, xSpeedLasers, laser, gameOver, time

  #Animate lasers
  for i in range( laserNum ):
    
    #Set the speed of each laser
    xLasers[i] = xLasers[i] + xSpeedLasers[i]

    #Reset laser positions when they go offscreen
    if xLasers[i] <= 0:
      xLasers[i] = 1200
      yLasers[i] = randint(32,949)


    #Hitbox, ends game when a laser collides with spiderman
    elif xLasers[i] <= xSpidey + 25 and xLasers[i] >= xSpidey - 25:
     
      if yLasers[i] <= ySpidey + 50 and yLasers[i] >= ySpidey - 50:
        sleep(2)
        print("hit")

        #End the game
        gameOver = True

        #Reset spiderman and webs
        xSpidey = 50
        ySpidey = 150
        x2Webs = 50
        y2Webs = 150
        y1Webs = 150
        x1Webs = 50

        #Reset lasers
        for j in range(laserNum):
          xLasers[j] = 1200
          yLasers[j] = randint(32,949)
      
      else: #Keep playing
        pass
    
   

  
  if swing == True: #If the mouse has been clicked


    if swingDirec == 1: #Swinging to the right
  
      swingTimeCount = swingTimeCount + 1
  

      #Make spidey swing in a circlular fashion around the web pivot point, clockwise
      xSpidey = webRadius * cos(-0.1*swingTimeCount) + x1Webs  	
      ySpidey = webRadius * sin(-0.1*swingTimeCount) + y1Webs	   
  
      
      #spiderman is at the bottom of the web
      x2Webs = xSpidey
      y2Webs = ySpidey

      if ySpidey <= 30:  #If spiderman is about to go above the bar, change his swing direction
       swingDirec = 2

      if ySpidey >=1000:  #If spiderman is about to go below the screen, jolt him back up
        ySpidey = ySpidey - 500
        x2Webs = xSpidey
        y2Webs = ySpidey

      if xSpidey <= 0 or xSpidey >= 1200: #If spiderman is going to go horizontally offscreen, bring him back to the middle
        xSpidey = 600
        x2Webs = xSpidey
        y2Webs = ySpidey
  
  

    elif swingDirec == 2: #Swinging to the left
      swingTimeCount = swingTimeCount + 1
    
      #Make spidey swing in a circlular fashion around the web pivot point, counterclockwise
      xSpidey = webRadius * cos(0.1*swingTimeCount) + x1Webs  	
      ySpidey = webRadius * sin(0.1*swingTimeCount) + y1Webs	   
  
      #spiderman is at the bottom of the web
      x2Webs = xSpidey
      y2Webs = ySpidey

      if ySpidey <= 30: #If spiderman is about to go above the bar, change his swing direction
       swingDirec = 1

      if ySpidey >=1000: #If spiderman is about to go below the screen, jolt him back up
        ySpidey = ySpidey - 500
        x2Webs = xSpidey
        y2Webs = ySpidey

      if xSpidey <= 0 or xSpidey >= 1200: #If spiderman is going to go horizontally offscreen, bring him back to the middle
         xSpidey = 600
         x2Webs = xSpidey
         y2Webs = ySpidey
      
  #No swinging happening    
  elif swing == False:
    xSpidey = xSpidey + xSpeedSpidey
    ySpidey = ySpidey + ySpeedSpidey
    
  
  
def mouseClickHandler( event ):
  global xMouse, yMouse,ySpidey, xSpeedSpidey, ySpeedSpidey, x1Webs, y1Webs, x2Webs, y2Webs, mouseDown, xSpidey, webRadius, swing, swingDirec, swingTimeCount, introScreen, gameOver, webDrawing, finalTimeDrawing, yourScoreIs

  mouseDown = True  #The nouse has been clicked!

  
  if introScreen == True: #Delete the intro screen, move on to game
    
    #Reset spiderman position, delete score display, set intro as false
    screen.delete(finalTimeDrawing, yourScoreIs)
    xSpidey = 50
    ySpidey = 150
    introScreen = False

  if gameOver == True:  #Draw intro screen again, delete GAME OVER screen, and set gameOver as false
    screen.delete( endScreen,endText,restartText )
    gameOver = False
    introScreen = True
    
   
   #Restarts game using runGame code (line 397)
    while gameOver == False:  
    
      if introScreen == True:  #Draw the intro
    
        drawIntro()
        screen.update()
        sleep(0.03)
        screen.delete( introBack, introLogo, introLogo2, instructionHeader, instructions, dodge, dodgeBox )
  
      else:
        drawObjects()  #Draw game
    
        screen.update()
        sleep(0.03)
        screen.delete( spideyDrawing, webDrawing, timeDrawing)
    
        for i in range(laserNum):
          screen.delete(lasers[i])
    
        #This should adjust all the objects' positions and speeds
        updateObjects()  
    endGame()
  

  
  else: #Create web for spiderman to swing on
  
    xMouse = event.x
    yMouse = event.y
  
    if yMouse > 30:  #If the mouse didn't click the orange var
      drawWeb = False
  
    else:  #Orange bar clicked

      #Web pivot/latching point
      x1Webs = xMouse
      y1Webs = yMouse

      #Spiderman is at the bottom of the web
      x2Webs = xSpidey
      y2Webs = ySpidey

      #Finding the angle between spiderman and the web pivot point
      opposite = abs(y1Webs-y2Webs)
      adjacent = abs(x1Webs-x2Webs)
      angle = atan((opposite/adjacent))
      angle = degrees(angle)
      print(angle)
    
      #Check which quadrant the angle is in, find RAA
      if x2Webs > x1Webs: # spidey in front of web
        if y2Webs < y1Webs: #in front and below
          newAngle = 360 - angle
        else: # in front and above
          newAngle = angle 
      else: # spidey behind web
        if y2Webs > y1Webs: # behind and below
          newAngle = 180 + angle
        else: #behind and above
          newAngle = 180 - angle

      #Set swing timer to new angle divided by 5.625, as that gives the proper corresponding time value
      swingTimeCount = newAngle/5.625 

      #Find radius of web
      webRadius = sqrt(((x1Webs - xSpidey)**2)+((y1Webs - ySpidey)**2))

      #If the point clicked for the webs is to the right of spidey, swing right
      if x1Webs > xSpidey:
        swingDirec = 1
        swing = True
        
      #If the point clicked for the webs is to the right of spidey, swing right
      elif x1Webs < xSpidey:
        swingDirec = 2
        swing = True
    
    
      
      


def mouseReleaseHandler( event ):  #Activates after mouse click ends
  global mouseDown, swing, swingTimeCount

  #reset swing and mouseDown variables
  mouseDown = False
  swing = False

  


def drawIntro(): #Drawing intro
  global introBack, introLogo, introLogo2, instructionHeader, instructions, dodge, dodgeBox
  introBack = screen.create_rectangle(0,0,1200,1000, fill = "darkblue")
 
  introLogo = screen.create_image( 600, 250, image = spideyLogoPNG)

  introLogo2 = screen.create_image( 600, 430, image = twoPNG)
 
  instructionHeader = screen.create_image(600, 620, image = controlsPNG)
  
  instructions = screen.create_image(600, 760,image = instructPNG)
  
  dodgeBox = screen.create_rectangle(200,900,1000,959, fill="black")
  
  dodge = screen.create_image(600,932,image = dodgePNG)
  
  
  

def endGame():  #Draw GAME OVER screen
  global endScreen, endText, restartText, time, finalTime, finalTimeDrawing, yourScoreIs

  endScreen = screen.create_rectangle(0,0,1200,1000, fill = "darkblue")
 
  endText = screen.create_image(600,300,image = gameOverPNG)
 
  restartText = screen.create_image(600,550,image = restartPNG)
  
  finalTime = time
  
  yourScoreIs = screen.create_text(600,700,text="Your Score Is:", font = "Arial 40", fill="white")
  
  finalTimeDrawing = screen.create_text(600,800, text = finalTime, font = "Arial 40", fill="white")
  
  #reset score
  time = 0


def runGame():  
  setInitialValues()

  while gameOver == False:   #Repeats 100’s of times per second, whether the player is doing anything or not
    
    if introScreen == True:  #Draw intro
    
      drawIntro()
      screen.update()
      sleep(0.03)
      screen.delete( introBack, introLogo, introLogo2, instructionHeader, instructions, dodge, dodgeBox )

    else:
      drawObjects()  #Draw game
  
      screen.update()
      sleep(0.03)
      screen.delete( spideyDrawing, webDrawing, timeDrawing)
  
      for i in range(laserNum):
        screen.delete(lasers[i])
  
      #This should adjust all the objects' positions and speeds
      updateObjects()  
  
  #create intro screen

    

  
  endGame()
    
  

#At the bottom
root.after( 0, runGame )

screen.bind( "<Button-1>", mouseClickHandler )
screen.bind("<ButtonRelease-1>", mouseReleaseHandler)

screen.pack()
screen.focus_set()
root.mainloop()