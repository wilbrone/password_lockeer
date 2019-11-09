class User:
    """
    class that creates new instances of the users
    """

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
        pass    