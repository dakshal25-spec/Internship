def count_word_frequency(text):
    words = text.split()
    frequency = {}
    
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
            
    return frequency

def main():
    paragraph = input("Enter a paragraph: ")
    word_counts = count_word_frequency(paragraph)
    
    print("\nWord Frequencies:")
    for word, count in word_counts.items():
        print(f"{word} -> {count}")

main()