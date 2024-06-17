text = input("Enter your text: ")
vowels = "aeiouAEIOU"

for i in text:
    if i not in vowels:
        print(i, end="")
