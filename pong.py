from sense_hat import SenseHat
sense = SenseHat()
import time
import random

white = [255,255,255]
red = [255, 0, 0]
pos_x = 4
x = random.randint(1,5)
y = random.randint(0,7)
xVelocity = 1
yVelocity = 1

def start(event):
  if event.action == 'pressed':
    start_Game()


def move_up(event):
  global pos_x
  if event.action == 'pressed' and pos_x>1:
    pos_x -=1

def move_down(event):
  global pos_x
  if event.action == 'pressed' and pos_x<6:
    pos_x +=1
  
sense.stick.direction_down = move_down
sense.stick.direction_up = move_up
sense.stick.direction_left = start

def draw_Pad():
  sense.set_pixel(0,pos_x,white)
  sense.set_pixel(0,pos_x +1,white)
  sense.set_pixel(0,pos_x -1,white)

def start_Game():
  global white
  global red
  global pos_x
  global x
  global y
  global xVelocity
  global yVelocity
  
  while True:
      time.sleep(.2)
      sense.clear()
      sense.set_pixel(y,x,red)
      draw_Pad()
      if x == 0:
        xVelocity = +1
        
      if x == 7:
        xVelocity = -1
        
      if y == 7:
        yVelocity = -1
       
      if y == 0:
        sense.clear()
        sense.show_message("GAME OVER",0.05)
        x = random.randint(1,5)
        y = random.randint(0,7)
        yVelocity = +1
        break
        
      if y == 1: 
        if x == pos_x or x == pos_x + 1 or x == pos_x - 1 or (x == pos_x + 2 and xVelocity == -1) or (x == pos_x - 2 and xVelocity == +1) :
          yVelocity = +1
          
      x = x + xVelocity
      y = y + yVelocity

