Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dic{}
a={"name":"tarun","year":2026,"month":4}
print(a)
{'name': 'tarun', 'year': 2026, 'month': 4}
type(a)
<class 'dict'>
b={"name","year","month"}
type(b)
<class 'set'>
a.keys()
dict_keys(['name', 'year', 'month'])
a.value()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a.value()
AttributeError: 'dict' object has no attribute 'value'. Did you mean: 'values'?
a.values()
dict_values(['tarun', 2026, 4])
a.items()
dict_items([('name', 'tarun'), ('year', 2026), ('month', 4)])
a={"year":2026,"month":4,"date":16}
a["year"]
2026
a.update({"time":6})
a
{'year': 2026, 'month': 4, 'date': 16, 'time': 6}
a.update({"hour":5,"min":10})
a
{'year': 2026, 'month': 4, 'date': 16, 'time': 6, 'hour': 5, 'min': 10}
a={"name":"tarun","age":20,}
a.setdefault("city","kkd")
'kkd'
a
{'name': 'tarun', 'age': 20, 'city': 'kkd'}

a={"colour",:"black","food":"biriyani")
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
a={"colour",:"black","food":"biriyani"}
SyntaxError: invalid syntax
a={"colour":"black","food":"biriyani")
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
a={"colour":"black","food":"biriyani"}
a.pop()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop("colour")
'black'
a
{'food': 'biriyani'}
a={"city":"kkd","country":"india"}
a.popitem()
('country', 'india')
a
{'city': 'kkd'}
a.copy()
{'city': 'kkd'}
a
{'city': 'kkd'}
a.get("city")
'kkd'
a
{'city': 'kkd'}

>>> a.get("city")
'kkd'
>>> a.clear()
>>> a
{}
>>> b-{}
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    b-{}
TypeError: unsupported operand type(s) for -: 'set' and 'dict'
>>> b={}
>>> b.update({"name":"tarun"})
>>> b
{'name': 'tarun'}
>>> a={"year":2026,"month":"april","name":"tarun","name":"tarun"}
>>> print(a)
{'year': 2026, 'month': 'april', 'name': 'tarun'}
>>> a={"year":2026,"month":"april","name":"tarun","name1":"tarun"}
>>> print(a)
{'year': 2026, 'month': 'april', 'name': 'tarun', 'name1': 'tarun'}
>>> a={"idnos":[1,2,3],"names":["tarun","sarath","gireesh"]}
>>> print(a)
{'idnos': [1, 2, 3], 'names': ['tarun', 'sarath', 'gireesh']}
>>> type(a)
<class 'dict'>
>>> a.keys()
dict_keys(['idnos', 'names'])
>>> a.values()
dict_values([[1, 2, 3], ['tarun', 'sarath', 'gireesh']])
>>> a.items()
dict_items([('idnos', [1, 2, 3]), ('names', ['tarun', 'sarath', 'gireesh'])])
