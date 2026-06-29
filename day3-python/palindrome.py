text = input("Enter a string: ")

# Make it lowercase and remove spaces for accurate checking
cleaned_text = text.lower().replace(" ", "")
reversed_text = cleaned_text[::-1]

if cleaned_text == reversed_text:
    print(f"{text} -> Palindrome")
else:
    print(f"{text} -> Not a Palindrome")