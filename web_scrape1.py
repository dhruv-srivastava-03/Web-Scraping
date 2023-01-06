import requests
from bs4 import BeautifulSoup

# get the HTML

url = "https://www.vulnspy.com/dvwa/"

r = requests.get(url)

html_content = r.content

#print(html_content)

print("-"*100)

#parse the HTML

soup = BeautifulSoup(html_content,"html.parser")
#print(soup.prettify)


# Tree traverse the html
title = soup.title
print(title)

for i in soup:
    print(i)