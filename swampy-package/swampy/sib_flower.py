# Flower excercise (4.2) from Week 0

# Name: Alex Lau

from sib_polygon import *

from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				
bob.delay = 0.005

# This is where you put code to move bob
def petal(t, r, angle):
	for i in range(2):
		arc(t, r, angle)
		lt(t, 180-angle)

def flower(t, n, r, angle):
	for i in range(n):
		petal(t, r, angle)
		lt(t, 360.0/n)

def move(t, length):
	pu(t)
	fd(t, length)
	pd(t)

move(bob, -100)
flower(bob, 7, 60.0, 60.0)

move(bob, 100)
flower(bob, 10, 40.0, 80.0)

move(bob, 100)
flower(bob, 20, 140.0, 20.0)

die(bob)

wait_for_user()					

