# import requests
# from threading import Thread
# from pprint import pprint
#
# # def get_data():
# url = 'https://randomuser.me/api/portraits/thumb/men/47.jpg'
# response = requests.get(url)
# data = response.json()
# pprint(data)


# if __name__ == '__main__':
#     pprint(get_data())

import os
from pprint import pprint
import requests
import time


class FileManager:
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode
    def __enter__(self):
        file = open(file=self.path, mode=self.mode)
        self.file = file
        return file
    def __exit__(self, *args, **kwargs):
        self.file.close()

if __name__ == '__main__':
    # url = 'https://randomuser.me/api/'
    # data = requests.get(url).json()
    # pprint(data)
    # os.mkdir('users')
    # os.chdir('..')
    num1, num2 = map(int, input('Enter from ... to ... -> ').split())
    while num1 <= num2:
        url = 'https://randomuser.me/api/'
        data = requests.get(url).json()
        large_img_url = data['results'][0]['picture']['large']
        medium_img_url = data['results'][0]['picture']['medium']
        thumbnail_img_url = data['results'][0]['picture']['thumbnail']
        id = data['results'][0]['id']['value']

        large = requests.get(large_img_url).content
        medium = requests.get(medium_img_url).content
        thumbnail = requests.get(thumbnail_img_url).content
        with FileManager(f'users/large_{id}.jpg', 'wb') as f1, FileManager(f'users/medium_{id}.jpg', 'wb') as f2, FileManager(f'users/thumbnail_{id}.jpg', 'wb') as f3:
            f1.write(large)
            f2.write(medium)
            f3.write(thumbnail)
        num1 += 1

