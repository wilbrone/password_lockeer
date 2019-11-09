class UserCredential:
    """
    class that creates new instances of the users credentials
    """
    user_credentials = [] 

    def __init__(self, media,email,p_code,u_name):

         '''
        __init__ method that helps us define properties for our objects.

        Args:
            media: New credential media.
            email : New credential email.
            p_code: New credential password/passcode.
            u_name : New credential username.
        '''
        self.media=media
        self.email=email
        self.p_code=p_code
        self.u_name=u_name
       