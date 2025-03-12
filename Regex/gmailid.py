import re

txt = "abc123.ab@gmail.com"

pattern = r"^[A-Za-z0-9.-_]+gmail.com$"  #| r"^[A-Za-z][0-9.-_]+gmail.com$"

res = re.match(pattern, txt)

print("Valid" if res else "Invalid")