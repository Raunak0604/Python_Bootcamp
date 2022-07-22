words = ["donkey", "kaddu", "mote"]

with open("02_sample_1.txt") as f:
    content = f.read()


for word in words:
    content = content.replace(word, "$%^@$^#")
    with open("02_sample_1.txt", "w") as f:
        f.write(content)

