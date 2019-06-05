'''
def calculate(n):
    a=list(range(1,n+1))
    print(a)
    i=0
    while a[i]!=n:
        if a[i]%3==0 or a[i]%5==0:
            #print(str(a[i])+'是3or5倍數')
            a.remove(a[i])
            print(a)
        if a[i]%15==0:
            a.insert(i,a[i])
            print(a)

        i=i+1
        print(i)
    print(a)
    return len(a)
calculate(15)
'''

'''
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
'''
def cal(n):
    l=[]
    for i in range(1,n+1):
        if i%3!=0 and i%5!=0:
            l.append(i)
        elif i%15==0:
            l.append(i)
    print(l)

cal(15)


