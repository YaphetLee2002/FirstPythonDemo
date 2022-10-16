 import requests
res = requests.get("https://movie.douban.com/top250")
print(res.text)