import json 
import markdown

def carregar_dados_json(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)