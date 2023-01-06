import requests


url="https://0a0f007204d2a2b3c07e276200a200a0.web-security-academy.net/filter?category=Tech+gifts"


#proxy_servers = {
 #  'http': '127.0.0.1:8080',
  # 'https': '127.0.0.1:8080',
#}
header ={
    'User-Agent': 'Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion',
    'Referer': 'https://google.com'
}
r = requests.get(url)
print(r.headers)
print("-"*100)
rh = requests.get(url, headers=header)
print(rh.headers)

