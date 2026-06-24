user_input = input("Enter numbers separated by spaces: ")

# Convert the string input into a list of numbers
number_strings = user_input.split()
numbers = []
for text in number_strings:
    numbers.append(float(text))

if len(numbers) == 0:
    print("No numbers were entered.")
else:
    # Set the first number as the largest initially
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
            
    print(f"The largest number is: {largest}")