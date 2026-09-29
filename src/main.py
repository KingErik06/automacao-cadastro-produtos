import pyautogui
import pandas as pd 
from login import login
from cadastro import cadastro

tabela = pd.read_excel('data/produtos.xlsx')

login()
for linha in tabela.index:
    codigo = tabela.loc[linha, 'codigo']
    marca = tabela.loc[linha, 'marca']
    tipo = tabela.loc[linha, 'tipo']
    categoria = tabela.loc[linha, 'categoria']
    preco_unitario = tabela.loc[linha, 'preco_unitario']
    custo = tabela.loc[linha, 'custo']
    obs = tabela.loc[linha, 'obs']
    if pd.isnull(obs):
        obs = 'N/A'
    print(codigo)
    print(marca)
    cadastro(codigo, marca, tipo, categoria, preco_unitario, custo, obs)