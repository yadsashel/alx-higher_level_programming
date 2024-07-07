#!/usr/bin/python3
# A pyhton script that fetchs "https://alx-intranet.hbtn.io/status"

import urllib.request

url = 'https://alx-intranet.hbtn.io/status'
with urllib.request.urlopen(url) as responce:
    html = responce.read()

print("Body responce:")
print("\t- type:", type(html))
print("\t- content:", html)
print("\t- utf8 content:", html.decode('utf-8'))
