## Read input as specified in the question.
## Print output as specified in the question.
dp = [0 for i in range(200)] 
def print1(idx):
    res=[]
    for i in range(1,idx,1): 
        res.append(dp[i]) 
    res.sort()
    print(*res) 

def solve(remSum,maxVal,idx):
    if (remSum == 0): 
        print1(idx) 
        return
    i = maxVal
    while(i >= 1): 
        if (i > remSum): 
            i -= 1
            continue
        else: 
            dp[idx] = i 
            solve(remSum - i, i, idx + 1) 
            i -= 1
            
if __name__=="__main__":
    n=int(input())
    solve(n, n, 1)
        