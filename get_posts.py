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

def main():
    '''url = 'https://graph.facebook.com/v2.9/me?feed=EAACEdEose0cBANgCz3AAdxHBtMvSCIUwok3P5kq89HZAHlWdQzho2ZBEYGZAj3SYAa89AEtUCZBHFYZCIbCCxT9Dwv9bc3DW7X0fEXnZBIHRgpZCslJnZA5on07aGzADUtHkXDPL6pxoI5r4XRtpZA5ZBUQbjLsZAlU1gj9PxcZAsWKt9ClsXhUMa2MTDGIcULflUufJJ2Vu3pErOzMY9TkApTDcOrZBfo0ZAnkdgZD'
    #facebook_api_key = 'EAACEdEose0cBAAVJGMO8OMMWIWyB8YNOTPoK2QsZAA4j9I6GiaTwjekgsxfjd8EIEaZBsFujSJXXfIUFgafBRDAcPzbt9QTvEVm50gujZAtnJzoxd6RVCKAE9Ms0BOc1C3NAN5g8DZBox6uNw1Mh0lDnt785kyPTF2cVZArsWQOuBjR0rdNyq08B3EZB61EuYZD'
    req = urllib.request.Request(url)
    #request.add.headers('access_token', facebook_api_key)
    req = urllib.request.urlopen(url)#Відкриває урл з токеном получає метод
    #request = request.open(url)
    response = requests.urlopen(req)
    encoding = response.headers.get_content_charset()
    if encoding is None:
        encoding = 'utf-8'
    global r
    r = req.read()
    data = json.loads(req.read().decode(encoding))
    with open('JSON.json', 'w') as file:
        json.dump(data)'''

    url = 'https://graph.facebook.com/v2.9/me?feed=EAACEdEose0cBANgCz3AAdxHBtMvSCIUwok3P5kq89HZAHlWdQzho2ZBEYGZAj3SYAa89AEtUCZBHFYZCIbCCxT9Dwv9bc3DW7X0fEXnZBIHRgpZCslJnZA5on07aGzADUtHkXDPL6pxoI5r4XRtpZA5ZBUQbjLsZAlU1gj9PxcZAsWKt9ClsXhUMa2MTDGIcULflUufJJ2Vu3pErOzMY9TkApTDcOrZBfo0ZAnkdgZD'
    accesstoken = "EAACEdEose0cBANgCz3AAdxHBtMvSCIUwok3P5kq89HZAHlWdQzho2ZBEYGZAj3SYAa89AEtUCZBHFYZCIbCCxT9Dwv9bc3DW7X0fEXnZBIHRgpZCslJnZA5on07aGzADUtHkXDPL6pxoI5r4XRtpZA5ZBUQbjLsZAlU1gj9PxcZAsWKt9ClsXhUMa2MTDGIcULflUufJJ2Vu3pErOzMY9TkApTDcOrZBfo0ZAnkdgZD"
    graph = facebook.GraphAPI(access_token = accesstoken, version=2.9)
    post = graph.get_object(id='380312659009364')
    print(post)

    return data, r
r = 0
main()
print (r)



print(main(request.read()))

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