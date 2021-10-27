n= int(input())
a=[]
for i in range(n):
    s= input().split(' ')
    if(s[0]=='insert'):
        a.insert(int(s[1]),int(s[2]))
    elif( s[0]=='print'):
        print(a)
    elif( s[0]=='remove'):
        a.remove(int(s[1]))
    elif(s[0]=='sort'):
        a=sorted(a)
    elif(s[0]=='append'):
        a.append(int(s[1]))
    elif(s[0]=='pop'):
        a.pop()
    elif(s[0]=='reverse'):
        a.reverse()
