from e2e.tests import test_authorization_page_not_registered_user as tapn

# from e2e import authorization_page_not_registered_user as apn
# from e2e import authorization_page_welcome_back as mpp
# from e2e import my_profile_page_client_area as mpp

# from e2e.authorization_page_welcome_back import go_to_profile

from e2e import my_profile_page_client_area as mpp


def test_connection():
    ''' Check connection'''
    tapn.test_connection()


def test_comparison_user_data():
    # print(mpp.data_of_profile())
    # assert len(mpp.data_of_profile()) == 5
    # assert type(mpp.data_of_profile()) == dict

    first_user_data = mpp.data_of_profile()
    second_user_data = mpp.data_of_profile()
    assert first_user_data == second_user_data


