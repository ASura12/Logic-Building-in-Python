from collections import Counter

def first_non_repeating_character(s):
    freq = Counter(s)  # Step 1: Count frequency of each character

    # Step 2: Find first character with frequency 1
    for char in s:
        if freq[char] == 1:
            return char
    
    return None  # Return None if all characters repeat

# Example Usage
s = "swiss"
result = first_non_repeating_character(s)

if result:
    print(f"First non-repeating character: {result}")
else:
    print("No non-repeating character found.")
