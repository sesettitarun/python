Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list[]
a=[4,6.7,"pooja",7+9j,True,False]
print(a)
[4, 6.7, 'pooja', (7+9j), True, False]
type(a)
<class 'list'>
b=6.0
type(b)
<class 'float'>
c=[6.0]
type(c)
<class 'list'>
a= ["python","java","c","c++"]
a.append("ml")
a
['python', 'java', 'c', 'c++', 'ml']
a.append("ds","ai")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a.append("ds","ai")
TypeError: list.append() takes exactly one argument (2 given)
a(2)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a(2)
TypeError: 'list' object is not callable
a[2]
'c'
a[2:4]
['c', 'c++']
a.aappend(["ds","ml")]
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
a.append(["ds","ml"])
a
['python', 'java', 'c', 'c++', 'ml', ['ds', 'ml']]
a.extend(["ds","ml"])
a
['python', 'java', 'c', 'c++', 'ml', ['ds', 'ml'], 'ds', 'ml']
a=["vjy","hyd"]
a.insert[1,"kkd"]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a.insert[1,"kkd"]
TypeError: 'builtin_function_or_method' object is not subscriptable
a.insert(1,"kkd")
a
['vjy', 'kkd', 'hyd']
a=["c","c++","python"]
a.index("c++")
1
a.copy()
['c', 'c++', 'python']

a.clear()
a
[]
b=[]
b.append("pooja")
b
['pooja']
a=["ap","hyd","mi","chennai","goa"]
a.sort()

a
['ap', 'chennai', 'goa', 'hyd', 'mi']
b=[3,5,7,1,9,7,6]
b.sort()
b
[1, 3, 5, 6, 7, 7, 9]
a=["tarun","are","how","you"]
a.reverse()
a
['you', 'how', 'are', 'tarun']
b={9,8,5,6,4,2]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
b=[8,4,2,3,6,9,7]
b.reverse()
b
[7, 9, 6, 3, 2, 4, 8]
b.sort()
b
[2, 3, 4, 6, 7, 8, 9]
a=["apple","grapes","orange"]
a.pop()
'orange'
a
['apple', 'grapes']
a.pop("apple")
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    a.pop("apple")
TypeError: 'str' object cannot be interpreted as an integer
a.pop("grapes")
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    a.pop("grapes")
TypeError: 'str' object cannot be interpreted as an integer
a
['apple', 'grapes']
#remove
a=["chocolates","sweets"]
a.remove("chocolates")
a
['sweets']
a.count("sweets")
1
b="python"
len(b)
6
c=["python"]
len(c)
1
#tuple()
a=(3,2.4,"python",2+4j,True,False)
print(a)
(3, 2.4, 'python', (2+4j), True, False)
type(a)
<class 'tuple'>
a.count("python")
1
len(a)
6
a.index(False)
5
a.index("python")
2
#sets
#sets{}
a={4,2.5,"hlo",1+5j,True,False}
print(a)
{False, True, 2.5, (1+5j), 4, 'hlo'}
type(a)
<class 'set'>
b={7,2,9,7,5,6,9,8,4,1,3,9}
type(b)
<class 'set'>
print(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9}
a={4,5,8,9,1}
a.add(0)
a
{0, 1, 4, 5, 8, 9}
#issubset()
a={7,8,9,6,5,4}
b={6,5,4}
b.issubset(a)
True
a.issubset(b)
False
#issuperset()
a={1,2,3,6,8}
b={6,8}
b.issuperset(a)
False
a.isisperset(b)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    a.isisperset(b)
AttributeError: 'set' object has no attribute 'isisperset'. Did you mean: 'issuperset'?
a.issuperset(b)
True
#union()
a={1,2,3,6,9,8}
b={8,9,6,5,2}

a.union(b)
{1, 2, 3, 5, 6, 8, 9}
#intersection()
a={7,4,1,2,6,9}
b={9,7,4,6,1}
a.intersection(b)
{1, 4, 6, 7, 9}
b.intersection(a)
{1, 4, 6, 7, 9}
#differences()
a={1,2,3,6,5,4,7}
b={9,8,5,6,4,2}
a.differences(b)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    a.differences(b)
AttributeError: 'set' object has no attribute 'differences'. Did you mean: 'difference'?
a.difference(b)
{1, 3, 7}
b.difference(a)
{8, 9}
#update()
a={9,8,7,6,5}
b={6,5,4,3,2}
a.update(b)
a
{2, 3, 4, 5, 6, 7, 8, 9}
a
{2, 3, 4, 5, 6, 7, 8, 9}
b
{2, 3, 4, 5, 6}
b.update(a)
b
{2, 3, 4, 5, 6, 7, 8, 9}
b
{2, 3, 4, 5, 6, 7, 8, 9}
#symmetric_difference()
a={9,6,5,8,4}
b={6,5,8,4,3}
a.symmetric_difference(b)
{3, 9}
b.symmetric_difference(a)
{3, 9}
#difference update()
a={9,6,5,3,2}
b={7,8,9,6,3,2,5}
b.difference(a)
{8, 7}
a.difference(b)
set()
a.difference_update(b)
a
set()
b.difference_update(a)
b
{2, 3, 5, 6, 7, 8, 9}
#interaction update()
a={12,18,19,16}
b={15,11,16,14,13}
a.interaction_update(b)
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    a.interaction_update(b)
AttributeError: 'set' object has no attribute 'interaction_update'. Did you mean: 'intersection_update'?
a.intersection_update(b)
a
{16}
b.intersection_update(a)
b
{16}
#symmetric difference update()
a={7,8,9,4,2,6,3}

b={1,2,5,4,8,9,6}
a.symmetric_difference_update(b)
a
{1, 3, 5, 7}
b.symmetric_difference_update(a)
a
{1, 3, 5, 7}

a={6,4,5,3,5,9}
a.pop()
3
a.pop(5)
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    a.pop(5)
TypeError: set.pop() takes no arguments (1 given)
a.remove(5)
aa
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    aa
NameError: name 'aa' is not defined. Did you mean: 'a'?
a
{4, 6, 9}
a={8,9,6,5,2}
a.discard(6)
a
{2, 5, 8, 9}
a.copy()
{8, 9, 2, 5}
b=a.copy()
>>> b
{8, 9, 2, 5}
>>> a={3,6,9,8}
>>> a.clear()
>>> a
set()
>>> b=set()
>>> b.add(20)
>>> b
{20}
>>> a={5,2,6,9,8,7}
>>> a.index()
Traceback (most recent call last):
  File "<pyshell#165>", line 1, in <module>
    a.index()
AttributeError: 'set' object has no attribute 'index'
>>> len(a)
6
>>> a.count(a)
Traceback (most recent call last):
  File "<pyshell#167>", line 1, in <module>
    a.count(a)
AttributeError: 'set' object has no attribute 'count'
>>> a={1,2,3,6,5,4}
>>> b={5,6,9,8,7}
>>> a.isdisjoint(b)
False
>>> a={1,2,3,4}
>>> b={5,6,7,8}
>>> a.isdisjoint(b)
True
