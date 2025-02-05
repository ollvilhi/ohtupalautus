from entities.user import User
import re
import sys, pdb


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # Username at least 3 characters
        if len(username) < 3:
            raise UserInputError("Username should be at least three characters between a-z")
        
        # Password at least 8 characters
        if len(password) < 8:
            raise UserInputError("Password should be at least 8 characters and not only letters between a-z")
        
        # Username characters between a-z
        if not re.match("^[a-z]+$", username):
            raise UserInputError("Username should be at least three characters between a-z")
        
        # Password not only characters between a-z
        if re.match("^[a-z]+$", password):
            raise UserInputError("Password should be at least 8 characters and not only letters between a-z")

        return
