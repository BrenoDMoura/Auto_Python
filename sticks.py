import pyautogui as pg
import time

time.sleep(2)
message = "O bot ira comecar!"
pg.write(message)
time.sleep(2)

for i in range(len(message)):
    pg.press('backspace')

time.sleep(2)

n = 100
pg.write("O programa deve enviar ")
pg.write(str(n))
pg.write(" figurinhas. Observe:")
pg.press('enter')
time.sleep(0.5)

pg.click(x=678, y=1033)
pg.click(x=802, y=1030)
pg.click(x=700, y=702)

for i in range(n):
    pg.click(x=911, y=829)