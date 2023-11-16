#Import Required Libraries 

try:
    from colorama import Fore, Style
    from colorama.initialise import reset_all
    from hashlib import sha256
    from discord_webhook import DiscordWebhook, DiscordEmbed
    from Crypto.Cipher import AES
    from Crypto.Util import Padding
    from urllib.request import Request
    import pyfiglet
    import hashlib
    import argparse
    import urllib.request
    import random
    import timeit
    import string
    import time
    import sys
    import os
    import colorama
except:
    sys.exit(Fore.RED + "\n[-]" + Style.RESET_ALL + " Error - Missing requirements. Run 'pip install -r requirements.txt' and re-try.")

# Banner for Good Description
def banner():
    try:
        pfbanner = pyfiglet.figlet_format("CipherGuard", font="graffiti")
        print(pfbanner)
    except pyfiglet.FontNotFound:
        sys.exit(Fore.RED + "\n[-]" + Style.RESET_ALL + " Error - Banner error. Run 'sudo pip3 install --upgrade pyfiglet' and re-try.")

# Option List when File Runs
def menu():
    print("\n\nWhat Do you want to do?")
    print("[1] File Encryption")
    print("[2] File Decryption")
    print("[3] Information About Project")

# File Encryption Code
def encryption():
    def filencrypt(pswd, iv, file):
        key = hashlib.sha256(pswd.encode()).digest()

        with open("AES_IV.txt", "w") as ivf:
            ivf.write(f"Encryption of : {file}\n\n-----BEGIN AES INITIALIZATION VECTOR BLOCK-----\n{iv}\n-----END AES INITIALIZATION VECTOR BLOCK-----".replace("b'", "").replace("'", ""))

        with open(file, "rb") as f:
            data = f.read()

        stime = timeit.default_timer()
        
        cipher = AES.new(key, AES.MODE_CBC, iv)
        paddeddata = Padding.pad(data, 16)
        encrypteddata = cipher.encrypt(paddeddata)
        
        with open(file, "wb") as ef:
            ef.write(encrypteddata)

        time = timeit.default_timer() - stime

        print(Fore.GREEN + "\n[+]" + Style.RESET_ALL + " Encryption of the file " + Fore.GREEN + str(file) + Style.RESET_ALL + " complete in " + Fore.GREEN + str(round(time, 3)) + Style.RESET_ALL + " seconds!\n")
        print("Don't forget the password you used for the encryption of this file!\nAlso a " + Fore.GREEN + "AES_IV.txt " + Style.RESET_ALL + "file has been created, it contains the initialization vector (IV) of the encryption. " + Fore.RED + "\nYou have to keep this file " + Style.RESET_ALL + "because you will need this IV for decrypt your file.")

    file = input(Fore.YELLOW + "\nFile to encrypt : " + Style.RESET_ALL)

    if "." in file:
        pass
    else:
        sys.exit(Fore.RED + "\n[-]" + Style.RESET_ALL + " Error - Missing extension")

    try:
        with open(file, "rb"):
            pass
    except IOError:
        sys.exit(Fore.RED + "\n[-]" + Style.RESET_ALL + f" Error - File not found. Make sure your file is in this path : {os.path.realpath(__file__).replace('filencrypt.py', '')}")

    if os.path.getsize(file) > 62914560:
        sys.exit(Fore.RED + "\n[-]" + Style.RESET_ALL + " Error - File too large. Max size is 60Mo to avoid crashes or errors.")
    else:
        pass

    pswd = input(Fore.YELLOW + "Choose a strong password : " + Style.RESET_ALL)

    def geniv(length):
        str = string.ascii_uppercase + string.digits #+ string.punctuation
        return "".join(random.choice(str) for i in range(length))

    iv = geniv(16)
                
    filencrypt(pswd, iv.encode(), file)

# File Decryption Code
def decryption():
    def filedecrypt(pswd, iv, file):
        key = hashlib.sha256(pswd.encode()).digest()

        with open(file, "rb") as f:
            data = f.read()

        stime = timeit.default_timer()

        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypteddata = cipher.decrypt(data)
        unpaddeddata = Padding.unpad(decrypteddata, 16)

        with open(file, "wb") as ef:
            ef.write(unpaddeddata)
    
        time = timeit.default_timer() - stime

        print(Fore.GREEN + "\n[+]" + Style.RESET_ALL + " Decryption of the file " + Fore.GREEN + str(file) + Style.RESET_ALL + " complete in " + Fore.GREEN + str(round(time, 3)) + Style.RESET_ALL)
    
    file = input(Fore.YELLOW + "\nFile to decrypt : " + Style.RESET_ALL)

    if "." in file:
        pass
    else:
        sys.exit(Fore.RED + "\n[-]" + Style.RESET_ALL + " Error - Missing extension")

    try:
        with open(file, "rb"):
            pass
    except IOError:
        sys.exit(Fore.RED + "\n[-]" + Style.RESET_ALL + " Error - File not found. Make sure your file is in this path : {os.path.realpath(__file__).replace('filencrypt.py', '')}")

    pswd = input(Fore.YELLOW + f"Password used to encrypt {file} : " + Style.RESET_ALL)
    iv = input(Fore.YELLOW + f"IV used to encrypt {file} : " + Style.RESET_ALL)

    if len(iv) != 16:
        sys.exit(Fore.RED + "\n[-]" + Style.RESET_ALL + f" Error - Incorrect length of initialization vector : {len(iv)} chars instead of 16.")

    filedecrypt(pswd, iv.encode(), file)

# Project Description Code
def about():
    print(Fore.YELLOW + f"\n[>] Running file : {os.path.realpath(__file__)}" + Style.RESET_ALL)
    print("\n[>] Presentation\nCipherGuard is a cryptography project is the project we have designed that encrypts and decrypts your files of all types (js, txt, png...) in AES-256. CipherGuard works with a strong password chosen by the user and with a 16 byte initialization vector (IV) generated by the program, you must keep this IV secret and you will need it to decrypt your file. Note that a new IV is created for each encrypted file.")
    print("\n[>] Security\nIs CipherGuard a secure project?\nCipherGuard uses AES-256-bit encryption with Cipher Block Chaining (CBC) mode. Although CBC Mode is less secure than XTS or GCM Modes, it is generally suitable for encrypting more or less sensitive files.\nSecurity also depends on the password you use, you should use a strong password with uppercase, lowercase, symbols and numbers.")


    try:
        with urllib.request.urlopen(req) as response:
            txt = response.read()
    except:
        sys.exit(Fore.RED + "\n[-]" + Style.RESET_ALL + " Error - Contact system error. Email Contact : 2021cs39ak@mitsgwl.ac.in")

    contactway = input(Fore.YELLOW + "\nEmailo be contacted : " + Style.RESET_ALL)
    subject = input(Fore.YELLOW + "Subject : " + Style.RESET_ALL)
    message = input(Fore.YELLOW + "Message : " + Style.RESET_ALL)

    if contactway == "" or subject == "" or message == "":
        sys.exit(Fore.RED + "\n[-]" + Style.RESET_ALL + " Error - Empty inputs")

    img = input(Fore.YELLOW + "Add an image ('y' or 'n') : " + Style.RESET_ALL)
    if img == "y":
        filepath = input(Fore.YELLOW + "Path of image : " + Style.RESET_ALL)

        try:
            with open(filepath, 'rb'):
                pass
        except IOError:
            sys.exit(Fore.RED + "\n[-]" + Style.RESET_ALL + " Error - Image not found")

        if os.path.getsize(filepath) > 8388608:
            sys.exit(Fore.RED + "\n[-]" + Style.RESET_ALL + " Error - File too large. Max size is 8Mo.")
        else:
            pass
        
        with open(filepath, "rb") as f:
            webhook.add_file(file=f.read(), filename="file.png")
    else:
        pass

    embed = DiscordEmbed(title="Contact CipherGuard", color="03b2f8")
    embed.add_embed_field(name="Moyen de contact", value=contactway, inline=False)
    embed.add_embed_field(name="Sujet", value=subject, inline=False)
    embed.add_embed_field(name="Message", value=message, inline=False)

    proxy = {
        "http": "14.97.216.232:80"
    }
    webhook.set_proxies(proxy)
    webhook.add_embed(embed)
    response = webhook.execute()

    print(Fore.GREEN + "\n[+]" + Style.RESET_ALL + " Message sent with success")

if sys.platform.startswith("linux"):
    os.system("clear")
elif sys.platform.startswith("win32"):
    os.system("cls")
else:
    pass

colorama.init()

parser = argparse.ArgumentParser()
parser.add_argument('-e', help="Encrypt a file", action="store_true")
parser.add_argument('-d', help="Decrypt a file", action="store_true")
parser.add_argument('-i', help="Informations", action="store_true")
args = parser.parse_args()

try:
    if args.e:
        banner()
        encryption()

    elif args.d:
        banner()
        decryption()

    elif args.i:
        banner()
        about()

    else:
        banner()
        menu()
        choice = input("Choice: ")

        if choice == "1":
            encryption()

        elif choice == "2":
            decryption()

        elif choice == "3":
            about()

        else:
            sys.exit(Fore.RED + "\n[-] " + Style.RESET_ALL + "Error - You must reply '1', '2', '3'")

except KeyboardInterrupt:
    sys.exit(Fore.RED + "\n[-]" + Style.RESET_ALL + " Error - CipherGuard has been interrupted by user")