# Coleta Ecommerce Automatica 
Este projeto foi feito para realizar a coleta de dados de anuncios e anunciantes dos principais Ecommerces do Brasil que são **Mercado Livre, Amazon e Shopee**. No momento temos apenas a pagina do Mercado Livre funcionando.

As telas são divididas em uma tela principal, uma tela para cada tipo de pesquisa e uma tela de help com informações do App:

**Tela Inicial:**

![Tela Inicial](/assets/paginaInicial.png)

**Tela Sobre:**

![Tela sobre o aplicativo](/assets/telaSobre.png)

**Tela Pesquisa Mercado Livre:**

![Tela Mercado Livre](/assets/telaMercadoLivre.png)

**Tela Pesquisa Amazon:**

Está em construção!!

# Modo de usar o aplicativo

Para usar o aplicativo você deve escolher primeiramente qual pesquisa de ecommerce vai fazer.

## Pesquisa Mercado Livre

### Pesquisa de Anúncios

1. Você deve ter um link do quantos anúncios pretende fazer o primeiro mapeamento, esse link deve ser da página de anúncios igual a página abaixo:

    ![Tela de pesquisa Mercado Livre](/assets/mercadoLivreAnunciosExemplo.png)
    *Imagen Ilustrativa

    Está página contém varios anúncios então a primeira etapa é fazer esta pesquisa e coletar este **link** que esta entre vermelho (Deve ser o link da sua pesquisa e não igual a imagem)

2. O próximo passo é inserir esse link no local correspondente a pesquisa no aplicativo, na imagem a seguir mostra o local correto:
    ![Local Link Mercado Livre](/assets/localLinkMercadoLivre.png)

3. Após inserido o link você deve colocar a qual **categoria** o produto pesquisado pertence. **Exemplo: SMARTPHONE** para uma pesquisa sobre celulares. Na imagem a seguir mostra o local onde deve ser escrito a categoria:

    ![Local categoria Mercado Livre](/assets/localCategoriaMercadoLivre.png)

4. Feito os passos anteriores basta clicar no botão de **Inicia Pesquisa de Anuncios** para iniciar a pesquisa dos anúncios em todas as páginas. Botão na foto a seguir:

    ![Botão Pesquisa Anuncios](/assets/botaoPesquisaAnunciosMercadoLivre.png)

Com isso ira iniciar a pesquisa e quando terminar vai gerar um **CVS** com o nome de **pesquisaAnunciosMercadoLivre.csv** com os anuncios coletados e a categoria no formato: **link;categoria**

### Pesquisa Anunciante



