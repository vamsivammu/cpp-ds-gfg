input1= input().split(" ")

n= int(input1[0])
k= int(input1[1])
presid = input().split(" ")
residents= []
for p in range(n-1):
    inp = input()
    a = inp.split(" ")    
  
    residents.append(a)

def checkrelation(pres,resident):

    checkedindexes=0
    for i in pres:
        if checkedindexes>=k:

            return True
        
        elif binarysearch(resident,i):
            checkedindexes=checkedindexes+1
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
   # remainingmem =[]
    numrel = 1
    for j in residents:
        j.sort()
        if checkrelation(presid,j):
            numrel=numrel+1
            stack.append(j)
            residents.remove(j)
            
    while len(stack)>0:
        resi = stack.pop()
        for l in residents:
            if checkrelation(resi,l):
                numrel = numrel+1
                stack.append(l)
                residents.remove(l)
    
    print(numrel)

calculaterelations()
    
        
    


