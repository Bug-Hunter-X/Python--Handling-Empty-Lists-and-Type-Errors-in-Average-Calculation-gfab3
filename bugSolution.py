def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("List must contain only numbers")
    return sum(numbers) / len(numbers)

# Example usage:
my_numbers = [1, 2, 3, 4, 5]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_numbers = []
average = calculate_average(my_numbers) 
print(f"The average is: {average}")

my_numbers = [1,2,'a']
try:
    average = calculate_average(my_numbers) 
    print(f"The average is: {average}")
except ValueError as e:
    print(f"Error: {e}") 