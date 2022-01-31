from enum import Flag
import os, random
#Siena M Richey
#Jan 14, 2022
# Declare variables, print variables, print type of data, learn some operators
# learn some operators

# this symbol is for comments, means the computer will ignore
# I want to clear my terminal
os.system('cls')
# Program is Average of 3 tests

#Declare and Assign Values
test1=89
test2=78.5
test3=86

#to display things on the screen we use the function print
# print(type(test1), type(test2), type(Flag)) 

#declare sum to add test symbols for addition is +
Sum = test1 + test2 + test3 
print('The Sum of tests is', Sum)
#average we will use division ... /
Average= Sum/3 
print('The Average of tests is', Average)

print("Test1 =", test1, end=" ")
print("Test2", test2)
print("The Average of the 3 tests is", Average)