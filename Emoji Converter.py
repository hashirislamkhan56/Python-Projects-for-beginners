#Emoji Converter with dictionaries
message = input(">")
words = message.split(" ")
emojis= {
    ":)": "😁",
    ":(": "😒",
    "hrt": "❤️"

}
output=  ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)
