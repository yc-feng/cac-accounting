from flask_login import UserMixin
from .util import get_users
from werkzeug.security import check_password_hash, generate_password_hash


class User(UserMixin):
    
    users = get_users()

    def __init__(self, id, password):
        self.id = id
        self.password_hash = password

    @staticmethod
    def get(user_id):
        user_data = User.users.get(user_id)
        if user_data:
            return User(user_id, user_data['password'])
        return None
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
