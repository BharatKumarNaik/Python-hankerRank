n=int(input())
b=[]
dic ={ }
for i in range(n):
    a= input().split(' ')
    b=a[0]
    a.remove(b)
    dic[b]= a
    #print(dic)
f=input()
s=dic[f]
result=0
for i in range(len(s)):
    result=result+float(s[i])
print("%.2f" %(result/len(s)))
