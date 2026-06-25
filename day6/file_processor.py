import os
from datetime import datetime

def process_file(filename):
    try:
        # 'r' opens the file in read mode
        with open(filename, 'r') as file:
            lines = 0
            words = 0
            chars = 0
            
            for line in file:
                lines += 1
                chars += len(line)
                words += len(line.split())
                
            return lines, words, chars
            
    except FileNotFoundError:
        print(f"\nError: The file '{filename}' does not exist.")
        return None

def display_summary(filename, lines, words, chars):
    print("\n---- File Summary Report ----")
    print(f"File Name   : {filename}")
    print(f"Total Lines : {lines}")
    print(f"Total Words : {words}")
    print(f"Total Chars : {chars}\n")

def append_to_log(filename, lines, words, chars):
    # Get the exact current date and time
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{now}] Processed {filename} - Lines: {lines}, Words: {words}, Chars: {chars}\n"
    
    # 'a' opens the file in append mode (so it adds to the bottom instead of overwriting)
    with open("activity_log.txt", "a") as log_file:
        log_file.write(log_message)

def main():
    filename = input("Enter the name of the file to process (e.g., sample.txt): ")
    result = process_file(filename)
    
    if result:
        # Unpack the 3 variables returned by the process_file function
        lines, words, chars = result
        display_summary(filename, lines, words, chars)
        append_to_log(filename, lines, words, chars)
        print("Activity successfully saved to 'activity_log.txt'.")

if __name__ == "__main__":
    main()