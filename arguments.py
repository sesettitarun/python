#keyword and positional arguments
'''def details(id,name,mailid):
    id=10
    name="tarun"
    mailid="tarun@gmail.com"
    print(id,name,mailid)
details(id="id",name="name",mailid="mailid")'''

'''def details(id,name,mailid):
    print(id,name,mailid)
details(id="id",name="name",mailid="mailid")
details(id=20,name="tarun",mailid="tarun@gmail.com")
details(id=15,name="saranyu",mailid="saranyu@gmail.com")
details(25,"gireesh","gireesh@gmail.com")
details("sarath","sarath@gmail.com",30)
details(name="srinu",mailid="srinu@gmail.com",id=35)'''

#default arguments

'''def Grocery(item,price):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery("sugar",100)'''

'''def Grocery(item="rice",price=1600):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery()'''

'''def Grocery(item,price=500):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery("ghee")'''

'''def Grocery(item="Dhal",price): #non default arg follows default argu
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery()'''

#cake,price,quantity
'''def grocery(cake,price,quantity):
    print("cake is %s" %cake)
    print("price is %.1f" %price)
    print("quantity is %.1f" %quantity)
grocery("chocolate",600,85)'''

'''def grocery(cake="chocolate",price=600,quantity=85):
    print("cake is %s" %cake)
    print("price is %.1f" %price)
    print("quantity is %.1f" %quantity)
grocery()'''

'''def grocery(cake,price,quantity=85):
    print("cake is %s" %cake)
    print("price is %.1f" %price)
    print("quantity is %.1f" %quantity)
grocery("chocolate",600)'''

'''def grocery(cake="chocolate",price,quantity=85):
    print("cake is %s" %cake)
    print("price is %.1f" %price)
    print("quantity is %.1f" %quantity)
grocery(600)'''

# *arguments- *is used to unpack the elements
'''a=[2,3,4,5,6,7,8]
print(a)
print(*a)'''

'''b=(6,7,8,9)
print(b)
print(*b)'''

'''c={5,6,7,8,9,10}
print(c)
print(*c)'''

'''d={"year":2026,"month":4}
print(d)
print(*d)'''

'''a="codegnan"
print(a)
print(*a)'''

'''a,b,c=2,3,4,5,6,7,8,9,10,11,12
print(a)
print(b)
print(c)''' #value error

'''a,b,c=2,3,4
print(a)
print(b)
print(c)'''

'''a,b,*c=2,3,4,5,6,7,8,9,10,11,12
print(a)
print(b)
print(*c)'''

'''a,b,c="codegnan"
print(a)
print(b)
print(c)''' #value error

'''a,b,c="cod"
print(a)
print(b)
print(c)'''


'''a,*b,c="codegnan"
print(a)
print(*b)
print(c)'''


























