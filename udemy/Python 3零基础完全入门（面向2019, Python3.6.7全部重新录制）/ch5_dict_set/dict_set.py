#https://stackoverflow.com/questions/18552001/accessing-dict-keys-element-by-index-in-python3
#dict底層是hash table，記得每項之間加逗號#key不可改，value可以
a={
    1:'a',#[1]則TypeError: unhashable type: 'list'#不等有人呼叫此座標就會報錯了，不像函數，呼叫才知道
    2:'b',
    '3':'c'
}

'''
#不可改的數據類型
if 'a' in a:# if XXX in 某dictionary 只讀key不讀value
    print('a')
print('None')
a['3']='d'
print(a['3'])#d
print(a.get(1))#a #若key不存在dict內則回傳None，若是用a[XXX]但XXX非key則報錯
'''
print(a.keys(),type(a.keys()))#dict_keys([1, 2, '3']) <class 'dict_keys'>
#dict.keys() method returns a dictionary view object, which acts as a set.
'''
test = {'foo': 'bar', 'hello': 'world'}
keys = test.keys()  # dict_keys object

keys.index(0)
AttributeError: 'dict_keys' object has no attribute 'index'
keys[0]
TypeError: 'dict_keys' object does not support indexing
'''
'''
正解 
>>> test = {'foo': 'bar', 'hello': 'world'}
>>> list(test)
['foo', 'hello']
>>> list(test)[0]
'foo'
'''
'''
print(type(a.pop(1)))#<class 'str'>
#print(a.pop())#TypeError: pop expected at least 1 arguments, got 0 argument
#print(type(a.pop(1)))#第二次pop已經沒值了??顧error??對，因為這樣又會去找一次key為1的key與對應的value，試圖刪除，找到就刪找不到就error#<誤>以為只刪key對應的value而1對至None
print(a)#{2: 'b', '3': 'c'}
'''
c=a.pop(1)
print(c)#因為傳回了value了，即return，不是再次呼叫函數
print(c)
print(type(c))
