#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2020-06-28 0:47:45

import time
from urllib.parse import quote

import pyautogui
import requests

login_url = "https://shimo.im/lizard-api/auth/password/login"
profile_url = "https://shimo.im/lizard-api/users/me"

user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

headers1 = {
    'authority': 'shimo.im',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'origin': 'https://shimo.im',
    'x-requested-with': 'XmlHttpRequest',
    'x-source': 'lizard-desktop',
    'user-agent': user_agent,
    'dnt': '1',
    'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'referer': 'https://shimo.im/login?from=home',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
}

headers2 = {
    'authority': 'shimo.im',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'accept': 'application/vnd.shimo.v2+json',
    'dnt': '1',
    'x-requested-with': 'XmlHttpRequest',
    'user-agent': user_agent,
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'referer': 'https://shimo.im/dashboard',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
}


def get_username():
    return pyautogui.prompt(text='请输入登录名', title='请输入登录名', default='')


def get_password():
    return pyautogui.password(text='请输入登录密码', title='请输入登录密码', default='', mask='*')


def login():
    body = {'email': get_username(), 'mobile': '+86undefined', 'password': get_password()}
    body = quote('&'.join(f"{k}={v}" for k, v in body.items()), safe='=&')

    r = requests.post(login_url, headers=headers1, data=body)
    time.sleep(5)

    try:
        response = requests.get(profile_url, headers=headers2, cookies=r.cookies)
        data = response.json()
        print("login success:")
        info = (f"name: {data['name']}\n"
                f"email: {data['email']}\n"
                f"createdAt: {data['createdAt']}\n")
        print(info)
    except Exception as e:
        print(e)


def main():
    login()


if __name__ == '__main__':
    main()
