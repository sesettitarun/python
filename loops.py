#loops
#for,,while,range,break,continue,pass
#for loop
'''a=[10,20,30,40,50]
for i in a:
    print(i)
print(type(a))
print(type(i))'''

'''a=[10,20,30,40,50]
for i in a:
    print(i,end=" ")'''

'''a=[10,20,30,40,50,60]
for i in a:
    print(a)'''

'''a=(5,6,7,8,9,10)
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''

'''a={3,4,5,6,7,8}
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''

'''a={"name"="tarun","year"=2026,"month"="april")
for i in a:
    print(i)
for i in a.keys():
    print(i)
    print(type(a))
    print(type(i))
for i in a.value():
    print(i)
    print(type(a))
    print(type(i))
for i in a.items():
    print(i)
    print(type(a))
    print(type(i))'''

'''a="codegnan"
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''


'''a=[4.5,6.7,8.9]]
for  i in a:
    print(i)
    print(type(a))
    print(type(i))'''

'''a=["apple","banana","grapes"]
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''

'''a=[5+6j,3+7j]
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''

'''a=[True,False]
for i in a:
    print(i)
    print(type(a))
    print(type(i))'''

#while loop
'''a=10
while a<1:
    print("true")'''

'''a=10
while a>1:
    print("true")'''

'''a=10
while a>1:
    print(a)'''

'''a=10
while a>=1:
    print(a)
    a=a-1'''

'''a=20
while a>=5:
    a=a-1
    print(a)'''

'''a=20
while a>5:
    print(a)
    a=a-1'''

'''a=30
while a>2:
    print(a)
    a+=1'''

#while loop tasks
#voting
'''while True:
    age=int(input("enter the age:"))
    if age>=18:
        print("eligible")
    else:
        print("not eligible")'''

#even or odd
'''while True:
    num=int(input("enter the number:"))
    if num%2==0:
        print("it is even")
    else:
        print("it is odd")'''

#pizza
'''while True:
    pizza=input("enter the pizza:")
    if pizza=="BBQ pizza":
        print(1000)
    elif pizza=="chicken pizza":
        print(950)
    elif pizza=="sandwich":
        print(800)
    elif pizza=="panner pizza":
        print(600)
    elif pizza=="cocacola with pizza":
        print(500)
    else:
        print("pizza is not available")'''

#range: the range function returns a squences of number ,starting from zero by defult and implements a one by one stop before a number 
#start-stop-step
#start
'''for i in range(5):
    print(i)'''

#start-stop
'''for i in range (5,15):
    print(i)'''

#start-stop-step
'''for i in range(2,19,2):
    print(i)'''

'''for i in range(5,46,5):
    print(i)'''

'''for i in range(0,28,3):
    print(i)'''
    
#task
'''while True:
    marks=int(input("enter the marks:"))
    if marks in range(91,101):
        print('A')
    elif marks in range(81,91):
        print('B')
    elif marks in range(71,81):
        print('C')
    elif marks in range(51,71):
        print('D')
    else:
        print('fail')'''

#difference between break,continue,pass

#break - break statement uses the termiates the entir loop
#continue- the continue skips the current iteration and rest of the code due continue
#pass- pass is a null statement if these  nothing bt syntacially we need

#break
'''a=10
while a>1:
    print(a)
    a=a-1
    if a==5:
        break'''

'''a=10
while a>1:
    a=a-1
    if a==5:
        break
    print(a)'''


'''for i in range(20):
    if i==12:
        break
    print(i)'''

#continue
'''a=30
while a>5:
    print(a)
    a=a-1
    if a==20:
        continue'''

'''a=30
while a>5:
    a=a-1
    if a==20:
        continue
    print(a)'''

'''for i in range(15):
    if i==9:
        continue
    print(i)'''

'''a="python"
for i in a:
    if i=="t":
        break
    print(i)'''

'''a="python"
for i in a:
    if i=="t":
        continue
    print(i)'''

#pass

'''a=40
while a>10:
    print(a)
    a=a-1
    if a==15:
        pass'''

'''for i in range(40):
    if i==20:
        pass
    print(i)'''






























