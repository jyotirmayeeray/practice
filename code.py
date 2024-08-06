n=int(input())
if n>1:
    for fact in range(2,n//2+1):
        if n%fact==0:
            print(n," not Prime")
            break
    else:
        print(n," Prime")
else:
    print(n,"is Not Prime")
