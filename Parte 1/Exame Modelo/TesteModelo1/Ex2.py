import re

data = "2016/02/21 23:43:01"
data2 = "02/20"

pattern = re.compile(r'\d+/(((01|03|05|07|08|10|12)/(0[1-9]|1[0-9]|2[0-9]|3[0-1]))|((02)/(0[1-9]|1[0-9]|2[0-9]))|((04|06|09|11)/(0[1-9]|1[0-9]|2[0-9]|30))) ([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]')

pattern2 = re.compile(r'((01|03|05|07|08|10|12)/(0[1-9]|1[0-9]|2[0-9]|3[0-1]))|((02)/(0[1-9]|1[0-9]|2[0-9]))|((04|06|09|11)/(0[1-9]|1[0-9]|2[0-9]|30))')
print(pattern2.search(data2))

if pattern.match(data):
    print("Data válida")
else:
    print("Data inválida")
