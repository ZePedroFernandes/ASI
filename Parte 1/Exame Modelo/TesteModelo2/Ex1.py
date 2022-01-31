import re

inputStr = "jpm@estgf.ipp.pt,mmo@aulas.pt,abc@gmail.com,abd@gmail.com"

pattern = re.compile(r'(.+),(.+),(.+),(.+)')
result = pattern.match(inputStr)

myfile = open("fich.txt","w+")

print(result.group(1), file=myfile)
print(result.group(2), file=myfile)
print(result.group(3), file=myfile)
print(result.group(4), file=myfile)
