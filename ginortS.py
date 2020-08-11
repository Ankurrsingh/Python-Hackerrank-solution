#APPROACH 1

st=input()
su=''
so=''
sl=''
se=''
an=""
for i in range(len(st)):
    if st[i].isupper()==True:
        su=su+st[i]
    if (st[i].islower()==True):
        sl=sl+st[i]
    if (st[i].isdigit()==True):
        if(int(st[i])%2==0):
            so=so+st[i]
        else:
            se=se+st[i]

p=(sorted(sl)+sorted(su)+sorted(se)+sorted(so))
print(an.join(p))

#APPROACH 2 same as above but more relaible
l,u,o,e=[],[],[],[]
for i in sorted(input()):
    if i.isalpha():
        x = u if i.isupper() else l
    else:
        x = o if int(i)%2 else e
    x.append(i)
print("".join(l+u+o+e))
