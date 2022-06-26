u=[]
f=1
s=1
start = int(input("Enter start no: "))
end = int(input("Enter end no: "))
limit = int(input("Enter limit: "))
while start<end:
	start=f+s
	f=s
	s=start
	m=start
	divisor=2 
	while divisor<m:
		if m%divisor==0:
			break
		divisor+=1
	else:
		u.append(m)
print(u)
total=0
for i in u:
	total+=i
else:
	if total>limit:
		print("yes")
	else:
		print("no")

		
Enter start no: 2
Enter end no: 90
Enter limit: 100
[2, 3, 5, 13, 89]
yes

Enter start no: 2
Enter end no: 50
Enter limit: 100
[2, 3, 5, 13]
no