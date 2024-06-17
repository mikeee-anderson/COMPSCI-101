text = input("Enter the text: ")

new_text = ""
a_count = 0
e_count = 0
i_count = 0
o_count = 0
u_count = 0
for char in text:
    if char == "A" or char == "a":
        a_count += 1
    elif char == "E" or char == "e":
        e_count += 1
    elif char == "I" or char == "i":
        i_count += 1
    elif char == "O" or char == "o":
        o_count += 1
    elif char == "U" or char == "u":
        u_count += 1
    else:
        new_text += char
if a_count > 0:
    print(f"'a' appears {a_count} times.")
if e_count > 0:
    print(f"'e' appears {e_count} times.")
if i_count > 0:
    print(f"'i' appears {i_count} times.")
if o_count > 0:
    print(f"'o' appears {o_count} times.")
if u_count > 0:
    print(f"'u' appears {u_count} times.")
print(f"Without vowels the text is: {new_text}")

