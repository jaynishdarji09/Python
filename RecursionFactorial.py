def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Enter a number: "))
print(f"The factorial of {n} is {factorial(n)}")     
while True:
    choice = input("Do you want to calculate another factorial? (yes/no): ").strip().lower()
    if choice == 'yes':
        n = int(input("Enter a number: "))
        print(f"The factorial of {n} is {factorial(n)}")
    elif choice == 'no':
        print("Exiting the program.")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")