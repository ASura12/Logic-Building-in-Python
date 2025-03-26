def check_palindrome(str):
    str = list(str)
    left ,right = 0 , len(str) - 1
    while(left < right):
        if(str[left] != str[right]):
            return False
        left+=1
        right-=1
    return True


str = "madam"
if(check_palindrome(str)):
    print("Given string is a palindrome")
else:
    print("Given string is not a palindrome")