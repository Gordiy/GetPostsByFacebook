import requests
import json
import urllib
import urllib.request
import facebook
from pyquery import PyQuery as pq
import argparse
from settings import USER_PASSWORD
from settings import USER_LOGIN
from settings import USER_ID

def login(session):
#Вказуємо домашню сторінку Facebook's і завантажуємо Facebook's cookies

    response = session.post('https://m.facebook.com')
    response = session.post('https://m.facebook.com/login.php', data={
        'email': USER_LOGIN,
        'pass': USER_PASSWORD
    }, allow_redirects=False)
#Якщо логін є вірним - то вхід відбудеться
    text = response.text
    file = open('Response.html', 'w')
    file.write(text)
    file.close()


    if 'c_user' in response.cookies:
        # Робимо запит на головну сторінку і отримуємо fb_dtsg token

        homepage_resp = session.get('https://m.facebook.com/home.php')
        dom = pq(homepage_resp.text.encode('utf8'))
        fb_dtsg = dom('input[name="fb_dtsg"]').val()

        return fb_dtsg, response.cookies['c_user'], response.cookies['xs']
    else:
        return False


def main(response):
    '''#url = 'https://graph.facebook.com/v2.9/me?feed=EAACEdEose0cBANgCz3AAdxHBtMvSCIUwok3P5kq89HZAHlWdQzho2ZBEYGZAj3SYAa89AEtUCZBHFYZCIbCCxT9Dwv9bc3DW7X0fEXnZBIHRgpZCslJnZA5on07aGzADUtHkXDPL6pxoI5r4XRtpZA5ZBUQbjLsZAlU1gj9PxcZAsWKt9ClsXhUMa2MTDGIcULflUufJJ2Vu3pErOzMY9TkApTDcOrZBfo0ZAnkdgZD'
    accesstoken = "EAACEdEose0cBANGUSuua7z41QLvR7rSL8j7d8XvhTweA86SFw1LS8gHlZCVHozKSH1RwZBHynRDQdZAaF65U8NkdgupGCNy99DKNDifNagtDefaqRXDu1WvxwmglZAzfmjozIo45wLqt1qTI4cEt1BjXjPXdTATz6lXxD0slRsTcEYT1vlt56JN3iZAsNO2EZD"
    graph = facebook.GraphAPI(accesstoken, version='2.9')

    #event = graph.get_object(id='me', fields='feed,context')
    #event = graph.get_object(user['id'])
    #user = graph.get_object('1210220782333953')
    posts = graph.get_all_connections(id='1210220782333953', connection_name='likes')
    response = json.loads(posts)
    with open("JSON.json", 'w') as file:
        json.dump(posts, file)'''


    url = 'https://graph.facebook.com/v2.9/1210220782333953?fields=posts'
    response = requests.get(url)
    posts = response.json()[0]['posts']
    resoult = response.text
    response = json.loads(resoult)
    resp = requests.put_like(url)
    count = 12
    while i < count:
        i = i + 1
        story = resp[0]['posts'][i]
    return response

if __name__ == '__main__':
    session = requests.session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36 Edge/12.0'
    })

    fb_dtsg, user_id, xs = login(session)

    if user_id:
        print('{0}:{1}:{2}'.format(fb_dtsg, user_id, xs))

    else:
        print ('Error!!! Login failed.')