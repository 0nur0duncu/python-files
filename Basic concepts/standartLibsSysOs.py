#Python Standart Libraries (sys and os module)
#--------------------------------------------

import sys
import os

print("Hello")
#sys.exit() #end of the execution

print(sys.executable) #C:\\python39\\pythonw.exe
print(sys.getwindowsversion()) #sys.getwindowsversion(major=10, minor=0, build=22621, platform=2, service_pack='')
print(sys.path)
print(sys.platform) #win32
print(sys.prefix) #directory of python
print(sys.version) #3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)]
print(sys.version_info) #sys.version_info(major=3, minor=11, micro=0, releaselevel='final', serial=0)
print(sys.stdout) #<_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>
print(sys.stderr) #<_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>
print(sys.stdin) #<_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>

print(os.name) #nt ->for windows posix for ->linux
print(os.sep) #\
print(os.getcwd()) #directory like pwd command
#os.chdir("newDirectory") #change your directory
#print(os.listdir("directoryName"))
print(os.listdir(os.curdir)) #files and directories
print(os.listdir((os.pardir))) #.. directory
#os.startfile("filename in directory.extension")
#os.mkdir("createNewDirectory") or os.mkedirs("createNewDirectoryUnerror")
#os.rename(x,y) #rename or os.replace() #same process
#os.remove("removeFileAndFolders")
#os.remove("emptyFolderDeleted")
#os.removedirs("manyEmptyFolders")
#os.system("matlab.exe") #os.system("explorer.exe")
print(os.urandom(10)) #b'C$U\xfe\x1fQy\x98{\x15'
print(os.environ)
#print(os.path.abspath("fileName"))
#print(os.path.dirname("directory"))
print(os.path.exists("directory")) #True or False
print(os.path.expanduser("~")) #default user