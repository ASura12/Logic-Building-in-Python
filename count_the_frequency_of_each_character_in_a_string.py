def count_frequency(s):
    freq = {}

    # Count occurrences of each character
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    # Display character frequencies
    print("\nCharacter Frequencies:")
    for char, count in freq.items():
        print(f" '{char}' -> {count}")

# Taking input from user
string = input("Enter the string: ")
count_frequency(string)
