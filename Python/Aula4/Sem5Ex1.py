import re

cc = "12345678 1 ZY1"

pattern = re.compile(r'\d{8} \d [A-Z0-1]{2}\d', re.I)

if pattern.match(cc):
    print("Match")
else:
    print("Not Match")
