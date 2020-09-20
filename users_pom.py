

users = [{"name": "wrong_user", "email": "wrong_mail@gmail.com", "password": "wrong_password"},
         {"name": "correct_user", "email": "ssls.automation+666@gmail.com", "password": "123456"}]


def get_user(name):
    try:
        return next(user for user in users if user["name"] == name)
    except:
       print('User {} is not defined, enter a valid user.'.format({name}))
