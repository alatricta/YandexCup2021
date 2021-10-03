import re

a = input()
b = input()


pattern = r"zero|one"
a1 = re.findall(pattern, a)
b1 = re.findall(pattern, b)

a2 = ""
for c in a1:
    if c == "zero":
        a2 += "0"
    elif c == "one":
        a2 += "1"

b2 = ""
for c in b1:
    if c == "zero":
        b2 += "0"
    elif c == "one":
        b2 += "1"

a = a2.encode(encoding="utf-8")
a = int(a2, 2)
b = int(b2, 2)

if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("=")
