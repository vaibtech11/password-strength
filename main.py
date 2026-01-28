# Regular expression for pattern matching on strings
import re  

passwords = ["abc", "123456", "Pass@123", "Admin"]

def validate_password(pwd):
    # to check whether the length is greater than or equal to 8 
    if len(pwd) < 8:
        return False

    # to check  whether the password includes atleast a special characters or not  
    if not re.search(r"[&!#$^@*(%)]", pwd):
        return False

    # for checking whether password has a number or not
    if not re.search(r"[0-9]", pwd):
        return False

    return True

# final loop for checking the pass/fail condition of password
print("Password results")
for pwd in passwords:
    if validate_password(pwd):
        print(f"{pwd}- pass")
    else:
        print(f"{pwd}- fail")