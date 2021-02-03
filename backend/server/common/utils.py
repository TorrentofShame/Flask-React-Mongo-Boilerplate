from werkzeug.security import safe_str_cmp

from server.models.user import User, UserRole

def authenticate(username: str, password: str):
    user = User(username=username).exclude("id").first()
    if user and safe_str_cmp(user.password.encode("utf-8"), password.encode("utf-8")):
        return user

