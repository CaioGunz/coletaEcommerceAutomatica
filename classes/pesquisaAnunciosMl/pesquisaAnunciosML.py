import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep


lista_valores = []

class iniciaDriver:
    
    def __init__(self, driver, link):
        self.driver = driver
        self.link = link
    
    def chamaDriver(self):
        user_agent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
                        "Mozilla/5.0 (compatible; msie 7.0; windows nt 5.0; trident/3.1)",
                        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.54 Safari/535.2",
                        "Mozilla/5.0 (windows; u; windows nt 6.1) applewebkit/537.1.1 (khtml, like gecko) chrome/37.0.830.0 safari/537.1.1",
                        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_4_11; ja-jp) AppleWebKit/533.16 (KHTML, like Gecko) Version/4.1 Safari/533.16",
                        "Mozilla/5.0 (compatible; msie 9.0; windows nt 5.1; trident/5.0; .net clr 1.5.85128.0)",
                        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.21 (KHTML, like Gecko) Chrome/19.0.1042.0 Safari/535.21",
                        "Mozilla/5.0 (Windows NT 6.2; rv:22.0) Gecko/20130405 Firefox/23.0",
                        "Mozilla/5.0 (windows; u; windows nt 5.2) applewebkit/533.1.1 (khtml, like gecko) chrome/23.0.822.0 safari/533.1.1",
                        "Mozilla/5.0 (windows nt 6.0; win64; x64; rv:7.2) gecko/20100101 firefox/7.2.1",
                        "Mozilla/5.0 (windows; u; windows nt 5.2) applewebkit/531.2.2 (khtml, like gecko) chrome/25.0.899.0 safari/531.2.2")
        
        option = webdriver.FirefoxOptions()
        option.add_argument(f'user-agent={user_agent}')
        servico = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=servico, options=option)
        
        if self.link:
            driver.get(self.link)
        
        return driver

class pesquisaMercadoLivre(iniciaDriver):
    
    def __init__(self, link, categoria):
        super().__init__(driver=None, link=link)
        self.categoria = categoria
        
    def novoModeloColeta(self):
        
        self.driver = self.chamaDriver()
        self.driver.get(self.link)
        
        while True:
            page_content = self.driver.page_source
            
            site = BeautifulSoup(page_content, 'html.parser')
            
            produtos = site.find_all('li', attrs={'class': 'ui-search-layout__item'})
            
            for produto in produtos:
                link = produto.find('a', attrs={'class': 'ui-search-item__group__element ui-search-link__title-card ui-search-link'})
                categoria = self.categoria

                lista_valores.append([link['href'], categoria])
                 
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
            
            