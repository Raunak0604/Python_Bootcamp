def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

this = "     Rabbit is a good      "
n = remove_and_split(this, "Rabbit")
print(n)

# print(this)
# print(this.strip())
