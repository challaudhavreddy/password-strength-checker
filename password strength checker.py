import re
def check_password_strength(password):
    length_error=len(password)<6
    digit_error=re.search(r"\d",password)is None
    uppercase_error=re.search(r"[A-Z]",password)is None
    lowercase_error=re.search(r"[a-z]",password)is None
    specialcharacter_error=re.search(r"[!@#$%^&*()_+]",password)is None
    error=[]
    if length_error:
        print("your password must be atleast 6 letters")
        error.append("length")
    if digit_error:
        print("your password should contain atleast one digit")
        error.append("digit")
    if uppercase_error:
        print("your password mmust conatain atleast one uppercase letter")
        error.append("uppercase")
    if lowercase_error:
        print("your password contain atleast one lowercase letter")
        error.append("lowercase")
    if specialcharacter_error:
        print("your password contain atleast one special character")
        error.append("specialcharacter")
    if not error:
        strength="strong level password"
    elif len(error)<=2:
        strength="mediun level password"
    else:
        strength="weak level password"
    return password,strength
if __name__=="__main__":
    pwd=input("enter the password=")
    password,strength=check_password_strength(pwd)
    print(password,"--->>",strength)
    
    