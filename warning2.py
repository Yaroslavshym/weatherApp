import grequests
# import requests


urls = [f'https://dummyjson.com/products/{item}' for item in range(1, 101)]



responses = (grequests.get(url) for url in urls)

data = grequests.map(responses)
for i in data:
    print(i.status_code, i.json())