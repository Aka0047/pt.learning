def main():
    operation = input("What do you want to do?(+, -, *-, or /):")
    if (operation != "+" and operation != "-" and operation != "*" and operation != "/"):
        print("Your input is invalid. Please enter a valid input.")
    else:
        num1 = float(input("Enter value for num1: "))
        num2 = float(input("Enter value for num2: "))
        if (operation == "+"):
            print(num1 + num2)
        elif (operation == "-"):
            print(num1 - num2)
        elif (operation == "*"):
            print(num1 * num2)
        elif (operation == "/"):
            if(num2!=0):
                print(num1 / num2)
            else:
                print("you cant divide with 0")
        

if __name__ == "__main__": 
    try:
        while True:
            main()
    except KeyboardInterrupt:
        pass
    #For this the exit keystroke would be ctrl+c