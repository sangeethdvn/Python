text = "hellopython"

i = 0

a=" "

while i < len(text):

    if text[i] in "aeiou" and text[i] not in a:
         
         print(f"{text[i]} is a vowel and the count is {text.count(text[i])}")
         
         a = a + text[i]

    i += 1