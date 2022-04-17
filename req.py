import requests


def get_data():
    r = requests.get('https://dt.miet.ru/ppo_it_final',
                     headers={'X-Auth-Token': 'famscoow'})
    return r.json()['message']
