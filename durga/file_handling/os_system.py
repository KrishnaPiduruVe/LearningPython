'''
os module is very important in python development with bigdata it gives us the leverage to interact with system commands 

all commands you think you can give in cmd you can use in system method 

system("hdfs dfs -ls /user/503005642/")

you can run another python program 

system("python /config/workspace/.vscode/durga_udemy/file_handling/test1.py")

you can run java program 

system("javac HelloWorld.java")
system("java HelloWorld")


'''
from os import system

'''
system() is a method in os module
returns 0 or non zero
'''
print(system("dir"))

print(system("di"))

print(type(system("notepad")))

val = system("notepad")

print("val : ", val)

result = system("python /config/workspace/.vscode/durga_udemy/file_handling/test1.py")

print("result : ",result)

result = system("py /config/workspace/.vscode/durga_udemy/file_handling/test1.py")

print("result : ",result)

result = system("python -u  /config/workspace/.vscode/durga_udemy/file_handling/test1.py")

print("result : ",result)

system("sleep 10") 
system("control + l")

import time
time.sleep(7)
system("cls")