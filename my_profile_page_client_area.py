from e2e import authorization_page_welcome_back


if __name__ == "__main__":
    authorization_page_welcome_back.routes(user='correct_user', driver=authorization_page_welcome_back.wdriver())

