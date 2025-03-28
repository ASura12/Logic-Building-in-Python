def are_Anagrams(str1,str2):
    return sorted(str1) == sorted(str2)

s1 = "listen"
s2 = "silent"
if(are_Anagrams(s1,s2)):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")