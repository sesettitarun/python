Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #datatypes
>>> a=4
>>> type(a)
<class 'int'>
>>> b=2.3
>>> type(b)
<class 'float'>
>>> c="code"
>>> type(c)
<class 'str'>
>>>  d='tarun'
...  
SyntaxError: unexpected indent
>>> d='tarun'
>>> type(d)
<class 'str'>
>>> e='''solutions'''
>>> type(e)
<class 'str'>
>>> f='t'
>>> type(f)
<class 'str'>
>>> g=2+5j
>>> type(g)
<class 'complex'>
>>> h=3j+7
>>> type(h)
<class 'complex'>
<class 'complex'>
SyntaxError: invalid syntax
x=5j
type(x)
<class 'complex'>
y=true
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    y=true
NameError: name 'true' is not defined. Did you mean: 'True'?
y= True
type(y)
<class 'bool'>
z=False
type(z)
<class 'bool'>
#datatype conversions
#int
int(6)
6
int(5.7)
5
int("tarun")
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    int("tarun")
ValueError: invalid literal for int() with base 10: 'tarun'
int(6+5i)
SyntaxError: invalid decimal literal
int(True)
1

int(False)
0
#float()
float(7)
7.0
float(7.8)
7.8
float("hlo")
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    float("hlo")
ValueError: could not convert string to float: 'hlo'
float(6+j)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    float(6+j)
NameError: name 'j' is not defined
float(True)
1.0
\
float(False)
0.0
#str
str(7)
'7'
str(6.0)
'6.0'
str("hello")
'hello'
str("2+j)
    
SyntaxError: unterminated string literal (detected at line 1)
str(2+j")
    
SyntaxError: unterminated string literal (detected at line 1)
str(2+j)
    
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    str(2+j)
NameError: name 'j' is not defined
str("23+4j")
    
'23+4j'
str(3+5j)
    
'(3+5j)'
str(True)
    
'True'
str(false)
    
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    str(false)
NameError: name 'false' is not defined. Did you mean: 'False'?
str(False)
    
'False'
#complex
    
complex(6)
    
(6+0j)
complex(4.5)
    
(4.5+0j)
complex("tarun")
    
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    complex("tarun")
ValueError: complex() arg is a malformed string
complex(True)
    
(1+0j)
complex(False)
    
0j
#boolean
    
bool(5)
    
True
bool(4.3)
    
True
bool("hlo")
    
True
bool(3+4j)
    
True
bool(True)
    
True
bool(False)
    
False
