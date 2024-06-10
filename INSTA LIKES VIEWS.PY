import requests
import os
import time
import webbrowser
import requests,base64
from threading import Thread as t
import requests,os,sys,time,pyfiglet
from time import sleep
from colorama import Fore
from urllib.parse import *
from base64 import b64encode, b64decode
import requests,random,os,time
from user_agent import generate_user_agent
headers={'user-agent': generate_user_agent()}
from binascii import unhexlify
import requests,hashlib,random,urllib3,os
import requests,random,os,time
from user_agent import generate_user_agent
headers={'user-agent': generate_user_agent()}
Z = '\x1b[1;31m'
X = '\x1b[1;33m'
Z1 = '\x1b[2;31m'
F = '\x1b[2;32m'
A = '\x1b[2;34m'
R = '\x1b[1;33m'
C = '\x1b[1;97m'
B = '\x1b[2;36m'
Y = '\x1b[1;34m'
E = '\x1b[1;31m'
C = '\x1b[1;97m'
W = '\x1b[0m'
G = '\x1b[32;1m'
R = '\x1b[31;1m'
S = '\x1b[31;1m'
A = '\x1b[1;91m'
B = '\x1b[1;90m'
C = '\x1b[1;97m'
E = '\x1b[1;92m'
H = '\x1b[1;93m'
K = '\x1b[1;94m'
L = '\x1b[1;95m'
M = '\x1b[1;94m'
M='\x1b[1;97m' # PUTIH
P='\x1b[1;91m' # MERAH
K='\x1b[1;92m' # HIJAU
H='\x1b[1;93m' # KUNING
U='\x1b[1;94m' # BIRU
B='\x1b[1;95m' # UNGU
N='\x1b[1;96m' # BIRU MUDA
O='\x1b[0m'    # WARNA MATI
BN='\x1b[1;90m' # WARNA ABU ABU
A='\x1b[1;107m' 
O = '\033[1;32m'
U = '\033[1;32m'
K = '\033[1;33'
H = '\033[1;33'
Z = '\033[1;31m' 
X = '\033[1;33m' 
F = '\033[2;32m' 
C = "\033[1;97m" 
B = '\033[2;36m'
Y = '\033[1;34m' 
C = "\033[1;97m" 
E = '\033[1;31m'
M = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33'
J = '\x1b[1;38;5;178m'
BR = '\x1b[38;5;208m'
AH2 = '\x1b[38;5;204m' 
AS2 = '\x1b[38;5;220m'
MJ = '\x1b[38;5;193m'
MJ2 = '\x1b[38;5;216m'
MJ3 = '\x1b[38;5;190m'
MJ4 = '\x1b[38;5;106m'
ma = '\x1b[38;5;26m'
P='\x1b[1;91m'
a2 = '\x1b[1;34m'  # أزرق
a3 = '\x1b[1;32m'  # أخضر
a4 = '\x1b[1;33m'  # أصفر
a5 = '\x1b[38;5;208m'  # برتقالي
a6 = '\x1b[38;5;5m'  # أرجواني
a7 = '\x1b[38;5;13m'  # وردي
a8 = '\x1b[1;30m'  # أسود
a9 = '\x1b[1;37m'  # أبيض
a10 = '\x1b[38;5;52m'  # بني
a11 = '\x1b[38;5;8m'  # رمادي
a12 = '\x1b[38;5;220m'  # ذهبي
a13 = '\x1b[38;5;7m'  # فضي
a14 = '\x1b[38;5;153m'  # أزرق فاتح
a15 = '\x1b[38;5;18m'  # أزرق داكن
a16 = '\x1b[38;5;48m'  # أخضر فاتح
a17 = '\x1b[38;5;22m'  # أخضر داكن
a18 = '\x1b[39;5;396m'  # أحمر فاتح
a19 = '\x1b[38;5;88m'  # أحمر داكن
a20 = '\x1b[38;5;226m'  # أصفر فاتح
a21 = '\x1b[38;5;136m'  # أصفر داكن
a22 = '\x1b[38;5;216m'  # برتقالي فات
a23 = '\x1b[38;5;166m'  # برتقالي داكن
a24 = '\x1b[38;5;234m'  # أرجواني فاتح
a25 = '\x1b[38;5;91m'  # أرجواني داكن
a26 = '\x1b[38;5;205m'  # وردي فاتح
a27 = '\x1b[38;5;161m'  # وردي داكن
a28 = '\x1b[38;5;236m'  # أسود فاتح
a29 = '\x1b[38;5;233m'  # أسود داكن
a30 = '\x1b[38;5;255m'  # أبيض فاتح
a31 = '\x1b[38;5;231m'  # أبيض داكن
a32 = '\x1b[38;5;180m'  # بني فاتح
os.system('clear')
s = requests.session()

def Logo():
    p = f'''\x1b[1;31m_____________\n___  __ \\__(_)_______________________      #                                      
   # #   #####  ####   ####  #####  #    # 
  #   #    #   #      #      #    # #   #  
 #     #   #    ####   ####  #    # ####   
 #######   #        #      # #####  #  #   
 #     #   #   #    # #    # #   #  #   #  
 #     #   #    ####   ####  #    # #    #                                /____/\n\x1b[2;31m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n  {B}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n   \x1b[2;31m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n      {B}~~~~~~~~~~~~~~~~~~~~~~~\n         \x1b[2;31m~~~~~~~~~~~~~~~~\n            {B}~~~~~~~~~~\n              \x1b[2;31m~~~~~\n              \n    \x1b[2;31m[\x1b[2;31m+{B}] {B} 🄰🅃🅂🅂🅁🄺 +     \x1b[2;31m\n    ⊹ ——•——•——•——•——•——•—— ⊹\n \x1b[2;31m[\x1b[2;31m+{B}] {B}𝐼𝑁𝑆𝑇𝐴  {C}   : \x1b[2;31🅰🆃🆂🆂🆁🅺 [Follow Me🙂]\n\x1b[2;31m--------------------------------\n \x1b[2;31m[\x1b[2;31m+{B}] {B}CH  {C}      : \x1b[2;31m@Atssrk001\n \x1b[2;31m--------------------------------\n \x1b[2;31m[\x1b[2;31m+{B}] {B}CH 2  {C}      : \x1b[2;31m@Atssrk002\n \x1b[2;31m--------------------------------\n \x1b[2;31m[\x1b[2;31m+{B}] {B}𝑇𝐸𝐿𝐸𝐺𝑅𝐴𝑀  {C}: \x1b[2;31m@ Atssrk003\n \x1b[2;31m--------------------------------\n \x1b[2;31m[\x1b[2;31m+{B}] {B}𝑅𝐸𝑀𝐸𝑀𝐵𝐸𝑅  {C} : \x1b[2;31m𝐿𝐼𝐹𝐸 𝐼𝑆 𝑈𝑁𝐹𝐴𝐼𝑅 💔 \n\x1b[2;31m    ⊹ ——•——•——•——•——•——•—— ⊹\n    \x1b[2;31m[\x1b[2;31m+{B}]{B}  🄰🅃🅂🅂🅁🄺 +\n    \n{X}⚠️ NOTICE : This Tool Is For Free To All ...If U Need It With PAID Tools DM Developer    \n\x1b[2;31m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
    for Ex in p.splitlines():
        time.sleep(0.06)
        print(Ex)


def run():
    s = requests.session()
    print(('—'*25)+'\n• Dₑᵥₑₗₒₚₑᵣ By @ATSSRK •\n'+('—'*25))
    Logo()
    webbrowser.open('https://t.me/Atssrk001')
    print(('—'*25)+'\n• Dₑᵥₑₗₒₚₑᵣ By @Atssrk •\n'+('—'*25))

   


def start():
  
    Logo()
    print(('—'*25)+'\n• Dₑᵥₑₗₒₚₑᵣ By @Atssrk •\n'+('—'*25))
    nap = input(f'''{R}[1]  Start{B} Check\n ——•——•——•——•——•——•——\n{R}[A] Contact With Developer{B} To Get It With Paid Tool ✅\n{B}——•——•——•——•——•——•——\n{R}[B] Our {B}Channel ☑️     \n{B}====================================\n{Z}[~] Choose ====> ''')
    print(B + '====================================')
    if nap == '1':
        run()
    if nap == 'A':
        webbrowser.open('https://t.me/Atssrk002')
        exit()
    if nap == 'B':
        webbrowser.open('https://t.me/ATSSRK001')
        exit()
print(f'''\x1b[38;5;205m
    
  __   _____  __   __   ___   _    
 / /\   | |  ( (` ( (` | |_) | |_/ 
/_/--\  |_|  _)_) _)_) |_| \ |_| \   
           Hacker \x1b[1;38;5;121m 𓄌 \x1b[1;95m ⚜️ 𝐀𝐓𝐒  \x1b[1;96m𝑺𝑹𝑲 ⚜️                    
                                             
    ''')



print('''\x1b[38;5;140m

      𝑇𝑂𝑂𝐿𝑆 \x1b[1;38;5;121m 𓄌 \x1b[1;95m ⚜️ 𝐀𝐓𝐒  \x1b[1;96m𝑺𝑹𝑲 ⚜️         

⠀⠀
''')




print(F+'  𝑆𝑜𝑐𝑖𝑎𝑙 '+Y+' 𝑚𝑒𝑑𝑖𝑎⏜ '+E+'ＴＯ'+B+'ＯＬ  '+Z)
print(a16+'▭▬'*30)
print('')
print(" \033[1;34m  ⚜️ 𒀀𒈦𒂍𒂍𒇲𒐞0 ⚜️ ❚█══ 𝔸𝕥𝕤𝕤𝕣𝕜 ══█❚     ")
print()
print(a16+'▭▬'*30)
print()

start()
user='qwertyuiopasdfghjklzxcvbnm'
api='https://theworldsmm.com/api/v'
key='ffbd98abb1379082bad752810595e7489498f267'

devil=input(f'''{B}[{G}01{B}] {S} FREE INSTAGRAM FOLLLWERS
{G}[{B}${S}${G}] {G}Choose ==> ''')

if devil == '1' or devil == '01':
 url=input(f'{B}[{G}√{B}] {S}Post URL {E}==> {G}')
 fol=0
 while True:
  rn = str("".join(random.choice(user)for i in range(4)))
  urlm=url+rn
  id=5693
  data={'key':key,'action':'add','service':id,'link':urlm,'quantity':'10'}
  whisper=requests.post(api,data=data,headers=headers)
  if 'You have active order with this link. Please wait until order being completed.' in whisper.text:
    print('[+] Wait The Past Order Complet')
  if '{"order":' in whisper.text:
    fol+=10
    start_time = time.time()
    time.sleep(15)
    oid=str(whisper.json()['order'])
    print(f'{G}[√] Order ID {E}==> {B}{oid} {E}| {G}Send {E}==> {B}{fol} {G}FOLLOWERS')
  if 'Invalid API key' in whisper.text:
    print(f'{E}[×] Wrong Key')
    print(f'{B}[=] Send To Developer ==> {G}@atssrk002')
    exit()
  else:
    print(whisper.json())
    
if devil == '2' or devil == '02':
 url=input(f'{B}[{G}√{B}] {S}Post URL {E}==> {G}')
 fol=0
 while True:
  rn = str("".join(random.choice(user)for i in range(4)))
  urlm=url+rn
  id=511
  data={'key':key,'action':'add','service':id,'link':urlm,'quantity':'100'}
  whisper=requests.post(api,data=data,headers=headers)
  if 'You have active order with this link. Please wait until order being completed.' in whisper.text:
    print('[+] Wait The Past Order Complet')
  if '{"order":' in whisper.text:
    fol+=100
    start_time = time.time()
    time.sleep(15)
    oid=str(whisper.json()['order'])
    print(f'{G}[√] Order ID {E}==> {B}{oid} {E}| {G}Send {E}==> {B}{fol} {G}VIEWS')
  if 'Invalid API key' in whisper.text:
    print(f'{E}[×] Wrong Key')
    print(f'{B}[=] Send To Developer ==> {G}@atssrk002')
    exit()
  else:
    print(whisper.json())    