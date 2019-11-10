#!/usr/bin/env python3.6

from user import User
from credential import UserCredential

def main():
    print("please Login or creat account for new userto continue")
    print("Short Code:\nln - log_in\nsp - sign_up\nex - exit")

    short_code = input().lower()

    if short_code == "sp":
        print("Create an acount\n")
        print("Enter Full Name:")
        f_name = input()
        print("Enter prefered username:")
        user_name = input()
        print("Enter email:")
        email = input()
        print("Enter Phone No.:")
        phone = input()
        print("Enter password")
        pWord = input()
        credential = []

        newUser = create_user(f_name,user_name,email,phone,pWord,credential)
        
        short_code = "ln"
        return short_code

    elif short_code == "ln": 
        print("\n")
        print("Enter UserName:")
        user_name = input()
        print("Enter Password:")
        p_word = input()

        current_user = log_in(user_name,p_word)
        print("\n")
        print(current_user)

        while current_user != None:
            print("welcome")
            code = input()

    elif short_code == "ex":
        print("You Logged out...")    
    else:
        print("invlid choice")


def create_user(f_name,user_name,email,phone,pWord,credential):
    nUser = User(f_name,user_name,email,phone,pWord,credential).save_user()
    # cnt_user = nUser.save_user()
    return nUser


def log_in(name,pword):
    print("you entered " + name + " " + pword)
    return User.user_login(name,pword)

if __name__ == '__main__':

    main()