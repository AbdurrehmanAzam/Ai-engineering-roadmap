gmail = input("Enter your Gmail : ")
check_symbol = gmail.count("@")

if check_symbol != 1:
    print("Invalid format: A Gmail address must contain exactly one '@' symbol.")
elif gmail == "abdurrehmanazam300@gmail.com":
    print("Your entered gmail is correct now enter your password : ")
    password = input("(password tries 1 of 2)=> ")

    if password == "1234":
        print("Welcome")
    else:
        print("Incorrect password Enter your password again : ")
        password = input("(password tries 2 of 2)=> ")

        if password == "1234":
            print("Welcome")
        else:
            print("All tries have been exhausted")
else:
    print("Email not found in our system.")
