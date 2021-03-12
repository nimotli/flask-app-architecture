import sys
from src.domain.User import User

def testNewUser(newUser):
    assert newUser.username == 'testUserName'
    assert newUser.password == 'testPassword'