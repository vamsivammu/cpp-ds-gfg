#permutation

letters=["a","b","c","d"]

permutations=[]
for k in letters:
    permutations.append(0)
p=[]
def containsalready(sp,l):
    for o in range(sp):
        if permutations[o]==l:
            return True
    
    return False
        

def printall(startpos):
    if startpos>len(letters)-1:
        seq = ""
        for i in permutations:
            seq = seq+i
        p.append(seq)
        
        return
    for j in letters:
        if containsalready(startpos,j):
            continue
        permutations[startpos]=j
        printall(startpos+1)

printall(0)

print(len(p))

