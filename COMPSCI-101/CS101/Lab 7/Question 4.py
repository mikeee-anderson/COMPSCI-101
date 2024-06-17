password = input("Please enter your password: ")
password = password.strip()
count = 0
number_count = 0
digit = 0
char = 0
if len(password) >= 10:
    if "abc" in password or "123" in password:
        print("Your password is invalid!")
    else:
        counter = 0
        while counter < len(password):
            index = password[counter]
            if index.isdigit() == True:
                char += 1
            elif index.isalpha() == True:
                digit += 1
            counter += 1
        if char >= 5:
            if digit >= 4:
                print("Your password is valid!")
            else:
                print("Your password is invalid!")
        else:
            print("Your password is invalid!")
else:
     print("Your password is invalid!")



