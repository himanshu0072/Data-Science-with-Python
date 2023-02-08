a=int(input("Enter a number:"))
print("Enter an operator like.... + , - , * ,  / , %  , **")
b=input("Enter operator:")
c=int(input("Enter a number:"))

match b:
    case "+":
        print("Sum=",a+c)
    case '-':
        print("Dif=",a-c)
    case '*':
        print("Product=",a*c)
    case '/':
        print("Division=",a/c)
    case '%':
        print("Remainder=",a%c)
    case '**':
        print("Square=",a**c)
    case _:                                
        print(f"{b} is Not a correct operator")