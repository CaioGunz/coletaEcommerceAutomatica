import pandas as pd
from bs4 import BeautifulSoup
from time import sleep
from classes.chamaDriver.chamaDriver import iniciaDriver

lista_valores = []

class pesquisaMercadoLivre(iniciaDriver):
    
    def __init__(self, link, categoria):
        super().__init__(driver=None, link=link)
        self.categoria = categoria
        
    def coletaAnuncios(self):
        
        self.driver = self.chamaDriver()
        self.driver.get(self.link)
      
        
        while True:
            page_content = self.driver.page_source
            
            site = BeautifulSoup(page_content, 'html.parser')
            
            produtos = site.find_all('li', attrs={'class': 'ui-search-layout__item'})
            
            for produto in produtos:
                link = produto.find('a', attrs={'class': 'ui-search-item__group__element ui-search-link__title-card ui-search-link'})
                categoria = self.categoria

                lista_valores.append([link['href'], categoria.upper()])
                 
            proximaPagina = site.find('a', attrs={'title': 'Seguinte'})
            if proximaPagina:
                proximaPaginaLink = proximaPagina['href']
                self.driver.get(proximaPaginaLink)
                sleep(1)
            else:
                print('Proxima Pagina Nao Encontrada!!! ENCERRANDO')
                self.driver.close()
                break
        self.salvarDados()
            

    def salvarDados(self):
        if self.driver is not None:
            column = ['link', 'categoria']
            planilhaGerada = pd.DataFrame(lista_valores, columns=column)
            planilhaGerada.to_csv('planilha.csv', index=False, sep=';')
            
            