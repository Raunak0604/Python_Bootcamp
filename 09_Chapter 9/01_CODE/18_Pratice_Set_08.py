with open("19_Content.txt") as f:
    content = f.read()

with open("20_Copy.txt", 'w') as f:
    f.write(content)