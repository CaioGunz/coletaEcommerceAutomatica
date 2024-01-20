#Import das Libs usadas na classe
import pandas as pd
from bs4 import BeautifulSoup
from time import sleep
from classes.chamaDriver.chamaDriver import iniciaDriver

#Cria uma lista fora da classe para salvar os dados
lista_valores = []

class pesquisaMercadoLivre(iniciaDriver):
    
    #Chama o driver da classe super classe e pega a categoria que foi adicionada no input da classe app
    def __init__(self, link, categoria):
        super().__init__(driver=None, link=link)
        self.categoria = categoria
        
    def coletaAnuncios(self):
        
        #Pega o driver da classe chamaDriver e adiciona o link que foi inserido no input de link da classe app
        self.driver = self.chamaDriver()
        self.driver.get(self.link)
      
        while True:
            #Pega o page_source e tranfosma na variavel page_content usando BeautifulSoup
            page_content = self.driver.page_source
            
            #Faz a leitura da estrutura da pagina 
            site = BeautifulSoup(page_content, 'html.parser')
            
            #pega todos os elementos que estão em uma 'li' da classe definida
            produtos = site.find_all('li', attrs={'class': 'ui-search-layout__item'})
            
            #Abre um loop para cada 'li' coletado na variavel produtos
            for produto in produtos:
                #Variavel que coleta o link da tag 'a' da classe definida
                link = produto.find('a', attrs={'class': 'ui-search-item__group__element ui-search-link__title-card ui-search-link'})
                #Pega a categoria que foi inserida no input da classe app
                categoria = self.categoria

                #Adiciona o link e a categoria, setando o 'href' no link conforme o BeatifulSoup determina e para
                # categoria ficar sempre em letra MAIUSCULA
                lista_valores.append([link['href'], categoria.upper()])
            
            #Coleta do link para proxima pagina fora do loop for    
            proximaPagina = site.find('a', attrs={'title': 'Seguinte'})
            
            if proximaPagina:
                #Pega o link da proxima pagina e adiciona a pesquisa para o driver pular a pagina
                proximaPaginaLink = proximaPagina['href']
                self.driver.get(proximaPaginaLink)
                sleep(1)
            else:
                #Se nao for encontrado nenhum link o Browser e fechado e emitido o alerta no console
                print('Proxima Pagina Nao Encontrada!!! ENCERRANDO')
                self.driver.close()
                break
        #Chama a funcao para salvar os dados obtidos
        self.salvarDados()
            
    #Funcao para salvar os dados gerados na pesquisa
    def salvarDados(self):  
        if self.driver is not None:
            #Define o nome de todas as colunas pesquisadas. Obs: o nome entre ' ' vai seguir a 
            # ordem que estiver no append da funcao coletaAnuncios, se não estiver
            #  na mesma ordem vai trazer o nome das colunas na ordem errada 
            column = ['link', 'categoria']
            planilhaGerada = pd.DataFrame(lista_valores, columns=column)
            #Salva o arquivo com o nome de planilha.csv separada por ; Obs: Se o nome for alterado por quebrar o codigo
            # entao se for alterado deve ser alterado tambem na classe pesquisaAnuncianteML
            planilhaGerada.to_csv('planilha.csv', index=False, sep=';')
            
            