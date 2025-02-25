from app.persistence.repository import InMemoryRepository
from app.models.user import User

class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()

    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    def get_all_users(self):
        return self.user_repo.get_all()
    
    @password.setter
    def password(self, password):
        if not isinstance(password, str):
            raise TypeError("Password must be a string")
        self._password = password
    
    @property
    def is_admin(self):
        return self._is_admin

    @is_admin.setter
    def is_admin(self, is_admin):
        if not isinstance(is_admin, bool):
            raise TypeError("is_admin must be a boolean")
        self._is_admin = is_admin
    
    def update_user(self, user_data):
        self.first_name = user_data.get('first_name', self.first_name)
        self.last_name = user_data.get('last_name', self.last_name)
        self.email = user_data.get('email', self.email)
        self.password = user_data.get('password', self.password)
        self.is_admin = user_data.get('is_admin', self.is_admin)

    def to_dict(self):
        user_dict = super().to_dict()
        user_dict.update({
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'is_admin': self.is_admin
            })
        return user_dict
