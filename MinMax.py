"""Autumn Capasso
//UMUC 300 SDEV
//October 23, 2019
//LAB 1 Max Min Program
"""


#This program will find the min and max of 5 integers


#Greeting
print('Welcome to the Max & Min Python Program')



#taking in input 1
num1 = int(input('Please enter first integer: '))

#taking in input 2
num2 = int(input('Please enter second integer '))

#taking in input 3
num3 = int(input('Please enter first integer '))

#taking in input 4
num4 = int(input ('Please enter first integer '))

#taking in input 5
num5 = int(input(' Please enter fifth integer'))



#min
minValue = min(num1, num2, num3, num4, num5)


#max
maxValue = max(num1, num2, num3, num4, num5)

print('The Maximum of all five integers is ' , maxValue)
print('The Minimum of all five integers is ', minValue)
print('Thank you for trying to MinMax program')