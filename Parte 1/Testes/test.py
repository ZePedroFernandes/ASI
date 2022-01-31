import re

string = "Jose Antonio;22;M;961237272"

pattern = re.compile(r'(.*);(\d{9})$')

result = pattern.match(string)

print(result.group(2))

newString = pattern.sub(r'\1;00351\2', string)

print(newString)
