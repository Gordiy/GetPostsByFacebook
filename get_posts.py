import requests
import json
from pyquery import PyQuery as pq
import argparse
from settings import USER_PASSWORD
from settings import USER_LOGIN
from settings import USER_ID

def login(session, email, password):
#Вказуємо домашню сторінку Facebook's і завантажуємо Facebook's cookies
    response = session.post('https://m.facebook.com')
    response = session.post('https://m.facebook.com/login.php', data={
        'email': USER_LOGIN,
        'pass': USER_PASSWORD
    }, allow_redirects=False)
#Якщо логін є вірним - то вхід відбудеться

    if 'c_user' in response.cookies:
        # Робимо запит на головну сторінку і отримуємо fb_dtsg token

        homepage_resp = session.get('https://m.facebook.com/home.php')
        dom = pyquery.PyQuery(homepage_resp.text.encode('utf8'))
        fb_dtsg = dom('input[name="fb_dtsg"]').val()

        return fb_dtsg, response.cookies['c_user'], response.cookies['xs']
    else:
        return False

def main():
    pass



if __name__ == '__main__':
	parser = argparse.ArgumentParser(description = 'Login to Facebook')
    parser.add_argument('email', help = 'Email address')
    parser.add_argument