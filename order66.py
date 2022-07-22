import math
import keyboard
import mouse
import pyperclip
import time
from django.db import connection

def get_entry(hard_coded):
    entry = 0
    if hard_coded:
        keyboard.send('F1')
        mouse.move(918,358)
        mouse.double_click()
        mouse.right_click()
        mouse.move(957,393)
        mouse.click('left')
        time.sleep(0.15)
        print(pyperclip.paste())
        entry = float(pyperclip.paste())
    else:
        operar = True
        while operar:
            inp = input ("Enter Entry or N to exit")
            if inp.lower() == 'n':
                operar = False
            else:
                try:
                    entry = float(inp)
                except:
                    print("error")
    return float(entry)



hard_coded = True
equity = 2000 #input("Enter Equity")
stop = float(input("Enter Stop: ")) #input ("Enter Stop")
mouse.move(1015,113)
time.sleep(0.15)
mouse.click()
entry = float(get_entry(hard_coded))
print(type(entry))
targetPrice = abs((entry-stop)*2+entry)
numShares = math.floor((equity*0.015)/abs((entry-stop)))
targetPrice = math.floor(targetPrice *100)/100.0
print("_______________________")
print(targetPrice)
mouse.move(648,395)
mouse.click()
cont = input("Press Y to Continue: ")
if 'y' in cont.lower():
    print(numShares)
    time.sleep(0.25)
    mouse.move(1015,113)
    mouse.click()
    keyboard.send('F1')
    time.sleep(0.35)
    keyboard.write(str(numShares))
    keyboard.send('Enter')
    time.sleep(0.35)
    keyboard.send('F3')
    keyboard.send('Tab')
    keyboard.send('Tab')
    keyboard.send('Tab')
    keyboard.send('Tab')
    keyboard.write(str(stop))
    keyboard.send('Tab')
    keyboard.write(str(targetPrice))
    keyboard.send("Enter")

    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO events_trade (date, time, entry_price, stop_loss, take_profit, shares)")







