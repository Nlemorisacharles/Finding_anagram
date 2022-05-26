# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word1, word2):
    if (len (word1)== len(word2)):
        sorted_str1 = sorted(word1)
        sorted_str2 = sorted(word2)
        
        if (sorted_str1 == sorted_str2):
            return "True"
        else:
            return "false"
    else:
        return "false"
anagram = find_anagram("below" , "elbow")
print(anagram)


