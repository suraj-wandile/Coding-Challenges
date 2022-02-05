
def isPalindrome(s):
    lens = len(s)
    for i in range(int(lens/2)):
        if s[i] != s[lens - i - 1]:
            return False
    return True


s = input()
ans = isPalindrome(s)

if ans == True:
    print("Yes")
else:
    print("No")
