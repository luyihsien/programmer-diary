from django.test import TestCase

# Create your tests here.
class Entity:
    def __init__(self, size, x, y):
        self.x, self.y = x, y
        self.size = size
    def __call__(self, x, y):
        self.x, self.y = x, y

e = Entity(1, 2, 3) #创建实例
print(e(4,5))#实例可以象函数那样执行，并传入x y值，修改对象的x y#None#可看成一個函數
print(e.x)#4#用在decorator
class a:
    x=3
print(a().x)
print(a.x)