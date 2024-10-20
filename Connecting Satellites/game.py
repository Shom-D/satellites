import pgzrun
import random
import time

WIDTH, HEIGHT, TITLE= 1000,900,'Connecting Satellites'

satellites=[]
numsatellite = 9
lines=[]
nextsatellite= 0
starttime=0
endtime=0
totaltime=0

def createsatellites():
    global starttime
    for x in range(0,9):
        satellite = Actor('satellite')
        satellite.pos = (random.randint(100,WIDTH-100), random.randint(100,HEIGHT-100))
        satellites.append(satellite)
    starttime = time.time()


def update():
   pass

def draw():
    screen.clear()
    for x in satellites:
        x.draw()
    
    



pgzrun.go()

