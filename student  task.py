#student marks analysis report
students=int(input("enter the total no.of students"))
marks=[]

for i in range(students):
    mark=int(input("enter the marks"))
    marks.append(mark)

for i in marks:
    print(i,end=" ")

print("marks analysis report.....")
print("the heightest marks",max(marks))
print("the lowest marks",min(marks))
print("the total marks",sum(marks))
print("the average marks",sum(marks)/students)



'''students=int(input("enter the total no.of students"))
marks=[]

for i in range(students):
    mark=int(input(f"enter the marks{i,i+1}"))
    marks.append(mark)

for i in marks:
    print(i,end=" ")

print("marks analysis report.....")
print("the heightest marks",max(marks))
print("the lowest marks",min(marks))
print("the total marks",sum(marks))
print("the average marks",sum(marks)/students)'''
