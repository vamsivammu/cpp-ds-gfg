testcases = int(input())
alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","q","r","s","t","u","v","w","x","y","z"]
for i in range(testcases):
    inp = str(input())
    numarr=[]
    for lett in range(len(inp)):
        # print(lett)
        numarr.append(alphabets.index(inp[lett])+1)
    # print(numarr)
    for j in numarr:
        
