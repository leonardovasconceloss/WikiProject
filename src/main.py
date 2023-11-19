import markdown
import os
import frontmatter

# Caminho para o diretório do script
dir_path = os.path.dirname(os.path.realpath(__file__))

# Caminho para o arquivo template.html
template_path = os.path.join(dir_path, 'templates', 'template.html')

base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def limpar_diretorio_html(diretorio, titulos_atuais):
    for arquivo in os.listdir(diretorio):
        if arquivo.endswith('.html') and arquivo not in titulos_atuais:
            os.remove(os.path.join(diretorio, arquivo))

def ler_markdown_e_extrair_dados(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        post = frontmatter.load(arquivo)
        conteudo_html = markdown.markdown(post.content)
        return conteudo_html, post.metadata
        
    
def substituir_placeholders(template, postagem, conteudo_html):
    return template.replace('{titulo}', postagem['titulo'])\
                   .replace('{conteudo}', conteudo_html)\
                   .replace('{data}', postagem['data'])\
                   .replace('{autor}', postagem['autor'])
                   
                   
def salvar_html(nome_arquivo, conteudo, diretorio):
    caminho_completo = os.path.join(diretorio, nome_arquivo)
    with open(caminho_completo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(conteudo)
            
# Carregar template HTML
with open(template_path, 'r', encoding='utf-8') as arquivo:
    template_html = arquivo.read()

# Diretório dos arquivos Markdown
diretorio_markdown = os.path.join(base_path, 'postsmd')

# Preparar para limpar o diretório de saída
diretorio_html = os.path.join(base_path, 'postshtml')
titulos_atuais = []

# Criar o diretório se não existir
if not os.path.exists(diretorio_html):
    os.makedirs(diretorio_html)
    
    # Processar cada arquivo Markdown
for arquivo_md in os.listdir(diretorio_markdown):
    if arquivo_md.endswith('.md'):
        caminho_completo = os.path.join(diretorio_markdown, arquivo_md)
        conteudo_html, dados_postagem = ler_markdown_e_extrair_dados(caminho_completo)
        pagina_html = substituir_placeholders(template_html, dados_postagem, conteudo_html)
        nome_arquivo_saida = f"{dados_postagem['titulo'].replace(' ', '_')}.html"
        titulos_atuais.append(nome_arquivo_saida)
        salvar_html(nome_arquivo_saida, pagina_html, diretorio_html)
        print(f"Processando postagem: {dados_postagem['titulo']}")
        
# Limpar o diretório HTML
limpar_diretorio_html(diretorio_html, titulos_atuais)