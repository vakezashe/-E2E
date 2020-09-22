import requests
from e2e.tests import test_authorization_page_not_registered_user as tapn
from e2e import authorization_page_not_registered_user as apn
from e2e import authorization_page_welcome_back as apw


def test_connection():
    tapn.test_connection()


def test_login_error():

    received_messages = apw.main(user='correct_user', driver=apn.wdriver())

    current_page_title = received_messages[0]
    current_url_title = received_messages[1]

    assert current_page_title == 'My Profile | SSLs.com' and current_url_title == 'https://www.sbzend.ssls.com/user/profile'
