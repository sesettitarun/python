Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string methods
#len()
a="python"
len(a)
6
b="python course"
len(b)
13
c=""
len(c)
0
d=" "
len
<built-in function len>
len(d)
1
#count()
a= "twinkle twinkle little star"
a.count("twinkle")
2
a.count("t")
5
a.count(" ")
3
#find a string
a="code"
a[1]
'o'
a.find("c")
0
a.find("e")
3
b="intern"
b.find("n")
1
b[2]+b[6]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    b[2]+b[6]
IndexError: string index out of range
b[1]+b[5]
'nn'
#escape sequences
#\n->new line
#\t->tab space
a="name\nmobileno\tmailid\naddress\tgender"
print(a)
name
mobileno	mailid
address	gender
b="name:tarun\nmobileno:8985421846\tmailid:tarunsesetti703@gmail.com\tgender:male"
print(b)
name:tarun
mobileno:8985421846	mailid:tarunsesetti703@gmail.com	gender:male
c="name:tarun\nmobileno:8985421846\tmailid:tarunsesetti703@gmail.com\nkakinada\tgender:male"
print(c)
name:tarun
mobileno:8985421846	mailid:tarunsesetti703@gmail.com
kakinada	gender:male
#replace
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
a
'wait until you succeed'
#upper()
a="tarun"
a.upper()
'TARUN'
#lower()
b="SESETTI"
a.lower()
'tarun'
c="python"
c.upper("p")
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    c.upper("p")
TypeError: str.upper() takes no arguments (1 given)
c[0].upper()
'P'
c.capitalize()
'Python'
d="python course"
d.title()
'Python Course'
d="i am in class"
d.title()
'I Am In Class'
a="hello"
a.isupper()
False
a.islower()
True
a.startwith("h")
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    a.startwith("h")
AttributeError: 'str' object has no attribute 'startwith'. Did you mean: 'startswith'?
a.startswith("h")
True
a.endswith("o")
True
b="python course"
b.isalpha()
False
>>> c="pythoncourse"
>>> c.isalpha()
True
>>> d=12345
>>> d.isdigit()
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    d.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
>>> d="12345"
>>> d.isdigit()
True
>>> e="tarun123"
>>> e.isalpha()
False
>>> e.isalnum()
True
>>> f."tarun@123"
SyntaxError: invalid syntax
>>> f="tarun@123"
>>> f.isalnum()
False
>>> #slipt
>>> a="python java c c++"
>>> a.split()
['python', 'java', 'c', 'c++']
>>> b="i am learning python full stack"
>>> b.split()
['i', 'am', 'learning', 'python', 'full', 'stack']
>>> b.split(2)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    b.split(2)
TypeError: must be str or None, not int
b.split("2")
['i am learning python full stack']
#join()
a="kkd","hyd","vjy"
"".join(a)
'kkdhydvjy'
" ".join(a)
'kkd hyd vjy'
#strip : strip is used the white spaces"
#strip: strip is remove the spaces
#lstrip: lstrip is remove the left spaces
#rstrip: rstrip is used the remove the right spaces
a="         tarun          "
a.strip()
'tarun'
a.lstrip()
'tarun          '
a.rstrip()
'         tarun'
#concatenation
a="python"
b="course"
print(a+b)
pythoncourse
print(a+" "+b)
python course
fname="tarun"
1name="s"
SyntaxError: invalid decimal literal
lname="s"
print(fname+lname)
taruns
print(fname+" "+lname)
tarun s
print(fname.tittle()+" "+lname.title())
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    print(fname.tittle()+" "+lname.title())
AttributeError: 'str' object has no attribute 'tittle'. Did you mean: 'title'?
print(fname.title()+" "+lname.title())
Tarun S
print((fname+" "+lname).title())
Tarun S
#formatting
a=2
b=3
print(a+b)
5
print("the sum is",a+b)
the sum is 5
city+"kkd"
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    city+"kkd"
NameError: name 'city' is not defined
city="kkd"
print("the city is",city)
the city is kkd
#format()
a="motu"
b="patlu"
print("hello {}{}".format(a,b))
hello motupatlu
print("hello {} {}".format(a,b))
hello motu patlu
print("hello {} hello {}".format(a,b))
hello motu hello patlu
#fstring
a="tarun"
b="sesetti"
print(f"hello {a}{b}")
hello tarunsesetti
print(f"hello {a} {b}")
hello tarun sesetti
print (f"hello {a} hello {b}")
hello tarun hello sesetti
