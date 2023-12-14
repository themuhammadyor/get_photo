# with open("salom.txt", )
import os
from pprint import pprint
import requests

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
    n = int(input('Enter how many pics you want to get?: '))
    l = 1
    while l <= n:

        url = "https://randomuser.me/api/"
        data = requests.get(url).json()
        large_img_url = data["results"][0]["picture"]["large"]
        medium_img_url = data["results"][0]["picture"]["medium"]
        thumbnail_img_url = data["results"][0]["picture"]["thumbnail"]
    # os.mkdir('images')
        large = requests.get(large_img_url).content
        medium = requests.get(medium_img_url).content
        thumbnail = requests.get(thumbnail_img_url).content

        with FileManager(path=f"images/large({str(l)}).jpg", mode='wb') as f1, FileManager(path=f"images/medium({str(l)}).jpg", mode='wb') as f2, FileManager(path=f"images/thumbnail({str(l)}).jpg", mode='wb')as f3:
            f1.write(large)
            f2.write(medium)
            f3.write(thumbnail)

        l += 1

    # l1 = []
    # for i in data:
    #     print(i)
        # for j in i.key:
        #     if j == "large" or j == "medium" or j == "thumbnail":
        #         pprint(j)
    # with open("urllar.txt", "a") as f:
    #     f.write(str(data))
    # pprint(data)