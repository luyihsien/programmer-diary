def calculate(n):
    a=(range(1,n+1))
    l=[]
    for i in a:
        if i%3!=0 and i%5!=0:
            l.append(i)
        if i%15==0:
            l.append(i)
    print(l)
    return len(l)
print(calculate(15))
