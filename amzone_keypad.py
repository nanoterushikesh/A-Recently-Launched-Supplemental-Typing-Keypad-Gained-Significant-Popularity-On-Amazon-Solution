a=input()
j=input()
b=[]
f=0
r=0
for i in range(0,len(a)):
    b.append(a[i])
    if (1+i)%3==0:
        b.append('#')
c=''.join(b)
n=c.split('#')
print(n)
for m,k in enumerate(j):
    for t in n:
        if k in t :
            r+=m+1
print(r)
        # else:
        #     print('no')
    




    


        

