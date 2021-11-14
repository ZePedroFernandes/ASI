import re

pattern = re.compile(r'^\d{8} \d [A-Z\d]{2}\d$', re.IGNORECASE)
print(pattern.search("12345678 1 AZ9"))

