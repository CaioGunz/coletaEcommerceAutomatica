#Import das Libs usadas na classe
import pandas as pd
from bs4 import BeautifulSoup
from time import sleep
from classes.chamaDriver.chamaDriver import iniciaDriver
from selenium.common.exceptions import InvalidArgumentException
from tkinter import messagebox


#Cria uma lista fora da classe para salvar os dados
lista_valores = []

class pesquisaMercadoLivre(iniciaDriver):
    
    #Chama o driver da classe super classe e pega a categoria que foi adicionada no input da classe app
    def __init__(self, link, categoria):
        super().__init__(driver=None, link=link)
        self.categoria = categoria
        
    def coletaAnunciosML(self, file_name):
        
        #Limpa a lista para começar uma nova pesquisa
        lista_valores.clear()
        
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
            
            if not produtos:
                break
            
            #Abre um loop para cada 'li' coletado na variavel produtos
            for produto in produtos:
                sleep(0.5)
                #Variavel que coleta o link da tag 'a' da classe definida
                link = produto.find('a', attrs={'class': 'ui-search-item__group__element ui-search-link__title-card ui-search-link'})
                #Pega a categoria que foi inserida no input da classe app
                categoria = self.categoria

                '''Adiciona o link e a categoria, setando o 'href' no link conforme o BeatifulSoup determina e para
                 categoria ficar sempre em letra MAIUSCULA'''
                lista_valores.append([link['href'], categoria.upper()])
            
            #Coleta do link para proxima pagina fora do loop for    
            proximaPagina = site.find('a', attrs={'title': 'Seguinte'})
            
            if proximaPagina:
                #Pega o link da proxima pagina e adiciona a pesquisa para o driver pular a pagina
                proximaPaginaLink = proximaPagina['href']
                
                try:
                    self.driver.get(proximaPaginaLink)
                    sleep(0.5)
                except InvalidArgumentException as e:
                    #Chama a funcao para salvar os dados obtidos e fecha o navegador
                     self.salvarDados(file_name)
                     self.driver.close()
                     return
            
            else:
                #Se nao for encontrado nenhum link o Browser e fechado e emitido o alerta no console
                messagebox.showinfo(title="Alerta!!", message='Erro ao acessar a próxima página. Encerrando.')
                self.driver.close()
                break
        
        #Chama a funcao para salvar os dados obtidos
        self.salvarDados(file_name)
            
    #Funcao para salvar os dados gerados na pesquisa
    def salvarDados(self, file_name):  
        if self.driver is not None:
            '''Define o nome de todas as colunas pesquisadas. Obs: o nome entre ' ' vai seguir a 
              ordem que estiver no append da funcao coletaAnuncios, se não estiver
              na mesma ordem vai trazer o nome das colunas na ordem errada '''
            column = ['link', 'categoria']
            planilhaGerada = pd.DataFrame(lista_valores, columns=column)
            '''Salva o arquivo com o nome setado pelo usuario e separado por ; Obs: Se o nome for alterado por quebrar o codigo
               entao se for alterado deve ser alterado tambem na classe pesquisaAnuncianteML'''
            planilhaGerada.to_csv(file_name, index=False, sep=';')
            
            