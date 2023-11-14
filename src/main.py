import json 
import markdown
import os

def limpar_diretorio_html(diretorio, titulos_atuais):
    for arquivo in os.listdir(diretorio):
        if arquivo.endswith('.html') and arquivo not in titulos_atuais:
            os.remove(os.path.join(diretorio, arquivo))

def carregar_dados_json(caminho_arquivo): # Criei uma função para ler os dados do arquivo json quando for chamada pelo parametro(caminho_arquivo)
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo: 
            return json.load(arquivo)
        
def ler_markdown(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        return markdown.markdown(arquivo.read())
    
def substituir_placeholders(template, postagem, conteudo_html):
    return template.replace('{titulo}', postagem['titulo'])\
                   .replace('{conteudo}', conteudo_html)\
                   .replace('{data}', postagem['data'])\
                   .replace('{autor}', postagem['autor'])
                   
def salvar_html(nome_arquivo, conteudo, diretorio):
    caminho_completo = os.path.join(diretorio, nome_arquivo)
    with open(caminho_completo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(conteudo)
            
# Carregar dados JSON
caminho_do_json = '../data/posts.json'
dados_postagens = carregar_dados_json(caminho_do_json)

# Ordenar postagens pela ordem
dados_postagens['postagens'].sort(key=lambda x: x.get('ordem', 9999))

# Carregar template HTML

with open('./templates/template.html', 'r', encoding='utf-8') as arquivo:
    template_html = arquivo.read()

# Preparar para limpar o diretório de saída
diretorio_html = '../postshtml'
titulos_atuais = [postagem['titulo'].replace(' ', '_') + '.html' for postagem in dados_postagens['postagens']]

# Criar o diretório se não existir
if not os.path.exists(diretorio_html):
    os.makedirs(diretorio_html)

# Limpar o diretório HTML
limpar_diretorio_html(diretorio_html, titulos_atuais)

# Processar cada postagem 

for postagem in dados_postagens['postagens']:
    caminho_markdown = postagem['caminho_markdown']
    conteudo_html = ler_markdown(caminho_markdown)
    pagina_html = substituir_placeholders(template_html, postagem, conteudo_html)
    nome_arquivo_saida = f"{postagem['titulo'].replace(' ', '_')}.html"
    salvar_html(nome_arquivo_saida, pagina_html, diretorio_html)

for postagem in dados_postagens['postagens']:
    print(f"Processando postagem: {postagem['titulo']} com ordem {postagem.get('ordem', 'Não definido')}")
 