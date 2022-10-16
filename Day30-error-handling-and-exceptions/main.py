try:
    file = open("a_file.text")
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("New file")
else:
    content = file.read()
    print(content)
finally:
    raise TypeError("This is a made up error")