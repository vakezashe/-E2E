

users = [{"name": "wrong_user", "email": "wrong_mail@gmail.com", "password": "wrong_password"}]


# users = [{"name": "USERNAME1", "email": "USERNAME2", "password": ""},
#          {"name": "user_login_error", "email": "mail_error", "password": "password_error"},
#          {"name": "user_password_error", "email": "IngridSchulzKH", "password": "password_error"},]


def get_user(name):
    try:
        return next(user for user in users if user["name"] == name)
    except:
       print('User {} is not defined, enter a valid user.'.format({name}))

























# from operator import itemgetter
#
# users = {"name": "mye", "email": "IngridSchulzKH", "password": ",f,fytvtw"}
#
#
# # users = [{"name": "mye", "email": "IngridSchulzKH", "password": ""},
# #
# #          {"name": "user_login_error", "email": "mail_error", "password": "password_error"},
# #          {"name": "user_password_error", "email": "IngridSchulzKH", "password": "password_error"},]
#
#
# def get_user(name):
#     try:
#         return next(user for user in users if user["name"] == name)
#     except:
#        print('User {} is not defined, enter a valid user.'.format({name}))
#
#
# # print(get_user(users)["mye"])
#
# try:
#     assert user.get_user(users)["email"] and users.get_user(user)["password"]
# except AssertionError as ae:\
#         print(ae)
#
# print((users)["password"])
#
# # print(get_user(users)["password"])
#
# # print(users.get_user('mye')["email"])
#
# # users.get_user(user)["password"]
#
#
#
#
#
#
#
#
#
#
# # get_user(users["name"])
#
# # print(get_user(user)["email"] and get_user(user)["password"])
