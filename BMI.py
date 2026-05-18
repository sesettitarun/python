#BMI calculator

while True:
    weight=float(input("enter the weight:"))
    height=float(input("enter the height:"))
    bmi=weight/(height)**2
    if bmi<18.5:
        print("under weight")
    elif bmi>=18.5 and bmi<=24.5:
        print("healthy weight")
    elif bmi>=24.5 and bmi<= 29.5:
        print("over weight")
    elif bmi>30:
        print("obisity")
    else:
        print("no comment.. thank you..")
