def compress_string(s):
    compressed = []
    count = 1
    
    for i in range(len(s)):
        if i + 1 < len(s) and s[i] == s[i + 1]:
            count += 1
        else:
            compressed.append(s[i] + str(count))
            count = 1
    
    compressed_str = ''.join(compressed)
    return compressed_str if len(compressed_str) < len(s) else s

if __name__ == "__main__":
    input_str = input("Enter a string: ")
    print("Compressed String:", compress_string(input_str))
