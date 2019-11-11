#!/usr/bin/env python3.6

from user import User
from credential import UserCredential

def main():

    count = 0

    print("do you have an account")
    print("y - Yes\nn - No")
    answer = input().lower()

    if answer == "n":
        print("Create an account\n")

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

        print("\n")
        print("Please Login to continue...")
        print("Enter UserName:")
        user_name = input()
        print("Enter Password:")
        p_word = input()

        current_user = log_in(user_name,p_word)
        print("\n")
        try:
            for c_user in current_user.user_list:
            
                count = 1

        except AttributeError:
            print("Please enter correct password and/or Username")
            # answer = "y" 
            # return answer
    elif answer == "y":
        print("\n")
        print("Login please..")
        print("-"*10)
        print("Enter UserName:")
        user_name = input()
        print("Enter Password:")
        p_word = input()

        current_user = log_in(user_name,p_word)
        print("\n")
        print(current_user)
        if current_user != None: 
            count = 1
        else:
            print("User do not Exist")    



    while count == 1:
        for active_user in current_user.user_list: 
            print("Welcome " + active_user.user_name)

            print("\nHere are a few options:")
            print("Short Code:\ncc - Add Credential\ndc - Display Creddentials\nex - exit\n")
            short_code = input().lower()

            if short_code == "dc":
                if len(active_user.credential) <= 0:
                    print("You have no save Credentials. You can add...")
                else:
                    for credentials in active_user.credential:
                        print(credentials.media + " " + credentials.u_name + " " + credentials.email)

            elif short_code == "cc":
                print("Add credential")
            elif short_code == "ex":
                print("You Logged out...")

                count = 0

# ********************************************************************************************
def create_user(f_name,user_name,email,phone,pWord,credential):
    nUser = User(f_name,user_name,email,phone,pWord,credential).save_user()
    # cnt_user = nUser.save_user()
    return nUser


def log_in(name,pword):
    # print(User.user_login(name,pword))
    return User.user_login(name,pword)

if __name__ == '__main__':

    main()