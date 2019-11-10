#!/usr/bin/env python3.6

from user import User
from credential import UserCredential

def main():
    print("please Login or creat account for new userto continue")
    print("Short Code:\nln - log_in\nsp - sign_up\nex - exit")

    short_code = input().lower()
    if short_code == "ln": 
        print("\n")
        print("Enter UserName:")
        user_name = input()
        print("Enter Password:")
        p_word = input()

        current_user = log_in(user_name,p_word)
        print(current_user)

        while True:
            print("welcome")


    elif short_code == "ex":
        print("You Logged out...")
    else:
        print("invlid choice")



def log_in(name,pword):
    return User.user_login(name,pword)

if __name__ == '__main__':

    main()