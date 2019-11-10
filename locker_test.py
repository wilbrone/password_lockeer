import unittest

from user import User #class user import
from credential import UserCredential #class credential import


class TestUser(unittest.TestCase):
    """
    Class to test the  functions on the  readfiles module

    Args:
        unittest.TestCase: Class from the unittest module to create unit tests
    """

    #****************************************************************************************
    test_list = []
    def setUp(self):
        """
        set up to run before all tests
        """
        self.new_user = User("James Muriuki","JM","james@ms.com","0712345678","godfather",[]) # create contact object

        self.new_user_credential = UserCredential("Twitter","james@ms.com","godfather","jemmo") # create contact object


    #***********************************************************************************************
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.full_name,"James Muriuki")
        self.assertEqual(self.new_user.user_name,"JM")
        self.assertEqual(self.new_user.email,"james@ms.com")
        self.assertEqual(self.new_user.phone,"0712345678")
        self.assertEqual(self.new_user.p_word,"godfather")
        self.assertEqual(self.new_user.credential,[])

        self.assertEqual(self.new_user_credential.media,"Twitter")
        self.assertEqual(self.new_user_credential.email,"james@ms.com")
        self.assertEqual(self.new_user_credential.p_code,"godfather")
        self.assertEqual(self.new_user_credential.u_name,"jemmo")

    #********************************************************************************************
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []
        UserCredential.credentials_list = []

    #*******************************************************************************************    
    def test_save_user(self):
        """
        test case for saving user ater appending the credentials in the array in user object            
        """

        self.new_user.save_user()

        self.assertEqual(len(User.user_list),1)

    #***********************************************************************************************    
    def test_save_new_user(self):    
        """
        test for saving a new user        
        """
        new_test_credential = UserCredential("IG","don@gmail.com","godfather","don") # create contact object
        new_test_credential.save_credential()

        self.new_user.save_user()
        test_user = User("Ray Don","DR","don@gmail.com","0712345678","sundry",[])
        test_user.save_user()

        # sre = User.user_list[1]
        # for i in sre.credential:
        #     print(i.media)

        self.assertEqual(len(User.user_list),2)

    #*************************************************************************************************
    def test_save_credential(self):
        """
        test case for the saving of credential object in an array        
        """
        self.new_user_credential.save_credential()
        self.assertEqual(len(UserCredential.credentials_list),1)

    #**************************************************************************************************
    def test_save_multiple_credential(self):
        """
        test case seving of multiple credential objects in an array
        """
        self.new_user_credential.save_credential()

        new_test_credential = UserCredential("Facebook","james@ms.com","godfather","moo") # create contact object
        new_test_credential.save_credential()

        self.assertEqual(len(UserCredential.credentials_list),2)

    #*******************************************************************************************************
    def test_get_user(self):
        """
        test case for testing if user is extracted via index chosen        
        """
        test = User("Brad Pitt","DR","don@gmail.com","0712345678","sundry",[])
        test.save_user()
        data = User.user_list[0]
        print(data.full_name)

        self.assertEqual(data,User.get_user())


    # ********************************************************************************************
    def test_password_gen(self):
        trial = self.new_user.p_word
        print(trial)

        self.assertEqual(trial,UserCredential.generate_password())


if __name__ == "__main__":
    unittest.main()


# ()