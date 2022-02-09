from Project.models import User

def test_new_user():
    
    '''
    Tests user creation through the following logic:
    
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, password (which should be hashed), name, and role fields are correctly defined (User ID is not included in this as it is not created by the user)
    '''
    
    user = User('joebloggs@gmail.com', 'Password')
    assert user.email == 'joebloggs@gmail.com'
    assert user.password != 'Password'
    assert user.name == 'Joe Bloggs'
    assert user.user_type == 'Tutor'