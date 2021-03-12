from src.domain.User import User
from werkzeug.security import check_password_hash, generate_password_hash
from src.repository.UserRepository import UserRepository

userRepository = UserRepository()

def authenticate(username, password):
    user = userRepository.findByUserName(username)
    if user and check_password_hash(user.password,password):
        return user


def identity(payload):
    user_id = payload['identity']
    return User.query.get(user_id)