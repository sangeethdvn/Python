text = "abcbcdedf"

# unique = []

# for i in text:

#     if text.count(i) == 1:

#         unique.append(i)

# print(unique)

print([i for i in text if text.count(i) == 1])