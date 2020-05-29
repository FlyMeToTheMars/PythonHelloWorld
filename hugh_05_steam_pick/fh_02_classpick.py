import requests

class demo:
    def keywordgetbaidu(self):
        try:
            keyword = "Python"
            kv = {'wd': keyword}
            url = "http://www.baidu.com/s"
            r = requests.get(url, params=kv)
            status_code = r.status_code
            print(status_code)
            url = r.request.url
            print(url)
            status = r.raise_for_status()
            print(status)
            r.encoding = r.apparent_encoding
            print(r.text)
        except:
            print("爬取失败")

    def keywordget360(self):
        try:
            keyword = "Python"
            kv = {'q': keyword}
            url = "http://www.so.com/s"
            r = requests.get(url, params=kv)
            status_code = r.status_code
            print(status_code)
            url = r.request.url
            print(url)
            status = r.raise_for_status()
            print(status)
            r.encoding = r.apparent_encoding
            print(r.text)
        except:
            print("爬取失败")
