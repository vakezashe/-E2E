import authorization_page_welcome_back
import authorization_page_not_registered_user
import users_pom


def main2(user, driver):
    print(authorization_page_welcome_back.main1(user, driver))


if __name__ == "__main__":
    main2(user='correct_user', driver=authorization_page_not_registered_user.wdriver())

