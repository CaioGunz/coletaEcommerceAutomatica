#Import das Libs usadas na classe
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

class iniciaDriver:
    
    #__init__ cria os atributos driver e link que vai ser usados pelas outras classes
    def __init__(self, driver, link):
        self.driver = driver
        self.link = link
    
    #Funcao para criar o Browser quando for chamado pelas classes
    def chamaDriver(self):
        
        #User-agent utilizado para contornar o erro de HTTP 403, quanto mais user_agent tiver 
        # menor e a chance do erro acontecer
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
        
        #Adiciona os options setados para que o Browser rode com limitações ou nao
        option = webdriver.ChromeOptions()
        
        #Adiciona os user_agent 
        option.add_argument(f'user-agent={user_agent}')
        
        #Oculta o driver enquanto o Scrypt estiver funcionando
        #option.add_argument('--headless')
        
        #Faz a instalacao automatica do Browser selecionado evitando assim ter que ficar baixando manualmente
        # e adiciona o service e options no Browser 
        servico = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=servico, options=option)
        
        #Se existir link vai abrir o driver no link setado
        if self.link:
            driver.get(self.link)
        
        #Retorna o driver
        return driver