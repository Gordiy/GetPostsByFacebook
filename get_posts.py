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
    parser.add_argument('password', help = 'Login password')

    args = parser.parse_args()

    session = requests.session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36 Edge/12.0'
    })

    fb_dtsg, user_id, xs = login(session, args.email, args.password)

    if user_id:
        print('{0}:{1}:{2}'.format(fb_dtsg, user_id, xs))

    else:
        print 'Error!!! Login failed.'