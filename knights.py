testcases = int(input())
def isvalid(x,y):
    if x<0 or x>10^9 or y<0 or y>10^9:
        return False
    else:
        return True
def generatesteps(kpos):
    allmoves=[[kpos[0]+1,kpos[1]+1],[kpos[0]-1,kpos[1]+1],[kpos[0]+1,kpos[1]-1],[kpos[0],kpos[1]-1],[kpos[0],kpos[1]+1],[kpos[0]+1,kpos[1]],[kpos[0]-1,kpos[1]],[kpos[0]-1,kpos[1]-1]]
    for m in allmoves:
        if isvalid(m[0],m[1]) and not ischeck(m):
            return True
    
    else:
        return False

def ischeck(kpos):
    for knpos in kpositions:
        xk = int(kpos[0])
        yk = int(kpos[1])
        xkn = int(knpos[0])
        ykn = int(knpos[1])
        if xkn==xk or ykn==yk:
            continue
        elif abs(xkn-xk)>2 or abs(ykn-yk)>2:
            continue
        elif abs(xkn-xk)==1 and abs(ykn-yk)==1:
            continue
        else:
            return True
    return False
for i in range(testcases):
    moves=[]
    kpositions =[]
    n = int(input())
    for j in range(n):
        move = input().split(" ")
        x1 = int(move[0])
        y1 = int(move[1])
        pos= [x1,y1]
        # print(pos)
        kpositions.append(move)
    
    movek = input().split(" ")
    p = int(movek[0])
    q = int(movek[1])
    kingpos=[p,q]
    # print(kingpos)
    if ischeck(kingpos):
        if generatesteps(kingpos):
            print("NO")
            exit
        else:
             print("YES")
    else:
        print("NO")
  
