import pyautogui
import pyperclip
from time import sleep
leituraPath = 'CNPJs.txt'
escritaPath = 'resultado.txt'
lista = []
with open(leituraPath, 'r') as arquivo:
    lista = arquivo.read().split('\n')
cnpjs = []
for i in lista:
  cnpjs.append(i.split(','))


pyautogui.press('win')
sleep(1)
pyautogui.write('google')
sleep(0.5)
pyautogui.press('enter')
sleep(1)

for cnpj in cnpjs:
  if(cnpj[1] == '0'):
    print(cnpj[0])
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('shift')
    pyautogui.press('n')
    pyautogui.keyUp('ctrl') 
    pyautogui.keyUp('shift') 

    pyautogui.write('https://solucoes.receita.fazenda.gov.br/Servicos/certidaointernet/PJ/EmitirPGFN')
    pyautogui.press('enter')
    sleep(3)
    pyautogui.press('tab')
    sleep(0.3)
    pyautogui.write(cnpj[0])
    sleep(0.3)
    pyautogui.press('enter')

    sleep(3)

    pyautogui.keyDown('ctrl')
    pyautogui.press('u')
    sleep(2)
    pyautogui.keyDown('ctrl')
    pyautogui.press('a')
    sleep(0.3)
    pyautogui.press('c')

    pyautogui.keyDown('ctrl')
    pyautogui.press('w')
    pyautogui.keyUp('ctrl') 
    sleep(1)

    texto = pyperclip.paste()
    # print(texto)
    
    
    if('Emiss&atilde;o de nova certid&atilde;o' in texto):
      with open(escritaPath, 'a') as arquivo:
        arquivo.write(f"{cnpj[0]}, 1\n")
      pyautogui.press('tab')
      pyautogui.press('tab')
      pyautogui.press('enter')

      sleep(5)
      pyautogui.press('enter')
      sleep(5)
      pyautogui.press('enter')
      sleep(5)
      pyautogui.press('enter')
    else:
      with open(escritaPath, 'a') as arquivo:
        arquivo.write(f"{cnpj[0]}, 0\n")

    pyautogui.keyDown('ctrl')
    pyautogui.press('w')
    pyautogui.keyUp('ctrl') 
  with open(escritaPath, 'a') as arquivo:
        arquivo.write(f"{cnpj[0]}, 1\n")
pyautogui.keyDown('ctrl')
pyautogui.press('w')
pyautogui.keyUp('ctrl') 