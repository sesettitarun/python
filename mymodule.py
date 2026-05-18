#difference between modules library and pakage
'''module-> a module in python is a single python file it consist python code.
it difficully consist of functions,classes and variables that can be used in other python scripts or programs
examples of modules include math.py,random.py or mymodule.py
package-> a package in python is a directory containing one or more python modules and an __init__.py file
the __init__.py file can be empty or contain intialization code for the package
examples of package of include numpy,pandas or jamboo
library-> libraries can consist of multiple module and packages organized to serve a particular purpose or domain
examples of library such as reqeests,numpy,pandas,matplotlib
note-> every python file is module and input is a keyword every python file is saved internally with variable name
as __main__'''

'''def greetings(name):
    print("welcome",name)'''

'''a=9
b=5
c=a+b
print(c)'''

'''a=input("fname")
b=input("lname")
print(a+b)'''

'''details={"idnos":[10,20,30],
         "names":["saranyu","gireesh","tarun"],
         "mark":[70,80,90]}'''

'''def dummy():
    if __name__=="__main__":
        print("this program is run as script")
    else:
        print("this program is run as module")
dummy()'''

'''if __name__=="__main":
    a=[10,20,30,40,50]
    a.append("code")
    a.extend("code")
    print(a)'''

'''a=int(input("enter the key and value pairs:"))
b=dict((lambda:(input("key"),input("value")))()for _ in range(a))
print(b)'''










