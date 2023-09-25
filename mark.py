import pyautogui as pg
import time


texto = "Insira o texto aqui!"
PessoasNoGrupo = 239

time.sleep(2)
message = "O bot ira comecar!"
pg.write(message)
time.sleep(2)

for i in range(len(message)):
    pg.press('backspace')

time.sleep(2)

PessoasNoGrupo -= 2  # Removendo você e o primeiro @ da conta.

inicio = time.time()

# Escreve o primeiro @ e pressiona enter para marcar o primeiro contato
pg.write("@")
pg.press('enter')
# pg.hotkey('shift', 'enter') # Para caso queira dar uma quebra de linha

# Marca as outras pessoas
for i in range(1, PessoasNoGrupo + 1):  # Começa de 1 porque o primeiro contato já foi marcado
    pg.write("@")

    
    # Move para baixo um número de vezes igual ao número de contatos já marcados
    for _ in range(i):
        pg.press('down')

    pg.press('enter')
    #pg.hotkey('shift', 'enter') # Para caso queira dar uma quebra de linha

fim = time.time()

pg.write(texto)
pg.press('enter')

print(f"O programa levou {fim - inicio} segundos para marcar todos os {PessoasNoGrupo} participantes.")