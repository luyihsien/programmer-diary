'''
    Ptt Crawler 記得要pip install下載import的套件與網路下載webdriver去啟動瀏覽器
'''
import os
import time
from bs4 import BeautifulSoup
from selenium import webdriver


def make_path(post_type):
    '''
    建立檔案路徑
    :param post_type:
    :return:
    '''
    posts_path = os.path.join(os.getcwd(), post_type)
    if not os.path.isdir(posts_path):
        os.mkdir(posts_path)
    return posts_path

def save_data(posts_path, post_info):
    '''
    存入檔案
    :param posts_path:
    :param post_info:
    :return:
    '''
    file_path = posts_path + "/" + str(post_info["title"])[2:-2] + ".txt"
    with open(file_path, "w") as f:
        for key, value in post_info.items():
            print(str(key) + " : " + str(value)[2:-2], file=f)

def ptt_crawler(base_url, post_type, url):
    '''
    執行爬蟲
    :param base_url:
    :param post_type:
    :param url:
    :return:
    '''
    # 建立存擋路徑
    posts_path = make_path(post_type)
    # chromedriver.exe 執行檔所存在的路徑
    chromedriver_path = "{0}/chromedriver".format(os.getcwd())
    # 使用webdriver開啟網頁
    options = webdriver.ChromeOptions()
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")
    # 使用Chrome作為webdriver(須引入chromedriver.exe所在的路徑)
    driver = webdriver.Chrome(chromedriver_path,
                              chrome_options=options)
    driver.implicitly_wait(3)
    driver.get(url)
    # 等候網頁載入
    time.sleep(1)

    # 點擊滿18歲頁面
    if driver.current_url != url:
        driver.find_element_by_css_selector(".btn-big").click()  # 點擊彈出視窗

    # 取得個文章區塊
    main_html = driver.execute_script("return document.documentElement.outerHTML")
    main_soup = BeautifulSoup(main_html, "html.parser")
    posts = main_soup.findAll("div", {"class": "r-ent"})
    # 取得個文章資訊
    for post in posts:
        try:
            # a標籤是否存在
            url_link = post.find("a")["href"]
        except:
            continue
        post_url = base_url + url_link
        print(post_url)
        driver.get(post_url)
        post_html = driver.execute_script("return document.documentElement.outerHTML")
        post_soup = BeautifulSoup(post_html, "html.parser")
        metas = post_soup.select(".article-meta-value")
        main_content = post_soup.find("div", {"class": "bbs-screen bbs-content"}).text.strip()
        if metas:
            post_info = {
                "auther": metas[0].contents,
                "board": metas[1].contents,
                "title": metas[2].contents,
                "date": metas[3].contents,
                "content": main_content
            }
            print(post_info)
        if post_info:
            save_data(posts_path, post_info)
    driver.close()


if __name__ == "__main__":

    # 網址
    base_url = "https://www.ptt.cc"
    post_type = "nba"
    url = base_url + "/bbs/" + post_type + "/index.html"

    # 執行爬蟲
    ptt_crawler(base_url, post_type, url)