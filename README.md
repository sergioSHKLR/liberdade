# liberdade

Página única, estática e bilíngue (PT padrão, EN via botão) da campanha virtual "Liberdade".

**Status: RASCUNHO.** Repositório privado, sem GitHub Pages, sem DNS. Publicação só com aprovação do Sergio.

- HTML/CSS puro + JS mínimo para o idioma. Sem rastreadores, fontes externas ou CDNs.
- Credenciais: https://shadowbox.shklr.org
- Imprensa: sergio@shklr.org
- Fotos (comprimidas, webp) em photos/. TODO: kit de imprensa.
- Editar textos em build.py + template.html e rodar `python3 build.py`.

## Publicar depois (quando aprovado)
1. Tornar público / ativar GitHub Pages (branch `main`, raiz), domínio `liberdade.shklr.org`.
2. Na Hover: registro `CNAME` com host `liberdade` apontando para `sergioshklr.github.io`.
