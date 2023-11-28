---
titulo: "Documentação WikiProject"
conteudo: "Documentação"
data: "2023-11-27"
autor: "Leonardo v Santana"

---

Documentação do Projeto WikiProject

Introdução

No decorrer do meu trabalho com blogs estáticos, desenvolvi o WikiProject, um sistema que eu criei para transformar arquivos Markdown em páginas HTML, com o objetivo de facilitar a publicação de conteúdo de maneira eficiente. Este projeto é o resultado da minha exploração com Python, onde implementei um processo automatizado que não só converte Markdown para HTML, mas também integra este conteúdo a um modelo HTML e o publica no GitHub Pages.
Pré-requisitos que Preparei

Antes de começar a usar o sistema que desenvolvi, você precisará ter em seu ambiente de desenvolvimento:

Python instalado na versão 3.11.5 ou mais recente.
Pip, o gerenciador de pacotes do Python, instalado.
Os módulos Python markdown e frontmatter, que eu selecionei por sua robustez e facilidade de uso.

Configuração que Realizei

Primeiro, clonei o repositório do GitHub para a minha máquina local.
Certifiquei-me de que estava trabalhando na branch "main".
Organizei os arquivos Markdown em uma pasta que nomeei "postsmd".
Coloquei o modelo HTML que elaborei em uma pasta chamada "templates", especificamente no arquivo "template.html".
Criei uma pasta "postshtml" para armazenar os arquivos HTML que o script gera.

Como eu Utilizo

Com os pré-requisitos instalados, eu:

Executo o script src/main.py para converter os arquivos Markdown para HTML e gerar as páginas do blog.
As páginas HTML resultantes são armazenadas na pasta "postshtml".
Personalizo o modelo HTML em "template.html" para moldar o layout do blog conforme meu gosto.

Publicando no GitHub Pages

Para hospedar o blog estático no GitHub Pages, configurei uma ação no GitHub Actions para automatizar o processo de implantação, utilizando um fluxo de trabalho configurado em um arquivo yml.

Esta configuração permite que eu faça o deploy automático do meu blog sempre que faço um push para a branch "main" ou quando aciono manualmente o workflow.
Conclusão

Criei o WikiProject para ser uma solução personalizável e adaptável. As instruções que compartilhei aqui são o que eu sigo para configurar e utilizar o sistema, mas é claro que você pode e deve ajustar as configurações para que atendam às suas necessidades específicas. 


