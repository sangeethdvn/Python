"""
Write a function  that reverses the order of words in a given sentence but keeps the characters in each word in the correct order.
Example: "Hello World" → "World Hello"

"""

def rev(sen):

    revsen = " "

    for i in sen.split(" ")[::-1]:

        revsen = revsen + i + " "

    return (revsen.strip())

sentence = input("Sentence please: ")

print(rev(sentence))