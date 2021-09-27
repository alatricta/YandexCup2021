import requests

arg1 = input()
arg2 = input()
arg3 = input()
arg4 = input()
args = f"{arg1}, {arg2}, {arg3}, {arg4}"

Metod = "MEW"
URL = "http://127.0.0.1:7777/"

Headers = {"X-Cat-Variable": arg1+", "+arg2}

req = requests.Request(Metod, url=URL, headers=Headers).prepare()

s = requests.Session()

r = s.send(req)
ans1 = r.headers["X-Cat-Value"].split(", ")

req.headers["X-Cat-Variable"] = arg2+", "+arg3 
r = s.send(req)
ans2 = r.headers["X-Cat-Value"].split(", ") 

req.headers["X-Cat-Variable"] = arg3+", "+arg4
r = s.send(req)
ans3 = r.headers["X-Cat-Value"].split(", ")



ans = [0 for i in range(4)]
if ans1[0] in ans2:
	ans[1]=ans1[0].strip()
	ans[0]=ans1[1].strip()
else:
	ans[1]=ans1[1].strip()
	ans[0]=ans1[0].strip()
		
if ans3[0] in ans2:
	ans[2]=ans3[0].strip()
	ans[3]=ans3[1].strip()
else:
	ans[2]=ans3[1].strip()
	ans[3]=ans3[0].strip()



for a in ans:
	print(a)