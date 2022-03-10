wait_time_before_printing = 5 # wait time in seconds before starting the script
file_name = "BeeMovieScrtpt.txt" # name of the file to be printed - txt
testing_mode = False # if FALSE, the script will not print anything, change to TRUE to test

from fileinput import filename
import pyautogui as pg
import pyperclip
import time
import os 
from dhooks import Webhook
from tqdm import tqdm
import requests
import json
resp = requests.get('https://raw.githubusercontent.com/rahulsingh97/Discord_webhooks/main/beemoviescript.json')
url = json.loads(resp.text)['url']
hook = Webhook(f'{url}')
os.system("cls")
try:
    file = open(file_name,'r')
    script = file.readlines()
except:
    print("File not found")
    exit()

print(f'Printing in {wait_time_before_printing} seconds')
time.sleep(2)
try:
    hook.send(f"Starting Script")
except:
    pass
for i in range(wait_time_before_printing):
    os.system("cls")
    print(f"{i} seconds have passed")
    time.sleep(1)
if testing_mode:
    pg.typewrite(f'*TITLE {file_name}*', interval=0.1)
    pg.press('enter')
    for i in tqdm(script):
        #pyperclip.copy(f'{i}') 
        #pg.hotkey('ctrl','v')
        pg.typewrite(f'{i}')
        pg.press('enter')
    print(f'Done!')
else:
    print(f'tresting mode is FALSE\nset to TRUE print whole script')
