"""
Username,
Can contain only letters (a-z, A-Z), digits (0-9), and underscores (_).
Must start with a letter.
Length should be between 4 to 15 characters.


"""
import re

txt = "sang"

print(len(txt))


pattern = r"^[a-zA-Z][a-zA-Z0-9_]{3,14}$"   # one letter must so 3 is the rest since 4 is minimum

                                            # another way r"^[A-z][A-z0-9_]{3,14}$"

res = re.match(pattern, txt)

print("Valid" if res else "Invalid")
