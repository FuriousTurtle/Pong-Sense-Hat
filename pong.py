from sense_hat import SenseHat

import time 

sense = SenseHat()

blue = [0,0,255]
red = [255,0,0]

x = 6
y = 4


pxHaut = 3

pxMilieu = 4

pxBas = 5

while True :
  time.sleep(0.5)
  sense.clear()
  x -= 1
  sense.set_pixel(x,y,red)
  if sense.stick.direction_up :
    sense.clear()
    pxHaut += 1
    pxMilieu += 1
    pxBas += 1
    sense.set_pixel(0,pxHaut,blue)
    sense.set_pixel(0,pxMilieu,blue)
    sense.set_pixel(0,pxBas,blue)
  else:
    sense.set_pixel(0,pxHaut,blue)
    sense.set_pixel(0,pxMilieu,blue)
    sense.set_pixel(0,pxBas,blue)

