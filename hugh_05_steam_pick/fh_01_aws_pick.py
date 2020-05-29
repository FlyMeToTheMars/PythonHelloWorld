import requests

url = "https://www.amazon.cn/dp/B073XFGC7K?ref_=Oct_DLandingS_D_a55db1a6_60&smid=A26HDXW89ZT98L"
try:
    kv = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=kv)
    print(r.status_code)
    r.encoding = r.apparent_encoding
    print(r.request.headers)
    print(r.text[:1000])
except:
    print("爬取失败")
