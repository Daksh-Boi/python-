choice = int(input("Enter 1 for addition, 2 for subtraction, 3 for division, 4 for division and 5 for modulus "))
print("Input the two numbers:")
a = float(input())
b = float(input())
if choice==1:
    print("Sum of",a,"and",b,"is:",(a+b))
elif choice==2:
    print("Difference of",a,"and",b,"is:",(a-b))
elif choice==3:
    print("Product of",a,"and",b,"is:",(a*b))
elif choice==4:
    print("Quotient of",a,"when divided by",b,"is:",(a/b))
elif choice==5:
    print("Mod of",a,"and",b,"is:",(a%b))
else:
    print("Incorrect output")
