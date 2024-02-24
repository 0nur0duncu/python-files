# File Input-Output
# "r" -> read
# "a" -> append
# "w" -> write
# "X" -> create
# "t" -> text
# "b" -> binary
#-----------------------------
# / or \\ define the path

try:
    w = open("new.txt","w")
    w.write("Hello World")
except IOError:
    print("FileeIO error")
finally:
    w.close()

#or second alternative
#this command include close() function
with open("new.txt","w") as f:
    f.write("Hello World \nHello thisUniverse \nHello otherUniverse")

#read() all of lines
lines1 = open("new.txt","r") #or lines = open("new.txt")
print(lines1.readlines()) #['Hello World \n', 'Hello thisUniverse \n', 'Hello otherUniverse']
print(type(lines1.read())) #<class 'str'>
print(lines1.read()) #empty line because cursor still end of the lines.
lines1.seek(0) #cursor in starting #0. byte each character one byte
print(lines1.read()) #again full lines
print(lines1.tell()) #54 include the \ and n characters
lines1.close()

#readline() line by line
lines2 = open("new.txt","r") #or lines = open("new.txt") 
print(lines2.readline())
print(lines2.readline())
print(lines2.tell()) #35
lines2.seek(10) #
print(lines2.tell()) #10
lines2.close()

with open("new.txt","r+") as f:
    old_data = f.read()
    f.seek(0)
    f.write("This lines is added new.\n" + old_data)
#if we don't write old_data, first line will delete and then new text will add starting.
with open("new.txt","r+") as f:
    f.seek(0)
    f.write("This lines is added.\n" + old_data)

with open("new.txt","a") as f:
    #if we don't write '\n', it will append to the available last lines side by side.
    f.write("\nThis lines is last text.")

#if we want to write center of the all text, we will use readlines() function
with open("new.txt","r+") as f:
    lines = f.readlines()
    lines.insert(2,"Sample\n")
    f.seek(0)
    f.writelines(lines)

isReadable = open("new.txt","r")
if(isReadable.readable()):
    print("that's true it is readable")
elif(isReadable.writable()):
    print("that's true it is writable")
else:
    print("another mode on")

if(isReadable.closed): # using closed.
    print("it was closed")
else:
    isReadable.close()
    print("it is closed.")

with open("new.txt","r+") as f:
    #f.truncate() all of them clear
    #f.truncate(20) # as byte
    f.readline()
    hide = f.tell()
    f.truncate(hide) # it will clear all of them except last line
print(isReadable.closed == False) #Fase
print(f.name) #new.txt
print(f.mode) #r+
print(f.encoding) #cp1254 #which character code type was code.

#for .pdf .png .jpeg  .doc
#with open("new.pdf","rb") as f:
#   f.readline() #b'PDF-1.7\r\n'
#   f.read() #Squeezed text(1068 lines)