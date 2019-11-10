import unittest

from user import User #class user import
from credential import UserCredential #class credential import

class TestUser(unittest.TestCase):
    """
    Class to test the  functions on the  readfiles module

    Args:
        unittest.TestCase: Class from the unittest module to create unit tests
    """

    def setUp(self):
        """
        set up to run before all tests
        """
        self.new_user = User("James Muriuki","jemmo","james@ms.com","0712345678","godfather",[]) # create contact object

        self.new_user_credential = UserCredential("Twitter","james@ms.com","godfather","jemmo") # create contact object



    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.full_name,"James Muriuki")
        self.assertEqual(self.new_user.user_name,"jemmo")
        self.assertEqual(self.new_user.email,"james@ms.com")
        self.assertEqual(self.new_user.phone,"0712345678")
        self.assertEqual(self.new_user.p_word,"godfather")
        self.assertEqual(self.new_user.credential,[])

        self.assertEqual(self.new_user_credential.media,"Twitter")
        self.assertEqual(self.new_user_credential.email,"james@ms.com")
        self.assertEqual(self.new_user_credential.p_code,"godfather")
        self.assertEqual(self.new_user_credential.u_name,"jemmo")
        
    def test_save_credential(self):
        """
        test case for the saving of credential object in an array        
        """
        self.new_user_credential.save_credential()
        self.assertEqual(len(UserCredential.credentials_list),1)

    def test_save_multiple_credential(self):
        """
        test case seving of multiple credential objects in an array
        """
        new_test_credential = UserCredential("Facebook","james@ms.com","godfather","moo") # create contact object
        new_test_credential.save_credential()

        self.assertEqual(len(UserCredential.credentials_list),2)



if __name__ == "__main__":
    unittest.main()


# ()