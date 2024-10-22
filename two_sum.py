l=list(map(int, input().split()))
t=int(input()) 
for i in range(0,len(l),1): 
    temp=t-l[i]
    for j in range(i+1,len(l),1):
        if l[j]==temp:
            print(i," ",j)
            break
