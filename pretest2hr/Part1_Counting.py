def counting(urls):
    dict = {}
    for i in range(len(urls)):
        urls[i]=urls[i].split('/',-1)[-1]#能切割'/'的最多次數的最後一項
    for i in urls:
        if i in dict:
            dict[i]=dict[i]+1
        else:
            dict[i]=1
    #此時dict={'a.txt': 3, 'c.jpg': 2, 'b.txt': 2, 'haha.png': 1}
    b=[]
    c=[]
    for i in range(3):
        a=max(dict,key=dict.get)
        b.append(a)
        c.append(dict[a])
        dict.pop(a)
    b.sort()
    for i in range(3):
        print(b[i],c[i])
if __name__ == '__main__':
    urls = [
        "http://www.google.com/a.txt",
        "http://www.google.com.tw/a.txt",
        "http://www.google.com/download/c.jpg",
        "http://www.google.co.jp/a.txt",
        "http://www.google.com/b.txt",
        "https://facebook.com/movie/b.txt",
        "http://yahoo.com/123/000/c.jpg",
        "http://gliacloud.com/haha.png",
    ]

counting(urls)