t = int(input())
res=[]
for i in range(t):
    k =int(input().split(" ")[1])
    # print(k)
    nums = input().split(" ")
    # print(nums)
    req =0
    for n in nums:
        # print(req)
        if n!="1":
            req = req+1
        if req>k:
            res.append("NO")
            break
            # print(len(res))
    if req<=k:
        res.append("YES")
        
     

for r in res:
    print(r)

            
