email = input("please input the email address: ")

try:
    email_split = email.split("@")
    username = email_split[0]
    print(username)
except Exception as e:
    print(f"something is wrong: {e}")
