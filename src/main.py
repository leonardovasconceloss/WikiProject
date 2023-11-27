import markdown
import os
import frontmatter

# Caminho para o diretório do script
dir_path = os.path.dirname(os.path.realpath(__file__))

# Caminho para o arquivo template.html
template_path = os.path.join(dir_path, 'templates', 'template.html')

# Define o caminho base do projeto como o diretório pai do diretório atual do script.
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Função que limpa o diretório HTML, removendo arquivos que não estão na lista de títulos atuais.
def limpar_diretorio_html(diretorio, titulos_atuais):
    for arquivo in os.listdir(diretorio):  # Itera sobre os arquivos no diretório.
        if arquivo.endswith('.html') and arquivo not in titulos_atuais:  # Checa se o arquivo é um HTML não listado.
            os.remove(os.path.join(diretorio, arquivo))  # Remove o arquivo.

# Função para ler o conteúdo de um arquivo Markdown e extrair os dados de frontmatter.
def ler_markdown_e_extrair_dados(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:  # Abre o arquivo Markdown.
        post = frontmatter.load(arquivo)  # Carrega os metadados e conteúdo do arquivo.
        conteudo_html = markdown.markdown(post.content)  # Converte o conteúdo Markdown para HTML.
        return conteudo_html, post.metadata  # Retorna o HTML e os metadados.

# Função para substituir placeholders no template HTML com os dados da postagem.
def substituir_placeholders(template, postagem, conteudo_html):
    # Substitui placeholders no template pelos valores correspondentes da postagem.
    return template.replace('{titulo}', postagem['titulo'])\
                   .replace('{conteudo}', conteudo_html)\
                   .replace('{data}', postagem['data'])\
                   .replace('{autor}', postagem['autor'])
                   
# Função para salvar o conteúdo HTML em um arquivo no diretório especificado.
def salvar_html(nome_arquivo, conteudo, diretorio):
    caminho_completo = os.path.join(diretorio, nome_arquivo)  # Monta o caminho completo do arquivo.
    with open(caminho_completo, 'w', encoding='utf-8') as arquivo:  # Abre/Cria o arquivo para escrita.
        arquivo.write(conteudo)  # Escreve o conteúdo HTML no arquivo.

            
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

# Atualizar index.html com novos links
index_path = os.path.join(base_path, 'index.html')

# Ler o conteúdo atual do index.html
with open(index_path, 'r', encoding='utf-8') as arquivo:
    conteudo_index = arquivo.read()

# Local onde os links devem ser inseridos no index.html
placeholder_links = '<!-- Placeholder para os links -->'

# Construir a lista de links HTML
links_html = '\n'.join(['<a href="postshtml/{0}.html">{1}</a>'.format(titulo.replace(' ', '_'), titulo.replace('_', ' ')) for titulo in titulos_atuais])



# Substituir o placeholder no index.html pelo conteúdo dos links
conteudo_index_atualizado = conteudo_index.replace(placeholder_links, links_html)

# Escrever as atualizações de volta para o index.html
with open(index_path, 'w', encoding='utf-8') as arquivo:
    arquivo.write(conteudo_index_atualizado)
