#characterical Types(CHAR - STRING)
#--------------------------------------------

#For single line comment

"""
For
Multiple
Lines
"""

print("Hello!") #Hello

#empty string 
print("") #

#blank
print(" ") # 

# sum of two string and blank
print("Hello" + " " + "World") #Hello World

#Actually string is sum of char arrays.
print("H" "E" "L" "L" "O") #HELLO
print("H" " I") #H I

print("C" * 6 + "H" * 2 + "A" "R") #CCCCCCHHAR

#Errors

# print("E" * "E") #TypeError: can't multiply sequence by non-int of type 'str'
# print("S" * 2.5) #TypeError: can't multiply sequence by non-int of type 'float'

#using the reverse slash "\""
print("Python is \"good\" beginning.") #Python is "good" beginning.

#new line "\n" it should write without blanck with new line if you don't want black character. 
print("Data\nScience") #Data
                       #Science

#four unit blank character with "\t" 
print("Data\tScience") #Data    Science


