#list comprehension
#every list comprehension can be re-written but every for loop cannot be re-written in list comprehension
a=["python","java","dsa"]
#["PYTHON","JAVA","DSA"]
'''b=str(a)
c=b.upper()
print(c)'''

'''for i in a:
    print(i.upper(),end=" ")'''
#syntax

#a=[exp for var in collection/range]
'''a=[b.upper() for b in a]
print(a)'''

'''a=["hyd","vzg","vja"]
#['HYD","VZG","VJA"]
a=[i.title() for i in a]
print(a)'''

'''a=[1,2,4,5,6,8,12,13]
#[1,4,16,25,36,64,144,169]
b=[i*i for i in a]
print(a)'''

'''b=[i**2 for i in a]
print(a)'''

''''b=[pow(i,2) for i in a]
print(a)'''
#if-usage in list comprehension
'''a=[n for n in range(16) if n%2==0]
print(a)'''

'''a=[n*2 for n in range(16) if n%2==0]
print(a)'''

'''fruits=["apple","banana","mango","grapes","kiwi","berry"]
a=[i for i in fruits if "a" in i]
print(a)'''

'''a=[i for i in fruits if not "a" in i]
print(a)'''

#no-elif usage in list comprehension
#if-else usage in list comprehension

'''a=[ n**2 if n%2==0 else n*5 for n in range(21)]
print(a)'''

a=[1,2,3,4,5]
b=[5,4,3,2,1]
#[6,6,6,6,6]
'''c=[a[i]+b[i] for i in range(5)]
print(c)'''

'''c=[a[i]+b[i] for i in range(len(a))]
print(c)'''





















