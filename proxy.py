import requests


url = "https://0a4000b1045dd92bc0640e2000a8009a.web-security-academy.net/filter?category=Tech+gifts"

proxy_servers = {
 'http': '127.0.0.1:8080',
 'https': '127.0.0.1:8080',
}

r = requests.get(url,proxies=proxy_servers,verify=False)
print(r.headers)

rh = requests.get(url,proxies=proxy_servers)
print(rh.headers)
