#variable length arguments-> variable length argument are automatically store in tupple and we use *arguments.

'''def check(*a):
    print(a)
    print(type(a))
check()

check(2,3,4,5,6)
b=[5,6,7,8,9]
check(*b)

c={4,5,6,7}
check(*c)

d={"name":"tarun","year":2026}
check(*d)'''

'''def check1(*a):
    d=2#creating a varible
    print(a)
    print(type(a))
    for  i in a:
        if type(i) in (int,float):
            d=d+i
            print(d)
check1()
check1(2,3,4,5,6,7)
check1(2,3,4,5.2,7.4)
check1(2,3,4,5,6.2,9.3,"tarun")'''

#kwargs(**)
'''def check(**a):
    print(a)
    print(type(a))
check()
details={"idnos":[10,20,30],
         "names":["saranyu","gireesh","tarun"],
         "places":["vja","hyd","vzg"]}
check(**details)'''

#1
'''def check(**a):
    for i in a:
        print(i)
check()
details={"idnos":[10,20,30],
         "names":["saranyu","gireesh","tarun"],
         "places":["vja","hyd","vzg"]}
check(**details)'''

#2
'''def check(**a):
    for i in  a.keys():
        print(i)
check()
details={"idnos":[10,20,30],
         "names":["saranyu","gireesh","tarun"],
         "places":["vja","hyd","vzg"]}
check(**details)'''

#3
'''def check(**a):
    for i in a:
        print(a[i])
check()
details={"idnos":[10,20,30],
         "names":["saranyu","gireesh","tarun"],
         "places":["vja","hyd","vzg"]}
check(**details)'''


#4
'''def check(**a):
    for i in a.values():
        print(i)
check()
details={"idnos":[10,20,30],
         "names":["saranyu","gireesh","tarun"],
         "places":["vja","hyd","vzg"]}
check(**details)'''

#5
'''def check(**a):
    for i in a:
        print(i,a[i])
check()
details={"idnos":[10,20,30],
         "names":["saranyu","gireesh","tarun"],
         "places":["vja","hyd","vzg"]}
check(**details)'''

#6
'''def check(**a):
    for i in a.items():
        print(i)
check()
details={"idnos":[10,20,30],
         "names":["saranyu","gireesh","tarun"],
         "places":["vja","hyd","vzg"]}
check(**details)'''


'''def check(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in  a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
check()
details={"idnos":[10,20,30],
         "names":["saranyu","gireesh","tarun"],
         "places":["vja","hyd","vzg"]}
check(**details)'''

#both * and ** usage
'''def final(*a,**b):
    d=3 #creating a variable
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i,j in b.items():
        print("key is",i)
        print("value is",j)
final()
data=(2,3,4,5.2,2,4)
final(*data)
details={"idnos":[10,20,30],
         "names":["saranyu","gireesh","tarun"],
         "places":["vja","hyd","vzg"]}
final(**details)
final(*data,**details)'''

#global and local variable-> variable inside and outside the function is called global and local variable
#GLOBAL-> a variable is define above the function and is assese to the entire global space is called global vaiable
#VARIABLE-> a variable is inside the function is called local variable

#first case of global variable
'''a=5
def check():
    print("inside value is",a)
check()
print("outside value is",a)'''

#second case of global variable
'''a=7
def check():
    a=5
    a=a**2
    print("inside value is",a)
check1()
print("inside value is",a)'''

#third case of both global and local variable
'''a=2
b=7
def check2():
    a=4
    print("inside value is",a)
    a=10
    print("updated value is",a+5)
    b=12#local variable
    b=b+a
    print("b valueis",b)
check2()
print("value of a is",a)
print("value of b is",b)'''

#usage of global keyword-> when user wants assess the global variable inside the function directly and carried forward
#-the updated vaiable even outside the function then we need the global variable

''''a=5
def final():
    global a,b
    print("inside value is",a)
    a=10
    print("updated value is",a)
    b=15
    b=b+a
    print("value of b is",b)
final()
print("a value is",a)
print("b value is",b)'''

#generators-> no tuple comprehension in above cases if we remove those brases and keep paramesis then outcome is generator
'''a=[i for i in range(16)]
print(a)
print(type(a))

a=(i for i in range(21))
print(a)
print(*a)
print(type(a))

a=(i for i in range(21))
print(a)
print(list(a))

a=(i for i in range(21))
print(a)
print(tuple(a))

a=(i for i in range(21))
print(a)
print(set(a))'''

# A generetor is also a function which can we use as an itaretor (loop)by producing group of values ,where we use yield keyword
# yield v/s return-> return will terminate the function where as yield will pass func and born with every succesive genaration

'''a,b=[int(x) for x in input("enter the values:").split(",")]
def check(a,b):
    while a<b:
        yield a
        a=a+1
        yield a
print(*check(a,b))'''

'''a,b=[int(x) for x in input("enter the values:").split(",")]
def check(a,b):
    while a<b:
        a=a+1
        return a
print(check(a,b))'''

#yield v/s return

'''def mygen():
    #return "python"
    #return "java"
    #return "ds"
    return "python","java","ds"
print(*mygen())'''

'''def mygen():
    yield "apple"
    yield "mango"
    yield "grapes"
print(*mygen())'''

#next()
'''d=mygen
print(next(d))
print(next(d))
print(next(d))'''











































