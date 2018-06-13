#!/usr/bin/python2
from time import sleep

#Taking a number as an input from the user
input=raw_input("Enter a number ")

#Type casting the number to integer
number=int(input)

#Checking whether a number is positive or negative 
if number<0:
	print "Number is negative"
elif number==0:
	print "Number is 0"
else:  
	print "Number is positive"


