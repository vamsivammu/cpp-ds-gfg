def checkreq(o):
	if o in req:
		print("YES")
	else:
		print("NO")
a = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
semiprimes=[]
req=[]

for i in range(25):
	for j in range(i+1,25):
		p = a[i]*a[j]
		if p<=200:
			semiprimes.append(p)
		
for k in semiprimes:
	for l in semiprimes:
		m = k+l
		if m<=200:
			req.append(m)
nums=[]
t = int(input())
for u in range(t):
	nums.append(int(input()))

for num in nums:
	checkreq(num)

        
