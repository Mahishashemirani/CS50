def convert(x):
    icon2emoji = {":)" : "🙂", ":(" : "🙁"}
    for icon , emoji in icon2emoji.items():
        x = x.replace(icon , emoji)
    return x
y = input("enter the sentence: ")
z = convert(y)
print(z)
