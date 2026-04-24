#1 task voting
'''age=int(input("enter the age:"))
if age>=18:
    print("eligible")
else:
    print("not eligible")'''

#2 task even or odd
'''num=int(input("enter the number:"))
if num%2==0:
    print("it is even")
else:
    print("it is odd")'''
 
#3 leap or non leap year
'''year=int(input("enter the year:"))
if year%4==0:
    print("it is leap year")
else:
    print("non leap year")'''

#4 vowels
'''a=input("enter the letter:")
if a in"aeiou":
    print("vowels")
else:
    print("consonant")'''

'''vowels=["a","e","i","o","u"]
a=("enter the letter:")
if a in vowels:
    print("vowels")
else:
    print("consonant")'''

'''vowels=["a","e","i","o","u"]
a=("enter the letter:").lower()
if a in vowels:
    print("vowels")
else:
    print("consonant")'''

#5 guest code
'''name=input("enter the name").lower()
if name=="tarun":
    print("welcome",name)
else:
    print("welcome guest")'''


'''name=["tarun","gireesh","saranyu","sarath"]
a=input("enter the name").lower()
if a in name:
    print("welcome",a)
else:
    print("welcome guest")'''

#swapping
'''a=10
b=20
a,b=b,a
print("a is value is",a)
print("b is value is",b)'''


'''a=10
b=20
a=a+b
b=a-b
a=a-b
print("a value is",a)
print("b value is",b)'''

'''a=10
b=20
a=a+b
b=a-b
a=a-b
print("after swapping a=%d,b=%d" %(a,b))'''


#social media login
'''username=input("enter the username:")
password=input("enter the password:")
if username=="tarun" and password=="12345":
    print("login successful")
else:
    print("not match")'''


'''username=input("enter the username:")
password=input("enter the password:")
if username=="tarun":
    if  password==12345:
        print("login successful")
    else:
        print("not match")
else:
    print("invalid user")'''


#bakery

'''price=int(input("enter the cake price:"))
if price==1200:
    print("redvelvet")
elif price==1000:
    print("choco almond")
elif price==800:
    print("chocolate cake")
elif price==600:
    print("butterscotch")
else:
    print("The cake is not available")'''

#pizza

'''name=input("enter the pizza name:")
if name=="BBQ pizza":
    print(1000)
elif name=="crispy chicken pizza":
    print(800)
elif name=="panner  pizza":
    print(600)
elif name=="corn pizza":
    print(400)
elif name==("french fired coke"):
    print(200)
else:
    print("The pizza is not available")'''


#loop task-1
a=["codegnan","python","course"]
'''b=str(a)
c=b.upper()
print(c)'''

'''for i in a:
    print(i.upper(),end=" ")'''

'''b=[]
for i in a:
    b.append(i.upper())
print(b)'''

#task-2
'''marks=int(input("enter the marks:"))
if marks>=91 and marks<=100:
    print("Grade-A")
elif marks>=81 and marks<=90:
    print("Grade-B")
elif marks>=71 and marks<=80:
    print("Grade-C")
elif marks>=50 and marks<=70:
    print("Grade-D")
else:
    print("fail")'''

#right angle
'''rows=4
for i in range (1,rows+1):
    print("*"*i)'''

'''a=int(input("enter the number:"))
for i in range(1,n+1):
    print("*"*i)'''

#reverse right angle
'''for i in range(5,0,-1):
    prin t("*"*i)'''

'''n=int(input("enter the number:"))
for i in range(n,0,-1):
    prin t("*"*i)'''

#square
'''n=int(input("enter the number:"))
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()'''

#pyramid
'''n=int(input("enter the number:"))
for i in range(1,n+1):
    print(" "*(n-i),"* "*i)'''

































