from os import *
def counting(urls):
    dict = {}
    for i in range(len(urls)):
        urls[i]=urls[i].split('/',-1)[-1]

    return urls

'''    
    for i in urls:
        #dict={}
        if i in dict:
            dict[i]=dict[i]+1
        else:
            dict[i]=1
    return dict

'''
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

print(counting(urls))