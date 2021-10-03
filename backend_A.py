import requests

args = []
for i in range(4):
    a = input().strip()
    if a not in args:
        args.append(a)

Metod = "MEW"
URL = "http://127.0.0.1:7777/"


#req = requests.Request(Metod, url=URL, headers=Headers).prepare()
s = requests.Session()
req = requests.Request(Metod, url=URL, headers={"X-Cat-Variable": ""}).prepare()
#Headers = {"X-Cat-Variable": ""}
ans = []
if len(args)>3:
    req.headers["X-Cat-Variable"] = ", ".join(args[0:2])
    r = s.send(req)
    ans1 = r.headers["X-Cat-Value"].split(", ")
    
    req.headers["X-Cat-Variable"] = ", ".join(args[1:3]) 
    r = s.send(req)
    ans2 = r.headers["X-Cat-Value"].split(", ") 
    
    req.headers["X-Cat-Variable"] = ", ".join(args[2:4])
    r = s.send(req)
    ans3 = r.headers["X-Cat-Value"].split(", ")

    if ans1[0] in ans2:
    	ans.append(ans1[1].strip())
    	ans.append(ans1[0].strip())
    else:
    	ans.append(ans1[0].strip())
    	ans.append(ans1[1].strip())
    		
    if ans3[0] in ans2:
    	ans.append(ans3[0].strip())
    	ans.append(ans3[1].strip())
    else:
    	ans.append(ans3[1].strip())
    	ans.append(ans3[0].strip())
    	
else:
    for arg in args:
        req.headers["X-Cat-Variable"] = arg
        r = s.send(req)
        ans.append( r.headers["X-Cat-Value"].strip() )


for a in ans:
    print(a)
