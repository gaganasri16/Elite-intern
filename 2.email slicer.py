
def email_slicer():
    print("Welcome to the Email Slicer!")
    email = input("Enter your email address: ").strip()

    if "@" in email and "." in email:  
        username, domain = email.split("@")
        print(f"Username: {username}")
        print(f"Domain: {domain}")
    else:
        print("Invalid email address. Please try again.")

if __name__ == "__main__":
    email_slicer()
    
