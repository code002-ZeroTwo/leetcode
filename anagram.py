def isAnagram(s,t):
    for i in s:
        if i in t:
            s = s.replace(i,"")
            t = t.replace(i,"")
        
    if len(s) == len(t) == 0:
        return True
    else:
        return False
    
print(isAnagram("anagram","nagaram"))
