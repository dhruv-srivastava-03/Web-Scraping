import requests

url = 'https://0afa0042031f052ec05a811400400088.web-security-academy.net/filter?category=Toys+%26+Games'

proxy_servers = {
    'http': '127.0.0.1:8080',
    'https': '127.0.0.1:8080',
}

r = requests.get(url)

for i in r.headers:
    print(i+" : "+r.headers[i])

header = {
    "Set-Cookie" : "teri mummy"
}


r2 = requests.get(url,headers=header,proxies=proxy_servers,verify=False)

print(r2.headers)