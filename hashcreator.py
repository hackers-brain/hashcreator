#!usr/bin/env python
import hashlib
from colorama import Fore, Style
print(Fore.GREEN + """    __  __           __       ______                           __            
   / / / /___ ______/ /_     / ____/__  ____  ___  _________ _/ /_____  _____
  / /_/ / __ `/ ___/ __ \   / / __/ _ \/ __ \/ _ \/ ___/ __ `/ __/ __ \/ ___/
 / __  / /_/ (__  ) / / /  / /_/ /  __/ / / /  __/ /  / /_/ / /_/ /_/ / /    
/_/ /_/\__,_/____/_/ /_/   \____/\___/_/ /_/\___/_/   \__,_/\__/\____/_/     
                                        [Author : HackersBrain]""" + Style.RESET_ALL)


def md5():
    text = input(Fore.GREEN + " [" + Fore.RED + 'x' + Fore.GREEN + "]" + Style.RESET_ALL + " Enter String : " + Fore.GREEN + Style.RESET_ALL)
    md5 = hashlib.md5(text.encode('utf8').strip()).hexdigest()
    m = md5
    print(" MD5 Hash :", m)


def sha1():
    text = input(Fore.GREEN + " [" + Fore.RED + 'x' + Fore.GREEN + "]" + Style.RESET_ALL + " Enter String : " + Fore.GREEN + Style.RESET_ALL)
    sha1 = hashlib.sha1(text.encode('utf8').strip()).hexdigest()
    sh1 = sha1
    print(" SHA1 Hash :", sh1)


def sha256():
    text = input(Fore.GREEN + " [" + Fore.RED + 'x' + Fore.GREEN + "]" + Style.RESET_ALL + " Enter String : " + Fore.GREEN + Style.RESET_ALL)
    sha256 = hashlib.sha256(text.encode('utf8').strip()).hexdigest()
    sh2 = sha256
    print(" SHA256 Hash :", sh2)


def sha384():
    text = input(Fore.GREEN + " [" + Fore.RED + 'x' + Fore.GREEN + "]" + Style.RESET_ALL + " Enter String : " + Fore.GREEN + Style.RESET_ALL)
    sha384 = hashlib.sha384(text.encode('utf8').strip()).hexdigest()
    sh3 = sha384
    print(" SHA384 Hash :", sh3)


def sha512():
    text = input(Fore.GREEN + " [" + Fore.RED + 'x' + Fore.GREEN + "]" + Style.RESET_ALL + " Enter String : " + Fore.GREEN + Style.RESET_ALL)
    sha512 = hashlib.sha512(text.encode('utf8').strip()).hexdigest()
    sh4 = sha512
    print(" SHA512 Hash :", sh4)


ex = 'n'
while ex != 'y':
    try:
        print()
        print(Fore.GREEN + " [" + Fore.RED + 'x' + Fore.GREEN + "]" + Style.RESET_ALL + " Choose option for Generating Hash : ")
        print("""\t     1 : MD5
         2 : SHA1
         3 : SHA256
         4 : SHA384
         5 : SHA512""")
        op = int(input(Fore.GREEN + " [" + Fore.RED + 'x' + Fore.GREEN + "]" + Style.RESET_ALL + " Enter Option : " + Fore.GREEN + Style.RESET_ALL))
        print()
        if op == 1:
            md5()
        elif op == 2:
            sha1()
        elif op == 3:
            sha256()
        elif op == 4:
            sha384()
        elif op == 5:
            sha512()
        else:
            print(" Wrong Input !!!")
    except Exception as error:
        print(f"\n {error}\n  Error Encountered...\t Exiting Program...")
    ex = input(" Do You Want to Exit [y,n] ? : ")
    if ex == 'y':
        print(" Thank You for Using this Program...")
    continue
