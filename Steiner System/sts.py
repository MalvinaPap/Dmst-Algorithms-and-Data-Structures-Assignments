import sys
import random
import itertools

u=int(sys.argv[1])

D=[]
c=u*(u-1)/6




while c>0:

    objs=list(range(1,u+1))

    # pick a random element  x
    x=random.randrange(1,u+1)
    #check how many times x appears in D
    ap=0
    for i in D:
        if x in i:
            ap=ap+1
    if ap>=(u-1)/2:
        continue
    objs.remove(x)



    for y in range(1,u+1):
        if y not in objs:
            continue
        counter=0
        for block in D:
            if (x in block) and (y in block):
                break
            counter=counter+1
        if counter==len(D):
            break

    objs.remove(y)

    for z in range(1,u+1):
        if z not in objs:
            continue
        counter=0
        for block in D:
            if (x in block) and (z in block):
                break
            counter=counter+1
        if counter==len(D):
            break



    for w in range(1,u+1):
        if (y,z,w) in D:
            D.remove((y,z,w))
            c=c+1
            break
        if (y,w,z) in D:
            D.remove((y,w,z))
            c=c+1
            break
        if (z,y,w) in D:
            D.remove((z,y,w))
            c=c+1
            break
        if (z,w,y) in D:
            D.remove((z,w,y))
            c=c+1
            break
        if (w,z,y) in D:
            D.remove((w,z,y))
            c=c+1
            break
        if (w,y,z) in D:
            D.remove((w,y,z))
            c=c+1
            break



    D.append((x,y,z))
    c=c-1

#end of while

hlpD=[]
for block in D:
    block=sorted(block)
    hlpD.append((block[0],block[1],block[2]))


finalD=sorted(hlpD)

print(finalD)
print(len(D))
