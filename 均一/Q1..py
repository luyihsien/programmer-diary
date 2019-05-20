# 1(a)小題
def f1(string):
    a=string[::-1]
    return a
print(f1('junyiacademy'))
# 1(b)小題
def f2(string):
    a=string.split(' ',-1)
    #print(a)
    c=[]
    for i in a:
        i=i[::-1]
        c.append(i)
    str=' '
    b=str.join(c)
    print(b)
f2('flipped class room is important')
