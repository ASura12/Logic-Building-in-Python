def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]

def longest_palindrome(s: str) -> str:
    if not s:
        return ""

    longest = ""
    for i in range(len(s)):
        # Odd length palindrome
        odd_palindrome = expand_around_center(s, i, i)
        # Even length palindrome
        even_palindrome = expand_around_center(s, i, i + 1)

        # Update the longest palindrome
        longest = max(longest, odd_palindrome, even_palindrome, key=len)

    return longest

# Example usage
s = "babad"
print(longest_palindrome(s))  # Output: "bab" or "aba"
