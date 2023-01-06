import requests


url = r"http://testphp.vulnweb.com/login.php"


proxy_servers = {
   'http': '127.0.0.1:8080',
   'https': '127.0.0.1:8080',
}
header ={
    'User-Agent': 'Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion',
    'Referer': 'https://google.com'
}
r = requests.get(url, proxies=proxy_servers)
print(r.headers)
print("-"*100)
#rh = requests.get(url, headers=header,proxies=proxy_servers)
#print(rh.headers)

