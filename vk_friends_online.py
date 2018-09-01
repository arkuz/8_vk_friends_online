import vk
import sys
import getpass

APP_ID = 6677787


def get_user_login():
    return input('VK login: ')


def get_user_password():
    return getpass.getpass(prompt='VK password: ')


def get_api_session(app_id, login, password, scope, api_version=5.84):
    try:
        session = vk.AuthSession(
            app_id=app_id,
            user_login=login,
            user_password=password,
            scope=scope
        )
        return vk.API(session, version=api_version)
    except vk.exceptions.VkAuthError:
        return None


def get_online_friends(api):
    try:
        return api.friends.getOnline()
    except vk.exceptions.VkAPIError:
        return None


def output_friends_to_console(friends_online):
    print('Friends online:')
    for friend in friends_online:
        print('  id:{}'.format(friend))


if __name__ == '__main__':

    login = get_user_login()
    if not login:
        sys.exit('Login is empty.')
    password = get_user_password()
    if not password:
        sys.exit('Password is empty.')

    scope = 'friends'
    api_params = [
        APP_ID,
        login,
        password,
        scope,
    ]

    api = get_api_session(*api_params)
    if api is None:
        sys.exit('Authorization error.')

    friends_online = get_online_friends(api)
    if friends_online is None:
        sys.exit('API error.')

    output_friends_to_console(friends_online)
