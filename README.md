<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Pandas-2.x-150458?logo=pandas&logoColor=white">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg">
</p>

# 🤖; Automação de Cadastro de Produtos.

Automação desenvolvida em Python e PyAutoGUI para realizar o cadastro automático de produtos em um sistema web, utilizando uma planilha Excel como fonte de dados.

## 🤖; Tecnologias.
- Python;
- PyAutoGUI;
- Pandas;
- OpenPyXL;

## 🤖; Objetivo.

O objetivo desta automação é facilitar o processo de cadastro de produtos em sistemas web, automatizando tarefas repetitivas e reduzindo a necessidade de preenchimento manual.
Os produtos são armazenados em uma planilha Excel e processados automaticamente pela aplicação.

## 🤖; Funcionalidades.
- Leitura de produtos através de uma planilha `.xlsx`;
- Login automático no sistema web;
- Preenchimento automático do formulário de cadastro;
- Cadastro de múltiplos produtos em sequência;
- Tratamento de campos de observação vazios;
- Navegação automática pelo formulário utilizando o teclado.

## 🤖; Como Funciona.
- A aplicação lê os produtos presentes na planilha Excel;
- Realiza o login automaticamente no sistema;
- Percorre os produtos utilizando Pandas;
- Preenche os campos do formulário automaticamente;
- Trata observações vazias como `N/A`;
- Realiza o cadastro de cada produto em sequência.

## 🤖; Execução.

Clone o repositório e instale as dependências:
`pip install -r requirements.txt`

Execute a automação a partir da pasta principal do projeto:
`python src/main.py`

> Observação: a automação utiliza PyAutoGUI para controlar o navegador e, por isso, depende da interface e da ordem dos campos do sistema utilizado.
