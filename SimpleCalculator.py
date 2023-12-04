while True:
    print("Enter 1 for Addition")
    print("Enter 2 for Subtraction")
    print("Enter 3 for Multiplication")
    print("Enter 4 for Division")
    print("Enter 5 for Exit")
    choice=int(input("Enter your Choice: "))
    if choice in [1,2,3,4]:
        if choice==1:
            a=int(input("Enter first number: "))
            b=int(input("Enter second number: "))
            print(a+b)
        elif choice==2:
            a=int(input("Enter first number: "))
            b=int(input("Enter second number: "))
            print(a-b)
        elif choice==3:
            a=int(input("Enter first number: "))
            b=int(input("Enter second number: "))
            print(a*b)
        elif choice==4:
            a=int(input("Enter first number: "))
            b=int(input("Enter second number: "))
            print(a/b)
        again=input("Do you want to perform another calculation? (y/n): ")
        if again.lower()!="y":
            break
            
    if choice==5:
        print("Exiting the Calculator")
        break
    else:
        print("Invalid choice.Please enter valid option")
    
    
