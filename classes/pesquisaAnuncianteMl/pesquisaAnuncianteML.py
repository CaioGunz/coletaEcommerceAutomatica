#Import de Libs usadas na classe
import pandas as pd
import os.path
from tkinter import messagebox
from time import sleep
from classes.chamaDriver.chamaDriver import iniciaDriver, By

#lista para gravacao de dados no pandas
lista_valores = []
lista_link = []

class pesquisaAnuncianteMl(iniciaDriver):
    
    #leitura da tabela gerada na classe pesquisaAnunciosML (a planilha deve estar na pasta do projeto 
    # para que funcione corretamente)
    filePath = 'pesquisaAnunciosMercadoLivre.csv'


    
    #__init__ que faz a instancia do chamaDriver() e chama a categoria
    def __init__(self, link, categoria, file_path):
        super().__init__(driver=None, link=link)
        self.categoria = categoria
        self.driver = self.chamaDriver()
        self.filePath = file_path
        
        #Se o arquivo existir ele iniciar a pesquisa, se nao ele gera um erro
        if os.path.isfile(self.filePath):
            self.links = pd.read_csv(self.filePath, sep=';')
        else:
            self.links = None
        
    #Funcao para coletar os dados usando o Selenium com a funcao By e XPATH para o elemento da pagina
    def coletaDadosAnunciante(self):
        
        sleep(1)
        try:
            #Faz a coleta do titulo do anuncio no Mercado Livre utilizando XPATH para encontrar o elemento
            titulo = self.driver.find_element(By.XPATH, '//h1[@class="ui-pdp-title"]').text
        except:
            #Caso a condicao do Try não exista, no except vai trazer como null para titulo
            titulo = 'null'
        try:
            #Faz a coleta do preco do anuncio no Mercado Livre utilizando XPATH para encontrar o elemento
            preco = self.driver.find_element(By.XPATH, '//div[@class="ui-pdp-price__second-line"]//span[@class="andes-money-amount__fraction"]').text
        except:
            #Caso a condicao do Try não exista, no except vai trazer como null para preco
            preco = 'null'
        try:
            #Faz a coleta da qtdVendida do anuncio no Mercado Livre utilizando XPATH para encontrar o elemento
            qtdVendida = self.driver.find_element(By.XPATH, '//span[@class="ui-pdp-subtitle"]').text
        except:
            #Caso a condicao do Try não exista, no except vai trazer como null para qtdVendida
            qtdVendida = 'null'
        try:
            #Faz a coleta do linkVendedor do anuncio no Mercado Livre utilizando XPATH para encontrar o elemento
            linkVendedor = self.driver.find_element(By.XPATH, '//a[@class="andes-button andes-button--medium andes-button--quiet andes-button--full-width"]').get_attribute('href')
        except:
            #Caso a condicao do Try não exista, no except vai trazer como null para linkVendedor
            linkVendedor = 'null'
        try:
            #Faz a coleta da classificacaoVendedor do anuncio no Mercado Livre utilizando XPATH para encontrar o elemento
            classificacaoVendedor = self.driver.find_element(By.XPATH, '//p[@class="ui-pdp-color--GREEN ui-pdp-size--XSMALL ui-pdp-family--SEMIBOLD ui-seller-data-status__title"]').text
        except:
            #Caso a condicao do Try não exista, no except vai trazer como null para classificacaoVendedor
            classificacaoVendedor = 'null'
        try:
            #Faz a coleta da marca do anuncio no Mercado Livre utilizando XPATH para encontrar o elemento
            marca = self.driver.find_element(By.XPATH, '//th[contains(., "Marca")]/following-sibling::td//span[@class="andes-table__column--value"]').text
        except:
            #Caso a condicao do Try não exista, no except vai trazer como null para marca
            marca = 'null'
        try:
            #Faz a coleta do sku do anuncio no Mercado Livre utilizando XPATH para encontrar o elemento
            sku = self.driver.find_element(By.XPATH, '//th[contains(., "Modelo")]/following-sibling::td//span[@class="andes-table__column--value"]').text
        except:
            #Caso a condicao do Try não exista, no except vai trazer como null para sku
            sku = 'null'
        try:
            #Faz a coleta da categoria do anuncio no Mercado Livre utilizando XPATH para encontrar o elemento
            categoria = self.categoria
        except:
            #Caso a condicao do Try não exista, no except vai trazer como null para categoria
            categoria = 'null'
        try:
            #Faz a coleta do link do anuncio no Mercado Livre utilizando XPATH para encontrar o elemento
            link = lista_link[-1]
        except IndexError:
            #Caso a condicao do Try não exista, no except vai trazer como null para link
            link = 'null'    
        
        #Salva os dados coletados na lista_valores criada no começo do scrypt   
        lista_valores.append([titulo, preco, qtdVendida, linkVendedor, classificacaoVendedor, marca, sku, categoria, link])

    
    #Função para pegar o link da planilha.csv adicionar na lista_link e realizar a pesquisa 
    # no Browser difinido na classe chamaDriver
    def pegaLink(self):
        
        if self.links is not None:
        
            #Entra no loop para realizar a coleta do link e da categoria um por um
            for index, row in self.links.iterrows():
                #Pega o link linha por linha
                link = row['link']
                #Pega a categoria relacionado ao link
                self.categoria = row['categoria']
                #Salva o link na lista_link
                lista_link.append(link)
            
                try:
                    sleep(0.5)
                    #Adiciona o link para o driver iniciar a manipulacao do Browser
                    self.driver.get(link)
                    #Chama a funcao coletaDadosAnunciante
                    self.coletaDadosAnunciante()
                    
                except Exception as e:
                    #Em caso de Exception vai trazer o erro no terminal e dar break no sistema
                    print('Erro desconhecido ao acessar o link: ', str(e))
                    sleep(2)
                    break
            #Chama a funcao salvaDados
            self.salvaDados()
        else:
            messagebox.showinfo(title="Alerta!!", message="O arquivo CSV não existe. Selecione o arquivo novamente com o nome de 'pesquisaAnunciosMercadoLivre.csv'. Gerado na pesquisa de anúncios")
        
    #Funcao para salvar os dados obtidos na coleta
    def salvaDados(self):
        #Define o nome de todas as colunas pesquisadas. Obs: o nome entre ' ' vai seguir a 
        # ordem que estiver no append da funcao coletaDadosAnunciante, se não estiver
        #  na mesma ordem vai trazer o nome das colunas na ordem errada 
        columns = ['titulo', 'preco', 'qtdVendida', 'linkVendedor', 'classificacaoVendedor', 'marca', 'sku', 'categoria', 'link']
        planilha = pd.DataFrame(lista_valores, columns=columns)
        #Salva a pesquisa realizada com o nome de planilhaGerada no formato CSV separada por ;
        planilha.to_csv('pesquisaAnuncianteMercadoLivre.csv', index=False, sep=';', encoding='utf-8')