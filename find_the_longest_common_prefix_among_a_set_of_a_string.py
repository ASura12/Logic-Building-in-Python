def longest_common_prefix(strs):
    if not strs:
        return ""
    
    strs.sort()
    first, last = strs[0], strs[-1]
    i = 0
    while i < len(first) and first[i] == last[i]:
        i += 1
    
    return first[:i]

if __name__ == "__main__":
    n = int(input("Enter number of strings: "))
    strs = [input("Enter string: ") for _ in range(n)]
    print("Longest Common Prefix:", longest_common_prefix(strs))
