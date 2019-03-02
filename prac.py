testcases = int(input())
for i in range(testcases):
    s = str(input())
    s = s.split(" ")
    n = int(s[0])
    req = int(s[1])
    arr = str(input())
    arr = arr.split(" ")
    maxsofar = 0
    maxending =0
    sindex =0
    eindex =-1
    for k in arr:
        maxending = maxending + int(k)
        eindex = eindex+1
        while req<maxending:
            maxending=maxending-int(arr[sindex])
            sindex=sindex+1
        if req==maxsofar:
            print(sindex,sep=" ")
            print(eindex)
            break    
        
       
