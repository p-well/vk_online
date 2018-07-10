import vk

from settings import APP_ID
from getpass import getpass


def get_user_login():
    return input('Login:\t')


def get_user_password():
    return input('Password:\t')


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope = 2
    )
    api = vk.API(session, v='5.78')
    friends_online_ids = api.friends.getOnline()
    print(friends_online_ids)


def output_friends_to_console(friends_online):
    pass

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    get_online_friends(login, password)

#    output_friends_to_console(friends_online)