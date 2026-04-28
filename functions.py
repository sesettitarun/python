#functions- a function is a block of organized,re-usable code and it is used to perform a single and multiple task
#python gives in-built functions like print you can make your owm function also and these are called user define funtions
#A function block begin with keyword called def followed by the function name and peramesis(())

'''a=10
b=20
print("the sum is",a+b)
print("the sum is",a-b)
print("the product is",a*b)
a=100
b=200
print("the sum is",a+b)
print("the sum is",a-b)
print("the product is",a*b)
a=1000
b=2000
print("the sum is",a+b)
print("the sum is",a-b)
print("the product is",a*b)'''

#function example
'''def calculate(a,b):
    print("the sum is",a+b)
    print("the sum is",a-b)
    print("the product is",a*b)
calculate(10,20)
calculate(100,200)
calculate(1000,2000)'''

'''def calculate(a,b):
    print("the int divi is",a//b)
    print("the pow is",a**b)
    print("the modulas is",a%b)
calculate(10,20)
calculate(20,10)
calculate(1000,2000)'''

'''def add (a,b):
    print(a+b)
add(5,6)'''

'''while True:
    def add():
        a=int(input("a value"))
        b=int(input("b value"))
        print(a+b)
    add()'''

'''def fullname():
    fname=input("first name")
    lname=input("last name")
    print((fname+" "+lname).title())
fullname()'''

#print v/s return
#print- print just shows the human user output in a concole
#return- return is a keyword and return is used to terminate the function and gives back a value function 

'''def sub(a,b):
    print(a-b)
sub(3,8)'''

'''def sub(a,b):
    return a-b
print(sub(2,9))'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
cal(20,5)'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    return c
    return d
    return e
print(cal(20,5))'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    return c,d,e
print(cal(20,5))'''

#1.task-split bill
'''def spilt_bill():
    a=int(input("total bill"))
    b=int(input("person"))
    print(a//b)
spilt_bill()'''

'''def spilt_bill():
    a=int(input("enter the total no.of friends"))
    b=int(input("enter the amounnt"))
    print("perhead bill is",b//a)
spilt_bill()'''


'''def spilt_bill():
    a=int(input("enter the total no.of friends"))
    b=int(input("enter the amount"))
    c=b//a
    print(f"the bill is {c}")
    print("the bill is {}".format(c))
spilt_bill()'''

'''def spilt_bill():
    a=int(input("enter the total no.of friends"))
    b=int(input("enter the amount"))
    print(f"the bill is {b//a}")
    print("the bill is {}".format(b//a))
spilt_bill()'''


#2.task
'''def operations():
    a=int(input("enter a value"))
    b=int(input("enter b value"))
    option=int(input(choose the options
                             1.add
                             2.sub
                             3.mul))
    if option==1:
        print(a+b)
    elif option==2:
        print(a-b)
    elif option==3:
        print(a*b)
    else:
        print("invalid option")
operations()'''


'''def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
    a=int(input("enter a value"))
    b=int(input("enter b value"))
    option=int(input(choose the options
                                 1.add
                                 2.sub
                                 3.mul))
    if option==1:
         print()
    elif option==2:
         print()
    elif option==3:
         print()
    else:
         print("invalid option")
add()
sub()
mul()'''
















    
























