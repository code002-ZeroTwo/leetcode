def isPalindrome(x):
    x = str(x)
    xlen = len(x) -1

    for i in range(len(x)):
        if x[i] == x[xlen]:
            xlen -= 1
        
        elif i == xlen:
            break
            
        else:
            return False
    
    return True


print(isPalindrome(-121))