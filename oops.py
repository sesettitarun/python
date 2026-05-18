#oppes->a class contains attributes are variables and methods are function that can manipulate the data
# a class is the blueprint of an object
# an object is an initiation of a class
# methods are functions define in the body of the class

#four pillars of oops:
#plymorphism is 4 types 1. operator overloading 2. operator overriding 3.method overloading 4.method overriding

#inheritens->inheritances has 3 types 1.single inheritences 2.multipe inheritences 3.multi-level inheritances

#enclapulation->combine mutliple unit into single unit is knowm as enclapuation
#enclapulation has 3 types 1.public data 2.__private date 3. _protecteddata

#abstraction->highly unnecessary information from user is known it as a abstraction
#abstract class-> if a class contain one or more than an abstract method is kknown it as abstract class
#abstract method-> if the methid is declared without implementation is called abstract method

#oops syntax:
'''class classname:
    name="codegnan"
    place="vja"
    year="2026"
    def fname(method_name):
        print("statement")
a=classname()
a.fname()'''

#class declaration
'''class Details:
    name="tarun"
    age=20
    place="kkd"
    def direct(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.direct()'''

#object instantiation
'''class Details:
    def Data(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.Data("tarun",20,"kkd")
a.display()
a.Data("saranyu",18,"jdp")
a.display()
b=Details()
b.Data("gireesh",24,"vja")
b.display()'''

#object initalization:
'''class Details():
    #creating a constructor
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=Details("tarun",20,"kkd")
print(dir(a))
a.display()'''

'''class Details():
    #creating a constructor
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def display(self):
        print(self.name,self.age,self.place)
a=input("name:")
b=int(input("age:"))
c=input("place:")
d=Details(a,b,c)
d.display()

e=Details(input("name:"),int(input("age:")),input("place:"))
e.display()'''

'''class Details():
    #creating a constructor
    def __init__(self):
        self.name=input("name:")
        self.age=int(input("age:"))
        self.place=input("place:")
    def display(self):
        print(self.name,self.age,self.place)
a=Details()
print(dir(a))
a.display()'''

#Difference b/w _ and __
#we generally used it for private variable that is when ever we use double reading we use our python interpretor
#treats it special variable to avoid name conflict with method and inner classes

'''class employee():
    def __init__(self):
        self.name="tarun"
        self._mailid="tarun@gmail.com"
        self.__salary="1000000" #private variable        
a=employee()
print(dir(a))
print(a.name)
print(a._mailid)
#print(a.__salary)
print(a._employee__salary)'''

'''class employee1():
    def __init__(self):
        self.name="tarun"
        self._mailid="tarun@gmail.com"
        self.__salary="1000000"
class employee2():
    def __init__(self):        
        self.name="gireesh"
        self._mailid="gireesh@gmail.com"
        self.__salary="1000000"
class employee3():
    def __init__(self):
        self.name="saranyu"
        self._mailid="saranyu@gmail.com"
        self.__salary="1000000" 
        
a=employee1()
print(a.name)
print(a._mailid)
print(a._employee1__salary)

a=employee2()
print(a.name)
print(a._mailid)
print(a._employee2__salary)

a=employee3()
print(a.name)
print(a._mailid)
print(a._employee3__salary)'''


#operator overloading
'''a=2;b=4
print(a+b)
print(a.__add__(b))
print(a.__add__(5))
print(a.__sub__(1))
print(a.__mul__(4))
#print(a.__div__(2))
print(a.__pow__(3))
print(a.__le__(4))
print(a.__ge__(9))
a=[1,2,3,4,5,6];b=[6,7,8,9,10]
print(a.__add__(b))
print(a.__getitem__(3))
print(b.__getitem__(4))
a="code";b="gnan"
print(a.__add__(b))
a="python";b="course"
print(a.__add__(b))
print(a.__add__(" "+b))
print(a.__add__(" "+b).title())
print("tarun".__add__(" "+"s").title())'''

#operator overriding
'''class A():
    def __init__(self,a):
        self.a=a
    def __add__(self,value):
        return self.a*value.b
class B():
    def __init__(self,b):
        self.b=b
x=A(5)
y=B(5)
print(x+y)'''

#method overloading
'''class New():
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("the sum is",a+b+c)
        elif a!=None and b!=None:
            print("the product is",a*b)
        else:
            print("program ends")
x=New()
x.sum()
x.sum(2,4,7)
x.sum(5,3)'''

#method overriding
'''class Animal():
    def speak(self):
        print("animal can make sounds")
class Dog():
    def speak(self):
        print("dog barks")
a=Animal()
b=Dog()
a.speak()
b.speak()'''

'''class lorry():
    def sound(self):
        print("keep distance")
class cab():
    def sound(self):
        print("don't sound horn")
a=lorry()
b=cab()
a.sound()
b.sound()'''

#inheritances:
#single inheritance
'''class RBI():   #parent class
    cash = 100000
    def available_cash(cls):
        print("available cash is",cls.cash)
        print("available cash is",RBI.cash)
class SBI(RBI):  #child-1
    pass
class HDFC(RBI):  #child-2
    cash = 50000
    def new_cash(cls):
        print("new cash is",cls.cash+cls.cash)
        print("new cash is",cls.cash+RBI.cash)
a = HDFC()
a.available_cash()
a.new_cash()'''

#multiple inheritances
'''class father():   #parent-1
    def height(self):
        print("height is 6 feet")
class mother():  #parent-2
    def weight(self):
        print("weight is 65 kgs")
class kid():  #child cllass
    def DOB(self):
        print("just born")
a=father()
a.height()
b=mother()
b.weight()
c=kid()
c.DOB()'''

'''class father():   #parent-1
    def height(self):
        print("height is 6 feet")
class mother():  #parent-2
    def weight(self):
        print("weight is 65 kgs")
class kid(father,mother):  #child cllass
    def DOB(self):
        print("just born")
c=kid()
c.height()
c.weight()
c.DOB()'''


#multi-level inheritences

'''class grandparent():
    def arces(self):
        print("10 arces")
class parent(grandparent):
    def house(self):
        print("100 sqft")
class child(parent):
    def car(Self):
        print("scoda car")
a=child()
a.arces()
a.house()
a.car()'''

#encapsulation:
#public data
'''class parent():
    publicdata=100
    def method1(self):
        print(self.publicdata)
class child(parent):
    def method2(self):
        print(self.publicdata)
obj1=child()
obj1.method1()
obj1.method2()'''

#_protecteddata()
'''class parent():
    _protecteddata=10
    def method1(self):
        print(self._protecteddata)
class child(parent):
    def method2(self):
        print(self._protecteddata)
obj1=child()
obj1.method1()
obj1.method2()
print(obj1._protecteddata)'''


#__privatedata():

class parent():
    __privatedata="tarun"
    def method1(self):
        print(self.__privatedata)
class child(parent):
    def method2(self):
        print(self._parent__privatedata)
obj1=child()
obj1.method1()
obj1.method2()

























