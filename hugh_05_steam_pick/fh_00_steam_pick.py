import requests

r = requests.get("https://www.amazon.cn/dp/B073XFGC7K?ref_=Oct_DLandingS_D_a55db1a6_60&smid=A26HDXW89ZT98L")
print(r.status_code)
r.encoding = r.apparent_encoding
print(r.request.headers)
print(r.text)

kv = {'User-Agent': 'Mozilla/5.0'}
