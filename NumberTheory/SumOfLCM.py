## Read input as specified in the question.
## Print output as specified in the question.
def gcd(a,b):
    if a == 0:
        return b
    return gcd(b % a, a)
 
# Function to return LCM of two numbers
def lcm(a,b):
    return int((a / gcd(a,b))* b)

n=int(input())
res=0
for i in range(1,n+1):
    res+=lcm(i,n)
print(res)