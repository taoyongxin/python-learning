import requests
from lxml import etree
import json


def get_data():
    url = 'https://music.163.com/weapi/v6/playlist/detail?csrf_token=cd7bb5e8c6e740481ae96c662e06a751'
    data = {
        'encSecKey': '4021383c6a8d10bc8d966c59bd8d1488a3535d5596c53d8e508ee5a540dc8179b70f8d3d0bb90b42a520325fc3085c2d3a1a203bc34b1b4f023e7043625f4ab4b6c93c8be855d83c7b438d9f15989b72f6b599a5c4cf922d616b39fcad8bb4a45c3b46669c7eb1e21409fddc79a973f570fc771972087f0664c7f57c4960aa7e',
        'params': 'a2w1fX1HEHrYHV/w5f0SCm/a/9fSTn2T9d3/iWk8vPV8DAdL2Mijjt3PNWSd3uLqBM32O7tu3MTy4Sy//BIk0K+tcc/P1jCdqe15WqMQK+Ir5UFbjIgxw1krdSd5YoI2g53EFtgIENw/IDWjpbtOT1uelUIkoIRlS7aTeSgNunPGipkt7lNilmTqsRigdMAV'
    }
    headers = {
        'accept': 'application/json, text/javascript',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': '_ntes_nnid=afc0b8c00fad7edac3529e13eb239079,1571915383131; _ntes_nuid=afc0b8c00fad7edac3529e13eb239079; __remember_me=true; WM_TID=YqM7BhU3VFBAVQBERUJ%2BUg%2Bozg%2BbhufE; MUSICIAN_COMPANY_LAST_ENTRY=316304066_musician; ntes_kaola_ad=1; WM_NI=8ccty8AYLgtKA5VvZoxNL9GiPnJnWaoCsUHIMlqs8rINtCNokTXpcogr2spFzUHcgOc0j82HgOTFATWvMUT%2FPegwi3Bd67p5xn00l2CrAO27Xrff%2B%2B76zJqs4cVDAtKJa1U%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed4fb7fb18a97d1e56bb19a8eb6c55b928b9baef15ead9afc82bb5ffcea96a9dc2af0fea7c3b92afcbdad95fc3483878488f74183eb9a97d965bc9284dac66394b2868fd66bad9dbdb6cb438fb4bf94bb7a8b92bca4cd65a98c9891e265a5aefe94f34eba8b8884e645a1f0a6d9b144a5919ca7c46095aa83b6d72594bba998ec3982bcfad8f33fbcb200d1ef3a81ae8fb0b13d9caeaa87aa21f5eab6abf479f8bd9aa5c4808996afd2d837e2a3; _iuqxldmzr_=33; JSESSIONID-WYYY=4vZFNPbaFcTomgzjs%2BZw3IXEtsZJU1zV9nXX2mJSys06YtWQNYC4EbHFjEO4Zhr05y5YpP087zMg7CJ0UQ%5CUOSF8z60xv6IGzsRzDy1NiBo8Xj157zfPUNIxX54jw1Vk685eMCXWDg6Tdu0u7NPFI45uCPf3PZTt2U60AAZZOqE6aHU%2B%3A1587102528986; playerid=55462361; MUSIC_U=ce1299bbfe2c8ced31eb76bf7c9a11bfcadf7a4d0478731a0d3bc96c04292f92f6dbb9e080384a87c20b862285ca8ec87955a739ab43dce1; __csrf=cd7bb5e8c6e740481ae96c662e06a751',
        'origin': 'https://music.163.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Mobile Safari/537.36',
        'referer': 'https://music.163.com/m/discover/toplist?id=19723756',
    }
    response = requests.post(url, data=data, headers=headers)
    with open('./res/json/cloud.json', 'w', encoding='utf-8') as fs:
        json.dump(response.json(), fs)
    print(response.json())


if __name__ == '__main__':
    get_data()
