# wap to read a file and  read the content. it should handle the exception

# new.txt    sample.txt      ==> filenotfoundeerror

try:

    file = open("abc.txt", "r")

    result = file.read()

    print(result)

except FileNotFoundError:

    print("File not found")
