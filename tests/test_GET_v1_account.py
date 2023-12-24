def test_get_v1_account(dm_api_facade):

    token = dm_api_facade.login.get_auth_token(login='test20', password='123456')
    dm_api_facade.account.set_headers(headers=token)
    dm_api_facade.login.set_headers(headers=token)
    dm_api_facade.account.get_current_user_info()
    #dm_api_facade.login.logout_user()
    dm_api_facade.login.logout_user_from_all_devices()
