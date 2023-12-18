import pandas as pd
from time import sleep
from bs4 import BeautifulSoup
from classes.chamaDriver.chamaDriver import iniciaDriver

lisra_valores = []
lista_link = []

class pesquisaAnuncianteML(iniciaDriver):
    
    links = pd.read_csv('planilha.csv', sep=';')
    
    
    def __init__(self, link, categoria):
        super().__init__(driver=None, link=link)
        self.categoria = categoria
    
    
    def coletaAnunciantes(self):
        
        
        while True:
            page_content = self.driver.page_source
            
            site = BeautifulSoup(page_content, 'html.parser')
            
        
        return self.pegaLink()
    
    
    def pegaLink(self):
        
        self.driver = self.chamaDriver()
        
        
        for index, row in self.links.iterrows():
            link = row['link']
            categoria = row['categoria']
            lista_link.append(link)
        
        
            try:
                sleep(1)
                self.driver.get(link)
                self.coletaAnunciantes()
            except Exception as e:
                print('Erro desconhecido ao acessar o link: ', str(e))
                sleep(5)
                break
        
    
    def salvaDados(self):
        columns = []
        planilha = pd.DataFrame(lisra_valores, columns=columns)
        planilha.to_csv('planilhaGerada.csv', index=False, sep=';', encoding='utf-8')