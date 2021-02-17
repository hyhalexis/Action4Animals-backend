from db import db, User

def get_user_by_username(username):
    return User.query.filter(User.username == username).first()


def get_user_by_session_token(session_token):
    return User.query.filter(User.session_token == session_token).first()


def get_user_by_update_token(update_token):
    return User.query.filter(User.update_token == update_token).first()


def verify_credentials(username, password):
    user = get_user_by_username(username)
    if user is None:
        return False, None
    
    return user.verify_password(password),user


def create_user(first_name, last_name, username, phone_number, email, password):
    user = get_user_by_email(email)
    if user is not None:
        return False, user
    new_user = User(
        first_name=first_name, 
        last_name = last_name, 
        username=username, 
        phone_number = phone_number, 
        mail=email, 
        password=password
    )
    db.session.add(new_user)
    db.session.commit()
    return True, new_user


def renew_session(update_token):
    user = get_user_by_update_token(update_token)
    if user is None:
        raise Exception("Invalid update token.")

    user.renew_session()
    db.session.commit()
    return user
