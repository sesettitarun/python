#fromkeys()
'''a="codegnan"
print(a)
print(type(a))
print(list(a))
print(tuple(a))
print(set(a))
#print(dict(a))

b=dict.fromkeys(a)
print(b)
b=dict.fromkeys(a,"pooja")
print(b)

b["g"]="python"
print(b)'''

#eval()
'''while True:
    a=int(input("a value"))
    b=int(input("b value"))
    print(a+b)'''

'''while True:
    a=float(input("a value"))
    b=float(input("b value"))
    print(a+b)'''

'''while True:
    a=(input("a value"))
    b=(input("b value"))
    print(a+b))'''

'''while True:
    a=eval(input("a value"))
    b=eval(input("b value"))
    print(a+b)'''

#zip-> we can combain multiple collection into one collection
'''a=[10,20,30,40]
names=["tarun","saranyu","gireesh","sarath"]
print(a+names)

b=zip(a,names)
print(b)

b=list(zip(a,names))
print(b)

b=tuple(zip(a,names))
print(b)

b=set(zip(a,names))
print(b)

b=dict(zip(a,names))
print(b)'''

#enumerate-> we can give counter to the collection
'''names=["gireesh","tarun","saranyu","sarath","sai"]
for i in range(len(names)):
    print(i,names[i])

b=dict(enumerate(names))
print(b)

b=dict(enumerate(names,100))
print(b)'''

#ASCII
#chr(),ord()
'''print(chr(30))
print(chr(90))
print(chr(65))
print(chr(91))'''

#ord()
'''print(ord("a"))
print(ord("z"))
print(ord("e"))'''

'''for i in range(97,123):
    print(chr(i),end=" ")'''

'''for i in range(65,91):
    print(chr(i),end=" ")'''


'''a=input("enter the name:")
for i in a:
    print(i,"-",ord(i))'''

#annonymous function(nameless function)-> annonymous function are nameless functions and we use keyword call as lambda to create a annonymous funtion 
#write a function to calculate 2*x+5 where x=5
'''def f(x):
    print(2*x+5)
f(5)'''

'''def f():
    x=int(input("enter the value"))
    print(2*x+5)
f()'''

#syntax
#a=lambda arg:expr

'''a=lambda x:2*x+5
print(a(5))'''

'''a=int(input("enter the value:"))
b=lambda x:2*x+5
print(b(a))'''

'''a=lambda x,y:x-y
print(a(4,9))'''

'''a=int(input())
b=int(input())
c=lambda x,y:x-y
print(c(a,b))'''

'''a="codegnan"
b=lambda a:a.upper()
print(b(a))'''

'''a=lambda a:a.upper()
print(a("codegnan"))'''

'''a=input()
b=lambda a:a.upper()
print(b(a))'''

'''a=input()
b=lambda a:a.title()
print(b(a))'''

'''fname=input()
lname=input()
c=lambda a,b:fname.title()+" "+lname.title()
print(c(fname,lname))'''

'''a,b=[x for x in input("enter the names").split(" ")]
c=lambda a,b:(a+" "+b).title()
print(c(a,b))'''

#filter()
a=[2,4,5,6,10,12,14,18,20]
'''if a%2==0:
    print(a) ''' #error

'''for i in a:
    if i%2==0:
        print(i)'''

'''b=list(filter(lambda a:a%2==0,a))
print(b)'''

#[],(),{}
'''a=[]
print(type(a))'''

'''b=()
print(type(b))'''

'''c={}
print(type(c))'''

'''d=set()
print(type(d))'''

'''a=[[],(),{},set()," ",None,3,4.6,5+6j,True,False]
b=list(filter(None,a))
print(b)'''

#map() -> each object from collection and forms a new collection
'''a=[1,3,5,7,9,10,11,13,15]
b=[2,4,6,8,10,12,14,16,18]
c=list(map(max,a,b))
d=list(map(min,a,b))
print(c)
print(d)'''

'''a=input("data1")
b=input("data2")
print(a+b)'''

'''a,b=input("enter the names").split(",")
print(a+b)'''

'''a,b=[x for x in input("names").split(",")]
print(a+b)'''

'''a=int(input("a value"))
b=int(input("b value"))
print(a+b)'''

'''a,b=[int(x) for x in input("values").split(",")]
print(a+b)'''

'''a,b=int(input("enter the value").split(","))
print(a+b)'''     #error

'''a,b=map(int,input("enter the values").split(","))
print(a+b)'''

'''a,b=map(str,input("enter the value").split(","))
print(a+b)'''

'''a=list(map(int,input("enter the values").split(",")))
print(a)
print(type(a))'''

'''a=tuple(map(int,input("enter the values").split(",")))
print(a)
print(type(a))'''

'''a=set(map(int,input("enter the values").split(",")))
print(a)
print(type(a))'''

'''a=list(map(eval,input("enter the values").split(",")))
print(a)
print(type(a))'''

'''a=input()
b=dict(i.split(":") for i in a.split(","))
print(b)'''

















