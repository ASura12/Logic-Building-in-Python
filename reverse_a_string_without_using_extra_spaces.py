def reverse_string(str1):
    str1 = list(str1)
    left ,right = 0 , len(str1) - 1
    while(left < right):
        str1[left] , str1[right] = str1[right] , str1[left]
        left +=1
        right -=1
    
    return ''.join(str1)


str1 = "HelloWorld"
print(reverse_string(str1))