import re

# ? ==> to check if it is at the beginnig

txt = "+91 89211492925"

pattern = r"^(?:\+91|91)\s?[6789][0-9]{9}$"     # ? ==> to check if it is at the beginnig(zero or more occurence)

res = re.match(pattern, txt)

print("Valid" if res else "Invalid")

"""

[6789] means:

The number must start with 6, 7, 8, or 9.

================================================================

 (Question Mark)
It just means "optional."
Whatever comes before it can be there or not.
Example: a? means "there might be an 'a', but it's okay if it's not there."
\s? means "there might be a space, but it's fine if there isn't one."


(?:\+91|91)

means begins with either +91 or 91

================================================================







"""