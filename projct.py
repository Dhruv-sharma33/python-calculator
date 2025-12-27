print("simple calculator")
number_1 = float(input("enter first number : "))
number_2 = float(input("enter second number : "))

print("choose operation")
print("addition = 1")
print("subtraction = 2")
print("multiplication = 3")
print("division = 4")

choice = input("enter choice(1/2/3/4) : ")

if choice == "1":
    result = number_1 + number_2
    print("result is " , result)

elif choice == "2":
    result = number_1 - number_2
    print("result is " , result)

elif choice == "3":
    result = number_1 * number_2
    print("result is " , result)

elif choice == "4":
    if number_2 == 0:
     print("cannot devide by zero")
    else:
     result = number_1 / number_2
     print("result is " , result)

else:
   print("invalid choice")

       






