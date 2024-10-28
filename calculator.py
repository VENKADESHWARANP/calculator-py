#program to perform the  simple calculator  operations
print("choose the operation:")
print("1-add")
print("2-subtract")
print("3-multiply")
print("4-division")
option=int(input("choose the operation:"))

if (option in[1,2,3,4]):
    num1=int(input("enter the value 1:" ))
    num2=int(input("enter the value 2:")) 

    if(option==1):
        result=num1 +num2
    elif(option==2):
          result=num1-num2
    elif(option==3):
         result=num1*num2
    elif(option==4):
        result=num1//num2          

else:
    print("invalid operation")

print("print the result of the operation is {}".format(result))    