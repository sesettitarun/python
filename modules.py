#math module
'''import math
print(math.pi)

print(math.pi*3)

print(math.sqrt(2))

print(math.log(10))

print(math.cos(30))

print(math.sin(30))

print(math.acos(-1))

print(math.tan(45))

print(math.ceil(3.8))

print(math.floor(5.8))'''

'''from math import pi,sqrt,log
print(pi)

print(sqrt(7))

print(log(10))'''

#sys module
'''import sys
print(sys.path)

for i in sys.path:
    print(i)


print(sys.version)'''

#os module
''';import os
print(os.path)

print(os.getcwd())

print(os.listdir())

print(os.mkdir("may6"))

print(os.listdir())'''

#random module-> to generate random number in python, randint funtion is use this is define in random module.
#python defines a set of functions that are used to generate or manipulate random number to the random modules
'''import random
a=random.sample(range(10,30),20)
print(a)

#randint()
import random
a=random.randint(20,40)
print(a)

import random
a=[10,20,30,40,50]
b=random.choice(a)
print(b)'''

#task 1:
'''import random
while True:
    Dice=int(input("enter the roll of dice:"))
    a=random.randint(1,6)
    print(a)
    option=input("roll again? (yes/no)")
    if option=="yes":
        continue
    elif option=="no":
        break
    else:
        print("invalid option")'''

#calendar module
'''import calendar
year=2026
month=6
print(calendar.month(year,month))'''


'''import calendar
year=2027
print(calendar.calendar(year))'''

'''import calendar
year=int(input("enter the year:"))
month=int(input("enter the month:"))
print(calendar.month(year,month))'''

#date & time
'''from datetime import date
a=date.today()
print(a)

import datetime
a=datetime.datetime.now()
print(a)'''

'''import time
a=time.time()
print(a) #epoch time

b=time.localtime(a)
print(b)

print(f"today date is {b.tm_mday}-{b.tm_mon}-{b.tm_year}")

print(f"present time is {b.tm_hour}-{b.tm_min}-{b.tm_sec}")

print(f"present day is {b.tm_mday}-{b.tm_yday}-{b.tm_isdst}")'''


'''import random
import time
for i in range(10):
    a=random.randint(1000,9999)
    print(a)
    time.sleep(2)'''

#attendence report
'''while True:
    a=int(input("enter the students:"))
    present=0
    absent=0
    for i in range(1,a+1):
        s=input(f"student{i}:")
        if s=="p":
            present+=1
        elif s=="a":
            absent+=1
        else:
             pass
    print(f"total no.of students:{a}")
    print(f"presentees:{present}")
    print(f"absentees:{absent}")'''

#Regular expressions(regex)
'''regulor exper are powerful tools (modulas embedded in pythhon) which is mainly used to find a pattern within a
string or files or statements and mainly used for text manipulation'''

'''a="codegnan is in vja"
print(a)'''

'''b="codegnan\nis\tin\nvja"
print(b)'''

#rstring
'''a=r"codegnan\nis\tin\nvja"
print(a)'''

#compile(),search(),findall(),split(),sub(),sequence characters
'''\w-> it matches alphanumeric
\W-> it matches non-alphanumeric
\d-> it matches any digit
\D-> it matches non-digit
\s-> it represents while spaces
\S-> it represents non-while spaces'''

#compile()
'''import re
a="cap cash map money mat maths cat dog donkey cup"
b=re.compile(r"m\w\w\w")
print(b)'''

#search()
'''c=b.search(a)
print(c)'''

'''b=re.search(r"m\w+",a)
print(b)'''

#findall()
'''c=re.findall(r"m\w+",a)
print(c)
print(*c)'''

'''c=re.findall(r"c\w+",a)
print(*c)'''

'''c=re.findall(r"d\w+",a)
print(*c)'''

#split()
'''d=re.split(r"c",a)
print(d)'''

'''d=re.split(r"\s",a)
print(d)'''

#sub()
'''e=re.sub(r"cat","science",a)
print(e)'''

'''import re
a="20 cap is 40 rs in cash he wins the 5 times cup"
f=re.findall(r"\d+",a)
print(f)
f=re.search(r"\d",a)
print(f)'''

#error handlind-
'''1). syntax error-> compile error
2). runtime error-> during execution time it will happens
3). logical error-> error in logic (it cannot visible)'''

#syntax error:
'''for i in range(10)
print(i)'''

#run_time error
'''a=int(input("a value"))
b=int(input("b value"))
print(a//b)'''

#logical error
'''a=10
b=20
print(a-b)'''

'''a=3
b=7
if a>b:
    print("less")'''

#exception handling
'''1). try-> instructions from which we are expecting the exceptions
2). except->exceptions are raised in try block it will be handle by this block
3). else-> optional(no-exception)
4). finally-> always'''

'''while True:
    a=int(input("a value"))
    b=int(input("b value"))
    try:
        c=a//b
        print(c)
    except:
        print("exception is raised")
    else:
        print("no exceptions")
    finally:
        print("program ends")'''

#file handling
#write()
'''a=open("tarun.txt","w")
a.write("codegnan")
a.close()'''

'''a=open("tarun.txt","w")
a.write("python")
a.close()'''

#append()
'''a=open("tarun.txt","a")
a.write("hello")
a.close()'''

'''a=open("tarun.txt","w")
a.write(input())
a.close()'''

'''a=open("tarun.txt","w")
b=input()
a.write(b)
a.close()'''

'''a=open("tarun.txt","w")
b=input()
a.write(b)
a.close()'''

#read()
'''a=open("tarun.txt")
#print(a.read())  #it will diplay entire data
#print(a.readline())  #it will display first line
#print(a.readlines())  #it will display with \n
print(a.read(5))'''

#writelines() #it makes every object side by side
'''a=["tarun","gireesh","saranyu","sarath","kumar"]
b=open("srinu.txt","w")
b.writelines(a)
b.close()'''

'''a=["tarun","gireesh","saranyu","sarath","kumar"]
b=open("srinu.txt","w")
b.writelines("\n".join(a))
b.close()'''

'''a=open("data.py")
print(a.read())'''

'''a=open("C://Users//user//OneDrive//Desktop//python  course//string.py")
print(a.read())'''







