def longestCommonPrefic(strs):
    prefix = strs[0]

    for words in strs[1:]:
        while words.find(prefix) != 0:
            print(words.find(prefix))
            prefix = prefix[:-1]

            if not prefix:
                return ""
    return prefix

print(longestCommonPrefic(["car","cir"]))
print(longestCommonPrefic(["abab","aba",""]))

