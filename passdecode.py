import hashlib
import time
import sys
import bcrypt
import threading

def md5_hash():
    counter = 1
    md5_pass = input("Enter Md5 Hash:")
    md5_file = input("Enter Wordlist Location:")
    if(md5_file == ''):
        md5_file = 'pass.txt'
    else:
        md5_file = md5_file

    try:
        md5_file = open(md5_file, 'r')
        print("*" * 50, "ACTION START", "*" * 50)
    except:
        print("\nFile Not Found")
        quit()

    try:
        for password in md5_file:
            hash_obj = hashlib.md5(password.strip().encode('utf-8')).hexdigest()
            start = time.time()
            # print("*"*100, "ACTION START", "*"*100)
            print("\nTrying password %d ----------->%s" % (counter, password.strip()))
            counter += 1
            end = time.time()
            t_time = end - start

            if hash_obj == md5_pass:
                print("\nPassword found !!! Password Is : %s" % password)
                print("\nTotal Running Time: ", t_time, "seconds")
                # time.sleep(100)
                quit()
        else:
            print("\nPassword Not Found")
            quit()
    except KeyboardInterrupt:
        print("\n-"*50)
        print("\nYou Terminate The Proggram")
        print("-"*50)
'''
import random
#import mechanize
import requests
try:
    import cookielib
except:
    import http.cookiejar as cookielib
import json

def start():
    import random
    #import mechanize
    import requests
    try:
        import cookielib
    except:
        import http.cookiejar as cookielib
    import json
    brows = mechanize.Browser()
    brows.set_handle_robots(False)
    brows._factory.is_html = True
    #brows.set_cookiejar(cookielib.LWPCookieJar())
    useragents = [
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.19) Gecko/20081202 Firefox (Debian-2.0.0.19-0etch1)',
        'Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.6 (KHTML, like Gecko) Chrome/16.0.897.0 Safari/535.6']
    #brows.addheaders = [('User-agent', random.choice(useragents))]
    #brows.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    
    try:
        url = 'https://api.ipify.org/post'
        payload = {'format': 'raw'}
        checkProxyIP = requests.post(url, params = payload, timeout=10)
        print(checkProxyIP.json(encoding ='utf8'))
        print(checkProxyIP.url)
    except:
        print("ERROR")

start()'''
def bc_encrypt():
    #print(dir(bcrypt))
    '''salt ltngth is 29 and main pass length is 60-29 = 31 totla length is 60.'''
    print("-"*50)
    pa = input("Enter Your Text:")
    sal = bcrypt.gensalt()
    ha = bcrypt.hashpw(pa.encode("utf8"), sal)
    print("Your Hashed ------> %s" %ha)
    print("NOTE: YOUR HASH VALUE IS BETWEEN THE QUATION ... OK")
    print("-"*50)

def bc_decrypt():
    counter = 1
    bc_pass = input("Enter Bcrypt Hash:")
    bc_file = input("Enter Wordlist Location:")
    if (bc_file == " "):
        bc_file = 'pass.txt'
    else:
        bc_file = bc_file

    try:
        bc_file = open(bc_file, 'r')
        print("*" * 50, "ACTION START", "*" * 50)
    except:
        print("\nFile Not Found")
        quit()

    try:
        def work():
            counter = 1
            #print("\nTrying password ----------->%s" %  p.strip())
            #counter = 1
            for p in bc_file:
                ok = p.strip("\n").encode("utf-8")
                print("\nTrying password %d----------->%s" %  (counter, p.strip()))
                counter += 1
                if bcrypt.checkpw(ok, bc_pass.encode("utf8")):
                    print("\nPassword found !!! Password Is : %s" % ok)
                    print("NOTE:PASSWORD IS ONLY BETWEEN THE SINGLE CODE ..OK")
                    sys.exit()
            


        #for p in bc_file:
            #ok = p.strip("\n").encode("utf8")
            #thread = threading.Thread(target=work, args=(ok,))
            #thread.start()
        #sys.exit()
        work()
    except KeyboardInterrupt:
        print("\n-" * 50)
        print("\nYou Terminate The Proggram")
        print("-" * 50)
        sys.exit()