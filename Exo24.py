def anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    return sorted(str1) == sorted(str2)

print(anagrams("tame", "meta"))  
print(anagrams("tame", "mate"))  
print(anagrams("tame", "team"))  
print(anagrams("tabby", "batty"))  
print(anagrams("python", "java")) 
