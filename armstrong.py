def is_armstrong_number(number):
    num_str = str(number)
    num_digits = len(num_str)
    return number == sum(int(digit)**num_digits for digit in num_str)

# Example usage
n = int(input("Enter a number: "))
if is_armstrong_number(n):
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not an Armstrong number.")
