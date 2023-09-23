import pyautogui as pg
import time

texto = "Insira o texto aqui!"
PessoasNoGrupo = 5

time.sleep(2)
message = "O bot ira comecar!"
pg.write(message)
time.sleep(2)

for i in range(len(message)):
    pg.press('backspace')

time.sleep(2)

PessoasNoGrupo -= 2  # Removendo você e o primeiro @ da conta.

# Escreve o primeiro @ e pressiona enter para marcar o primeiro contato
pg.write("@")
time.sleep(0.5)  # Adiciona um pequeno atraso
pg.press('enter')
time.sleep(0.5)  # Adiciona um pequeno atraso

# Marca as outras pessoas
for i in range(1, PessoasNoGrupo + 1):  # Começa de 1 porque o primeiro contato já foi marcado
    pg.write("@")
    time.sleep(0.5)  # Adiciona um pequeno atraso
    
    # Move para baixo um número de vezes igual ao número de contatos já marcados
    for _ in range(i):
        pg.press('down')
        time.sleep(0.2)  # Adiciona um pequeno atraso
    
    pg.press('enter')
    time.sleep(0.5)  # Adiciona um pequeno atraso

pg.write(texto)
pg.press('enter')