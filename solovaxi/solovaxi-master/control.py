#========= Control ==========#


def access():
    n = 1
    print('== Log in ==========')
    while n < 4:
        n = n + 1
        user = input('User Name : ' ,)
        password = input('Password : ',)

        set_user = 'group7'
        set_password = 'seven7'

        if user == set_user and password == set_password :
           
            aus = '%74521$co#'
            return aus

        else:

            print('Incorrect Try Again')


if __name__ == '__main__':
    access()
