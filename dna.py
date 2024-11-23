from random import *
from time import *
import os

def limpar():
    os.system("cls")
    


genes = {
    "A": "T",
    "T": "A",
    "G": "C",
    "C": "G"
}

pares = int(input())

controle = -1
round = 2

fita = []
fita2 = []


for i in range(pares):
    gene = choice(list(genes.keys()))

    # A variável cotrole [POR A DESCRIÇÃO DA VARIÁVEL CONTROLE AQUI!!!]
    controle += 1

    if controle == 6:
        controle = -1


    elif controle == 5:
        #print(f"   {gene} -- {genes[gene]}")
        fita += [f"   {gene} -- {genes[gene]}"]
        fita2 += [f"   {gene} --- {genes[gene]}"]


    elif controle == 4:
        #print(f"  {gene} ---- {genes[gene]}")
        fita += [f"  {gene} ---- {genes[gene]}"]
        fita2 += [f"  {gene} ----- {genes[gene]}"]



    elif controle == 3:
        #print(f" {gene} ------ {genes[gene]}")
        fita += [f" {gene} ------ {genes[gene]}"]
        fita2 += [f" {gene} ------- {genes[gene]}"]



    elif controle == 2:
        #print(f"  {gene} ---- {genes[gene]}")
        fita += [f"  {gene} ---- {genes[gene]}"]
        fita2 += [f"  {gene} ----- {genes[gene]}"]



    elif controle == 1:
        #print(f"   {gene} -- {genes[gene]}")
        fita += [f"   {gene} -- {genes[gene]}"]
        fita2 += [f"   {gene} --- {genes[gene]}"]

contador = 0



permissao_para_printar_o_numero_de_pares = False

# Loop de repetição com o tamanho da fita de DNA
for i in range(0, len(fita)):
    if permissao_para_printar_o_numero_de_pares == True:
        print(pares)

    # Se o Loop estiver em um número par, ele printará com as formataçõe da fita1
    if i%2 == 0:
        for ligacao in fita:
            print(f"{ligacao}")
        sleep(0.5)
        limpar()
        permissao_para_printar_o_numero_de_pares = True

    # Senao, ele vai printar com as formatacoes da fita2
    else:
        for ligacao2 in fita2:
            print(f"{ligacao2}")
        sleep(0.5)
        limpar()




#print(len(fita))
#print(len(f"   {gene} -- {genes[gene]}")) #  09
#print(len(f"  {gene} ---- {genes[gene]}")) # 10
#print(len(f" {gene} ------ {genes[gene]}")) # 11