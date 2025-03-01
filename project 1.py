def add(x,y):
     return x+y
def substract(x,y):
     return x-y
def multiplication(x,y):
     return x*y
def division(x,y):
     return x/y
      
operations=input("select(+,-,*,/)")
num1=float(input("enter the first number"))
num2=float(input("enter the second number"))
if operations=="+":
    print(num1,"+",num2,"=",num1+num2)
elif operations=="-":
        print(num1,"-",num2,"=",num1-num2)
elif operations=="*":
     print(num1,"*",num2,"=",num1*num2)
elif operations=="/":
     print(num1,"/",num2,"=",num1/num2)
else:
     print("inavalid operation")