# -*- coding: utf-8 -*-
##	THESE PROGRAMS ALLOW YOU TO CALCULATE
##	THE ENERGY OF A LIQUID, PARTICULE
##	AND MAYBE SOME OTHERS THINGS NOT CODED YET
##LICENSE : DO WHAT THE FUCK YOU WANT

## ./particle.py argv1 argv2 --> argv1: speed particle && argv2: particle's mass

import sys,math

args=len(sys.argv)
if args != 3:
	print("There's isn't enough arguments.\
	\nYou have to give exactly two arguments.\n\n\
	The first argument is the speed of the particle\n\
	And the second argument is the mass of the particle.\
	\nExiting...")
	sys.exit()
	pass

def lorentzian_factor(v, c):
	y=1/(((1-v*2)/(c*2))*0.5)
	return float(y)
	pass

def impulsion(y,m,v):
	p=y*m*v
	return float(p)
	pass

def energy_computing(m, c, p):
	m=math.pow(m, 2)
	cc=math.pow(c, 4)
	pp=math.pow(p, 2)
	c=math.pow(c, 2)
	EE=((m*cc)+pp*c)
	EE=float(EE)
	return EE
	pass

v=float(sys.argv[1]) #v is the speed of the particle
m=float(sys.argv[2]) #mass of the particle
c=float(299792458) #Fiat lux!
y=lorentzian_factor(v,c)
y=float(y)
print("The lorentzian factor is : " + str(y))
p=impulsion(y,m,v)
print("The impulsion is : " + str(p))
energy=energy_computing(m,c,p)
print("E²=" + str(energy) + "")
sys.exit()
