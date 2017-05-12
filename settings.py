def inf_by_user(USER_LOGIN, USER_PASSWORD, USER_ID):
    USER_LOGIN = input('Login : ')
    USER_PASSWORD = int(input('Password : '))
    USER_ID = input('ID  : ')
    return USER_ID, USER_LOGIN, USER_PASSWORD
print(inf_by_user(0, 0, 0))