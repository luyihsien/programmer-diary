class Entity:
    def __init__(self, size, x, y):
        self.x, self.y = x, y
        self.size = size
    def __call__(self, x, y):
        self.x, self.y = x, y

e = Entity(1, 2, 3) #创建实例
print(e(4,5))#实例可以象函数那样执行，并传入x y值，修改对象的x y#None
print(e.x)#4#用在decorator
class a:#等同class a():
    x=3
print(a().x)#3
print(a.x)#3
#python may_eleven.py在termianl是直譯一次
#python may_eleven.py shell反映如同沒打上shell
#https://www.udemy.com/30-days-of-python/learn/v4/t/lecture/4638946?start=0