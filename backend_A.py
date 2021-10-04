import requests

input_ = []  # всё что получили
args = []   # уникальные входные данные
for i in range(4):
    a = input().strip()
    input_.append(a)
    if a not in args:
        args.append(a)

Metod = "MEW"
URL = "http://127.0.0.1:7777/"

s = requests.Session()
req = requests.Request(Metod, url=URL, headers={"X-Cat-Variable": ""}).prepare()

##ans = []
ans = {}
if len(args) > 3:
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
        ans[input_[0]] = ans1[1].strip()
        ans[input_[1]] = ans1[0].strip()
# ans.append(ans1[1].strip())
# ans.append(ans1[0].strip())
    else:
        ans[input_[0]] = ans1[0].strip()
        ans[input_[1]] = ans1[1].strip()
# ans.append(ans1[0].strip())
# ans.append(ans1[1].strip())

    if ans3[0] in ans2:
        ans[input_[2]] = ans3[0].strip()
        ans[input_[3]] = ans3[1].strip()
# ans.append(ans3[0].strip())
# ans.append(ans3[1].strip())
    else:
        ans[input_[2]] = ans3[1].strip()
        ans[input_[3]] = ans3[0].strip()
# ans.append(ans3[1].strip())
# ans.append(ans3[0].strip())

else:
    for arg in args:
        req.headers["X-Cat-Variable"] = arg
        r = s.send(req)
        ans[arg] = r.headers["X-Cat-Value"].strip()


for a in input_:
    print(ans[a])
