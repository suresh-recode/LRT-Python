# import pyautogui as pg
# import time
# time.sleep(5)
# for i in range(10):
#     pg.typewrite('Vijay Recode')
#     pg.press('enter')


import webbrowser
import pyautogui as pg
import time
whatsappphonenumber = '918778479731'
data = 'Test'
webbrowser.open('https://wa.me/{0}?text={1}'.format(whatsappphonenumber, data))
time.sleep(2)
pg.press(['tab'] * 8)
time.sleep(2)
pg.press('enter')
time.sleep(2)
pg.press(['tab'] * 2)
pg.press('enter')
time.sleep(20)
pg.press('enter')
