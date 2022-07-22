with open("02_sample_1.txt") as f:
    content = f.read()

content = content.replace("donkey", "$%^@$^#")

with open("02_sample_1.txt", "w") as f:
    f.write(content)

