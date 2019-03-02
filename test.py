
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

a = ['1','2','3','4','5','6']
print(binarysearch(a,'7'))
