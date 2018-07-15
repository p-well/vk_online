import vk
import requests

from settings import APP_ID
from getpass import getpass


def get_user_login():
    return input('Login:  ')


def get_user_password():
    return getpass('Password:  ')


def fetch_online_friends(login, password):
    #try:
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope = 2
    )
    api = vk.API(session, v='5.78')
    friends_online_ids = api.friends.getOnline()
    friends_online_data = api.users.get(
        user_ids = friends_online_ids,
        lang = 3
    )
    friends_online_data = friends_online_data
#    except requests.exceptions.RequestException:
#        friends_online_data = []
    return friends_online_data


def show_online_friends(friends_online_data):
    print('\nOnline:\n')
    for count, friend_online_data in enumerate(friends_online_data):
        print('{}.{} {}'.format(
            count,
            friend_online_data['first_name'],
            friend_online_data['last_name']
        ))



if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online_data = fetch_online_friends(login, password)
    if friends_online_data:
        show_online_friends(friends_online_data)
    else:
        print('\nError')
