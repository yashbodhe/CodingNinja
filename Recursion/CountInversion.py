from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def merge(a1, a2):
    swaps, i, j, result, m, n = 0, 0, 0, [], len(a1), len(a2)
    ra = result.append
    while i < m and j < n:
        if a1[i] <= a2[j]:
            ra(a1[i])
            i += 1
        else:
            ra(a2[j])
            j += 1
            swaps += m - i
    result += a1[i:]
    result += a2[j:]    
    return swaps, result
    
def msort(arr):
    n = len(arr)
    mid = n // 2
    if n > 1:
        left_swaps, left_result = msort(arr[:mid])
        right_swaps, right_result = msort(arr[mid:])
        m_swaps, result = merge(left_result, right_result)
        return m_swaps + left_swaps + right_swaps, result
    return 0, arr

def getInversions(arr, n) :
    res,arr=msort(arr)
    return res

#taking inpit using fast I/O
def takeInput() :
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


#main
arr, n = takeInput()
print(getInversions(arr, n))