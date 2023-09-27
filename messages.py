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
n = 5
pg.write("O programa deve enviar ")
pg.write(str(n))
pg.write(" mensagens predefinidas. Observe:")
pg.press('enter')
time.sleep(0.5)

for i in range(1, n + 1):
    pg.write(message)
    pg.write("_* (")
    pg.write(str(i))
    pg.write(")*_")
    pg.press('enter')