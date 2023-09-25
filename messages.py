import pyautogui as pg
import time

time.sleep(2)
message = "O bot ira comecar!"
pg.write(message)
time.sleep(2)

for i in range(len(message)):
    pg.press('backspace')

time.sleep(2)

message = "Digite a mensagem a ser enviada n vezes"
n = 100
pg.write("O programa deve enviar 100 mensagens. Observe: ")
pg.press('enter')

for i in range(n):
    pg.write(message)
    pg.press('enter')