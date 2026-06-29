def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

def main():
    user_input = input("Enter values separated by spaces: ")
    items = user_input.split()
    
    result = remove_duplicates(items)
    print("List without duplicates:", result)

main()