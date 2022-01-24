num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Enter which operation would you like to perform?")
choice = input("Enter 'a' to add,\nEnter 'b' to substract,\nEnter 'c' to divade,\n"
               "Enter 'd' to multiply,\nEnter 'e' to get number square. ")
result = 0
if choice == 'a':
    result = num1 + num2
    print(result)
elif choice == 'b':
    result = num1 - num2
    print(result)
elif choice == 'd':
    result = num1 * num2
    print(result)
elif choice == 'c':
    result = num1 / num2
    print(result)

else:
    print("Input character is not recognized!")




