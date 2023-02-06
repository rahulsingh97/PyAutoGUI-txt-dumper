wait_time_before_printing = 5 # wait time in seconds before starting the script
#file_name = "BeeMovieScrtpt.txt" # name of the file to be printed - txt
testing_mode = True # if FALSE, the script will not print anything, change to TRUE to test

count = 0
times = 10
sleep_time_before_next_text = 300 # 5 minutes

from fileinput import filename
import pyautogui as pg
import pyperclip
import time
import os 
from dhooks import Webhook
from tqdm import tqdm
import winsound
os.system("cls")

for i in range(wait_time_before_printing):
    os.system("cls")
    print(f"{5-i} seconds start printing")
    time.sleep(1)
os.system("cls")
for i in tqdm(range(times)):
    if testing_mode:
        pg.typewrite(f'I want github student account', interval=0.0001)
        pg.press('enter')
        time.sleep(sleep_time_before_next_text)
        os.system("cls")
    else:
        print(f'tresting mode is FALSE\nset to TRUE') 

winsound.PlaySound("SystemExit", winsound.SND_ALIAS)