def isPalindrome(x: int):
    list = []
    while x != 0:
        digit = x%10
        list.append(digit)
        x = int(x/10)
    print(list)
    l2 = list.copy()
    list.reverse()
    return list == l2




    """s = str(x)
    #l1=[]
    #for i in range (len(s)):
     #   l1.append(s[i])
    l1 = list(s)
    print(l1)
    l2=l1.copy()
    l1.reverse()
    print(l2)
    if l1==l2:
        return True
    else:
        return False
"""


print(isPalindrome(1212121))