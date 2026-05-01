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

def check1(*a):
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
check1(2,3,4,5,6.2,9.3,"tarun")
