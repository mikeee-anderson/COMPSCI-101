text = input("Enter your text: ")
html_list = []
html = ""
opening_html = False
for char in text:
    if char == ">":
        html_list += [html]
        html = ""
        opening_html = False
    if opening_html == True:
        html += char
    if char == "<":
        opening_html = True

print(f"List of HTML tags: {html_list}")
