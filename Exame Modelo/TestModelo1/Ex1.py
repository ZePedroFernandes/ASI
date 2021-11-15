import re

ip = "192.168.1.0/24"
pattern = re.compile(r'\d{1,3}(.\d{1,3}){3}/\d{1,2}')

if pattern.match(ip):
    print("Bem formatado!")
