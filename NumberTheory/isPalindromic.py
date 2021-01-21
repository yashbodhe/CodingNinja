## Read input as specified in the question.
## Print output as specified in the question.
def isPalindrome(s):
    return s==s[::-1]
n=int(input())
for i in range(1,n+1):
    if isPalindrome(str(i)):
        print(i)