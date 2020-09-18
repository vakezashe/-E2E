import authorization_page_welcome_back
import authorization_page_not_registered_user
import users_pom


print(authorization_page_welcome_back.main1(user='correct_user', driver=authorization_page_not_registered_user.wdriver()))


def main2(user, driver):
    pass


if __name__ == "__main__":
    main2(user='correct_user', driver=authorization_page_not_registered_user.wdriver())

