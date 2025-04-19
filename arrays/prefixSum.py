def prefixSum(listArray:list)->list:
    ps=[]
    cumsum=0
    n=len(listArray)
    for i in range(0, n):
        cumsum+=listArray[i]
        ps.append(cumsum)
    
    return ps

def prefixSumBtnIdx(A:list, s:int, e:int)->list:
    # first build the prefix sum array
    prefixSumArray=prefixSum(A)
    return prefixSumArray[e]-(prefixSumArray[s-1] if s>0 else 0)
    
    

def eqIndex(A:list):
    ps=prefixSum(A)
    n=len(ps)
    for i in range(n):
        
        sl=ps[i-1] if i>0 else 0
        sr=ps[n-1]-ps[i]

        if sl==sr:
            return i
    
    return "No Eq Index found"
    

            



def main():
    print(eqIndex([-7,2,5,2,-4,3,0]))

if __name__=="__main__":
    main()