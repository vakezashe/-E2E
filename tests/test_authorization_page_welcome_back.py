import requests
from e2e.tests import test_authorization_page_not_registered_user as tapn
from e2e import authorization_page_not_registered_user as apn
from e2e import authorization_page_welcome_back as apw


def test_connection():
    ''' Check connection'''
    tapn.test_connection()


def test_login():
    ''' Check profile url and title page '''

    received_messages = apw.main(user='correct_user', driver=apn.wdriver())
    print(received_messages)

    current_url = received_messages[0]
    current_title = received_messages[1]

    url = 'https://www.sbzend.ssls.com/user/bundles'

    assert current_title == 'My SSL' and current_url == url
