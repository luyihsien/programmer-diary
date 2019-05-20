def calculate(n):
    a=list(range(1,n+1))
    print(a)
    i=0
    while a[i]!=n:
        if a[i]%3==0 or a[i]%5==0:
            a.remove(a[i])
        if a[i]%15==0:
            a.insert(i,a[i])
        i=i+1
    print(a)
    return len(a)
print(calculate(15))
