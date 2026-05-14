def calculator():
    print("--- Python Power Calculator ---")
    
    while True:
        print("\nSelect an operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        # Check if the user wants to exit
        if choice == '5':
            print("Shutting down. Goodbye!")
            break

        # Validate choice
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue

            # Perform operations
            if choice == '1':
                print(f"Result: {num1} + {num2} = {num1 + num2}")

            elif choice == '2':
                print(f"Result: {num1} - {num2} = {num1 - num2}")

            elif choice == '3':
                print(f"Result: {num1} * {num2} = {num1 * num2}")

            elif choice == '4':
                if num2 == 0:
                    print("Error: You cannot divide by zero!")
                else:
                    print(f"Result: {num1} / {num2} = {num1 / num2}")
        else:
            print("Invalid Selection. Please choose 1-5.")

        # Ask if they want to do another calculation
        again = input("\nPerform another calculation? (y/n): ").lower()
        if again != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    calculator()