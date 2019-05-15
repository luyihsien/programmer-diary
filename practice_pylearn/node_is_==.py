#啟發from Leetcode的reverse LinkedList#是指向自己還是有一個新的值相同的記憶體??
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
a=Node(1000000000)
b=a#True
print(a is b)
a=1000000000
b=a#True
print(a is b)

a=10000000000000000000
b=10000000000000000000
#True
print(a is b)
