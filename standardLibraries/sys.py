import sys

if(len(sys.argv)!=4):
    print("Usage : filename.py operator operand operator e-g 10 + 5")
    

num1=float(sys.argv[1])
op=sys.argv[2]
num2=float(sys.argv[3])


if(op=="+"):
    print(num1+num2)
elif(op=="-"):
    print(num1-num2)
elif(op=="*"):
    print(num1*num2)
elif(op=="/"):
    print(num1/num2)
else:
    print("Invalid operator or operands")    
