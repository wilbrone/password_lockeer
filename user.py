from credential import UserCredential as user_cred

class User:
    """
    class that creates new instances of the users
    """
    user_list = [] #an empty users list
    def __init__(self,full_name,user_name,email,phone,p_word,credential):

        '''
        __init__ method that helps us define properties for our objects.

        Args:
            first_name: New contact first name.
            last_name : New contact last name.
            number: New contact phone number.
            email : New contact email address.
        '''

        self.full_name = full_name
        self.user_name = user_name
        self.email = email
        self.phone = phone
        self.p_word = p_word
        self.credential = []

    def save_user(self):
        """
        this is a method to save the users and also get the credentials 
        and save them in my user object.        
        """
        self.credential = user_cred.credentials_list

        User.user_list.append(self)

    @classmethod
    def get_user(cls):
        """
        this method gets the user object         
        Returns:
            user object for itteration
        """
        for user in cls.user_list:
            print(user.full_name)
            return user

    @classmethod
    def user_login(cls,uName,passWord):
        """
        method for getting the user based on th password
        """
        print(passWord+" is here")
        for user in cls.user_list:
            if user.p_word == passWord and user.user_name == uName:
                print("Login successful")
                return user
            else:
                print("wrong user name or password")
            return user

User("Ray Don","DR","don@gmail.com","0712345678","sundry",[])