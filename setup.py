import os
try:
    os.system("python3 install python3-colorama")
    os.system("pip3 install colorama")
    os.system("clear")
    print(" Setup Installed Successfully !!!")
    os.system("python3 hashcreator.py")
except Exception as error:
    print(f"\n {error}\n  Error Encountered...")