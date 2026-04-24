#conditions
#if condition by using comparision operators
#<,>,<=,>=,==,!=
'''a=2
b=4
if a<b:
    print("it is less")'''

'''a=2
b=4
if a>b:
     print("it is less")'''

'''a=5
b=10
if a<=b:
    print("true")'''

'''a=7
b=11
if b>=a:
    print("greater")'''

'''a=2
b=4
if a!=b:
    print("it is less")'''

'''a=10
b=10
if a==b:
    print("it is equal")'''


'''a=int(input("a value"))
b=int(input("b value"))
if a<b:
    print("less")'''


'''a=int(input("a value"))
if a<15:
    print("less")'''


'''a="python"
if a!="java":
    print("true")'''


'''a="python"
if a=="python":
    print("true")'''

'''a=input("name")
if a=="tarun":
    print("true")'''

#if condition by using logical operators
#and,or,not
'''a=9
b=12
if a<b and b>a:
    print("true")'''

'''a=9
b=12
if a<=b and b>=a:
    print("true")'''

'''a=20
b=30
if a!=b and b==a:
    print("true")'''

'''a=4
b=8
if a<b or b>a:
    print("true")'''

'''a=5
b=10
if a<=b or b>=a:
    print("true")'''


'''a=9
b=12
if a!=b and b==a:
    print("true")'''

'''a=6
b=9
if not a<b:
    print("it is less")'''

'''a=6
b=9
if not a>b:
    print("it is less")'''

#if condition by using identify
#is ,is not
'''a=8
if type(a) is int:
    print("it is int")'''

'''a=8
if type(a) is not int:
    print("it is int")'''

'''a=int(input("enter the value"))
if type(a) is int:
    print("true")'''

'''a=2.0
if type(a) is float:
    print("true")'''

'''a= 5.2
if type(a) is not float:
    print("true")'''

#membership
'''a=[3,4,5,6,7,8,9]
if 7 in a:
    print("true")'''

'''a=[3,4,5,6,7,8,9]
if 7 not in a:
    print("true")'''

'''a=[3,4,5,6,7,8,9]
if 10 not in a:
    print("true")'''

'''a=[3,4,5,6,7,8,9,10]
b=int(input("a value"))
if b in a:
    print("true")'''

#if condition by usinng comparision
'''a=6
b=11
if a<b:
    print("flase")
else:
    print("true")'''

'''a=6
b=11
if a>b:
    print("flase")
else:
    print("true")'''

'''a=14
b=14
if a==b:
    print("true")
else:
    print("false")'''

'''a=14
b=14
if a!=b:
    print("true")
else:
    print("false")'''


#if else condition by using logical
'''a=8
b=10
if a<b and  b>a:
    print("true")
else:
    print("false")'''

'''a=8
b=10
if a!=b and  b==a:
    print("true")
else:
    print("false")'''

'''a=15
b=20
if not a<b and  b>a:
    print("true")
else:
    print("false")'''

#if else condition by using identify operators

'''a=9
if type(a) is int:
    print("it is int")
else:
    print("false")'''

'''a=9
if type(a) is int:
    print("it is int")
else:
    print("false")'''

#if else condition by using membership
'''a=[10,20,30,40,50]
if 10 in a:
    print("true")
else:
     print("false")'''

'''a=[10,20,30,40,50]
if 10 not in a:
    print("true")
else:
     print("false")'''

#if-elif condition by using comaparision
'''a=4
b=6
if a<b:
    print("less")
else:
    print("greater")'''

'''a=4
b=6
if a==b:
    print("less")
elif b>a:
    print("greater")'''

'''a=4
b=6
if a==b:
    print("equal")
elif b<a:
    print("greater")
elif a!=b:
    print("not equal")'''

#logical
'''a=4
b=6
if a>b and b<a:
    print("less")
elif b<a or a>b:
    print("greater")
elif not a==b or a<b:
    print("true")'''


#membership
'''a=[3,4,5,6,7,8,9]
if 10 in  a:
    print("no")
elif not 5 in a: 
    print("false")
elif 7 in a:
    print("yes")'''

#identify
'''a=9
if type(a) is int:
    print("it is int")
elif:
    print("false")'''

'''a=9
if type(a) is int:
    print("it is int")
elif:
    print("false")'''


#if-elif-else condition by using comparision
'''a=8
b=9
if a<b:
    print("less")
elif b>a:
    print("greater")
elif a!=b:
    print("not equal")
else:
    print("true")'''

#logical
'''a=4
b=6
if a>b and b<a:
    print("less")
elif b<a or a>b:
    print("greater")
elif not a==b or a<b:
    print("true")
else:
    print("false")'''

#membership
'''a=[3,4,5,6,7,8,9]
if not 3 in  a:
    print("no")
elif not 5 in a: 
    print("true")
elif 7  in a:
    print("yes")
else:
    print("false")'''
         
#multiple- if
'''a=4
b=3
if a>b:
    print("greater")
if b<a:
    print("less")
if a==b:
    print("equal")'''

'''a=4
b=3
if a<b:
    print("greater")
if b<a:
    print("less")
if a==b:
    print("equal")'''

#memebership
'''a=[3,4,5,6,7,8,9]
if 3 in  a:
    print("true")
if 5 in a: 
    print("true")
if 7  in a:
    print("yes")'''

'''a=[1,2,5,6,8,9]
if not 3 in a:
    print("true")
if not 4 in a:
    print("yes")
if 7 in a:
    print("false")'''

#logical

'''a=4
b=6
if a<b and b>a:
    print("less")
if b>a or a<b:
    print("greater")
if not a==b or a<b:
    print("true")'''

'''a=7
b=6
if a>b and b<a:
    print("yes")
if b<a or a<b:
    print("greater")
if not a==b or a<b:
    print("true")'''

#identify
'''a=[9,4,5,6,'tarun']
if type(a[3]) is int:
    print("it is int")
if type (a[4]) is not int:
    print("false")'''

'''a=[9,4,5,6,'sesetti']
if type(a[1]) is int:
    print("it is int")
if type (a[4]) is chr:
    print("false")'''

#nested-if
'''a=5
a=10
if a<b:
    print("less")
    if b>a:
        print("grater")'''

'''a=10
b=20
if a>b:
    print("less")
    if b>a:
        print("grater")'''

'''a=5
b=10
if a>b:
    print("less")
    if b==a:
        print("greater")'''

'''a=5
b=10
if a<b:
    print("less")
    if b<a:
        print("greater")
    else:
        print("true")'''

'''a=5
b=10
if a>b:
    print("less")
    if b>a:
        print("greater")
    else:
        print("false")
else:
    print("true")'''

'''a=5
b=10
if a==b:
    print("less")
    if b<a:
        print("greater")
    else:
        print("false")
else:
    print("true")'''

'''a=7
b=12
if a<b:
    print("less")
    if a==b:
        print("equal")
    elif a!=b:
        print(not equal")
    else:
        print("true")
else:
    print("false")'''







































