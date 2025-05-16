
def calculator():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Multiplication")
    
    choice = input("Enter choice (1/2): ")
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == '1':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif choice == '2':
        result = num1 * num2
        print(f"{num1} × {num2} = {result}")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    calculator()
