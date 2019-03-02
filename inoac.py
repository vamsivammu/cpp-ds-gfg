input1= input().split(" ")

n= int(input1[0])
k= int(input1[1])
presid = input().split(" ")
presid.pop(0)
residents= []
for p in range(n-1):
    inp = input()
    a = inp.split(" ")    
    a.pop(0)
    residents.append(a)
# print(residents)

def checkrelation(pres,resident):
    # print(pres)
    # print(resident)
    checkedindexes=0
    for i in pres:
        # print(i)
        # print(binarysearch(resident,i))
        # print(checkedindexes)

        if binarysearch(resident,i):
            
            checkedindexes=checkedindexes+1
            # print(i,checkedindexes)
        if checkedindexes>=k:
            return True
        
    return False



def binarysearch(ar,elem):
    f =0
    l = len(ar)-1
    while f<=l:
        m = int((l+f)/2)
        if ar[m]==elem:
            return True
        elif ar[m]>elem:
            l = m-1
        else:
            f=m+1
    return False


def calculaterelations():
    presid.sort()
    stack =[]
    # print(presid)
   # remainingmem =[]
    numrel = 1
    for j in residents:
        j.sort()
        # print(j)
        # print(checkrelation(presid,j))
        if checkrelation(presid,j):
            numrel=numrel+1
            stack.append(j)
            residents.remove(j)
            # print(residents)
            
    while len(stack)>0:
        resi = stack.pop(0)
        for l in residents:
            if checkrelation(resi,l):
                numrel = numrel+1
                stack.append(l)
                residents.remove(l)
    
    print(numrel)

calculaterelations()
    
        
    


