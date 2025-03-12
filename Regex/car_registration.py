import re

txt = "kl 31 at 0707"

# kl\s[0-9]{2}\s[a-z]{1,2}\s[0-9]{4}

pattern = r"^kl\s[0-9]{2}\s[a-z]{1,2}\s[0-9]{4}$"     # r The r in r"^kl\s[0-9]{2}\s[a-z]{1,2}\s[0-9]{4}$" stands for raw string literal in Python. When you use a raw string, Python treats the backslashes (\) in the string as literal characters instead of escape characters.
                                                      # adding the ^ and $ anchors This ensures that the entire string must match the pattern from start to end.
result = re.match(pattern,txt)

if result:

    print("VAlidated")

else:

    print("Not vali")