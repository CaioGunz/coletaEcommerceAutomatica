import pandas as pd
from time import sleep
from classes.chamaDriver.chamaDriver import iniciaDriver, By

lista_valores = []
lista_link = []

class pesquisaAnuncianteML(iniciaDriver):
    
    links = pd.read_csv('C:/Users/caio.araujo/Desktop/myProjects/coletaEcommerceAutomatica/planilha.csv', sep=';')
    
    
    def __init__(self, link, categoria):
        super().__init__(driver=None, link=link)
        self.categoria = categoria
    
    
    def coletaAnunciantes(self):
        
        
        while True:
            
            titulo = self.driver.find_element(By.XPATH, '//h1[@class="ui-pdp-title"]').text
            preco = self.driver.find_element(By.XPATH, '//div[@class="ui-pdp-price__second-line"]//span[@class="andes-money-amount__fraction"]').text
            qtdVendida = self.driver.find_element(By.XPATH, '//span[@class="ui-pdp-subtitle"]').text
            linkVendedor = self.driver.find_element(By.XPATH, '//a[@class="ui-pdp-media__action ui-box-component__action"]').get_attribute('href')
            classificacaoVendedor = self.driver.find_element(By.XPATH, '//p[@class="ui-seller-info__status-info__title ui-pdp-seller__status-title"]').text
            marca = self.driver.find_element(By.XPATH, '//th[contains(., "Marca")]/following-sibling::td//span[@class="andes-table__column--value"]').text
            sku = self.driver.find_element(By.XPATH, '//th[contains(., "Modelo")]/following-sibling::td//span[@class="andes-table__column--value"]').text
            categoria = self.categoria
            link = lista_link
            
            lista_valores.append([titulo, preco, qtdVendida, linkVendedor, classificacaoVendedor, marca, sku, categoria, link])
            
            
            return self.pegaLink()
        salvaDados()
    
    
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
        columns = ['titulo', 'preco', 'qtdVendida', 'linkVendedor', 'classificacaoVendedor', 'marca', 'sku', 'categoria', 'link']
        planilha = pd.DataFrame(lista_valores, columns=columns)
        planilha.to_csv('planilhaGerada.csv', index=False, sep=';', encoding='utf-8')