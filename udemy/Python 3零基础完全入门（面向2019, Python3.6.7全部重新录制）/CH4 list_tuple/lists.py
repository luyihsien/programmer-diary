#list:可容納不同type的元素 有max min方法 比數字 count方法傳數字出現頻率 .append(123)  123插尾
print(1,'2')#1 2 #1中間空格2不會error#print(1+'2')才會有問題
#第2講4:12繼續
#string無法改內值
list1=[1,2,3,4]
print(list1*2)
print(list1*2+[4,5,6])
print(list1+[1,2,3,4])#誤[2,4,6,8]#聯想 既然list1*2是[1,2,3,4,1,2,3,4]了，那加理應也是
print(list1+[1])