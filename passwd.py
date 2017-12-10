#!/usr/bin/python3
global passwd
passwd='kn@ck_kn@ck'

def check_passwd():
    password=input('Enter the password: ')
    if password==passwd:
        print('Password match.')
    else:
        print('Wrong password.')


check_passwd()
