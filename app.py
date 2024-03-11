#Import das Libs utilizadas nessa classe
import os
import tkinter as tk
import customtkinter
from tkinter import messagebox
from classes.pesquisaAnunciosMl.pesquisaAnunciosML import pesquisaMercadoLivre
from classes.pesquisaAnuncianteMl.pesquisaAnuncianteML import pesquisaAnuncianteMl
from classes.chamaDriver.chamaDriver import iniciaDriver



class janelas:
    
    #Funcao __init__ que cria a primeira e principal janela do sistema com botoes
    def __init__(self, root):
        #Cria a janela root com o titulo de Gunz Program
        self.root = root
        self.root.title('Gunz Program')

        
        #Titulo Geral do aplicativo (Pagina Inicial)
        self.tituloAbaGeral = customtkinter.CTkLabel(self.root, text='WebScraping Ecommerce', font=('Arial', 24))
        self.tituloAbaGeral.place(x=110, y=20)
        
        #Botao para acessar a janela de Pesquisa anuncios mercado livre
        self.botaoPesquisaML = customtkinter.CTkButton(self.root, text='Pesquisa Mercado Livre', width=155, command=self.pesquisaMercadoLivre,
                                                       corner_radius= 32, fg_color='transparent',
                                                        hover_color='#47494d', border_color='#008584', border_width=2, text_color='#75787d')
        self.botaoPesquisaML.place(x=170, y=95)
        
        #Botao para acessar a janela Pesquisa Amazon
        self.botaoAmazon = customtkinter.CTkButton(self.root, text='Pesquisa Amazon', width=170, command=self.alertaBotaoPesquisaAmazon,
                                                       corner_radius= 32, fg_color='transparent',
                                                        hover_color='#47494d', border_color='#008584', border_width=2, text_color='#75787d')
        self.botaoAmazon.place(x=170, y=150)
        
        self.apperance(root=self.root)
        
    #Função para setar a aparencia do sistema
    def apperance(self, root):
                    
        #Label com o nome Tema
        self.escritaModoAparencia = customtkinter.CTkLabel(root, bg_color='transparent', text_color=['#000', '#fff'], text="Tema:")
        self.escritaModoAparencia.place(x=50, y=230)
        
        #Lista com as 3 opcoes de temas: Dark, Light e System
        self.listaModoAparencia = customtkinter.CTkOptionMenu(root, values=['System', 'Dark', 'Light'], command=self.change_apm, corner_radius=32, fg_color='#008584')
        self.listaModoAparencia.place(x=50, y=260)
    
    #Funcao de comando para o botao de tema do sistema
    def change_apm(self, nova_aparencia):
        #Instancia novo tema
        customtkinter.set_appearance_mode(nova_aparencia)
        
        #Funcao para setar o icone em cada janela aberta
    def iconeJanelas(self, root):
        #Procura o icone usando a lib os
        icon_path = os.path.join(os.path.dirname(__file__), 'assets', 'icon', 'Gunz-3.ico')
        if os.path.exists(icon_path):
            try:
                #Adiciona o icone na janela aberta
                root.iconbitmap(icon_path)
            except Exception as e:
                print(f'Erro ao carregar o icone: {e}')
        else:
            print(f'Error: O arquivo do icone nao foi encontrado no caminho: {icon_path}')
            print('Verificar com o Administrador do Sistema')      
    
    #Funcao que cria a janela de pesquisa do mercado livre        
    def pesquisaMercadoLivre(self):
        #Fecha a pagina inicial quando aberta a pagina de pesquisa
        self.root.withdraw()
        
        #Cria a pagina de pesquisa
        self.rootPesquisaML = customtkinter.CTkToplevel()
        self.rootPesquisaML.title('Pesquisa Mercado Livre')
        self.rootPesquisaML.resizable(width=False, height=False)
        self.rootPesquisaML.geometry('500x300')
        self.iconeJanelas(root=self.rootPesquisaML)
                
        #Titulo geral da pagina do Mercado Livre
        self.tituloAbaMercadoLivre = customtkinter.CTkLabel(self.rootPesquisaML, text='WebScraping Mercado Livre', font=('Arial', 24))
        self.tituloAbaMercadoLivre.place(x=110, y=20)
        
        #Label para vazio e assim posicionar o titulo corretamente
        self.vazioMercadoLivre = customtkinter.CTkLabel(self.rootPesquisaML, text='')
        self.vazioMercadoLivre.grid(row=1, column=1, pady=10)
        
        #Label para entrada de link
        self.labelEntradaDeLink = customtkinter.CTkLabel(self.rootPesquisaML, text='Insira o Link aqui', font=('Arial', 12, 'bold'))
        self.labelEntradaDeLink.grid(row=2, column=1, pady=10)
        
        #Entry Entrada de link
        self.inputEntradaLink = customtkinter.CTkEntry(self.rootPesquisaML)
        self.inputEntradaLink.grid(row=2, column=2, pady=10, ipadx=70)
        
        #Label para coleta da categoria
        self.labelColetaCategoria = customtkinter.CTkLabel(self.rootPesquisaML, text='Insira a categoria pesquisada', font=('Arial', 12, 'bold'))
        self.labelColetaCategoria.grid(row=3, column=1, pady=10, padx=5)
        
        #Input Coleta Categoria
        self.inpuColetaCategoria = customtkinter.CTkEntry(self.rootPesquisaML)
        self.inpuColetaCategoria.grid(row=3, column=2, pady=10, ipadx=40)
        
        #Botao inicia a pesquisa
        self.botaoIniciaPesquisa = customtkinter.CTkButton(self.rootPesquisaML, text='Inicia Pesquisa de Anuncios', command=self.coletaDadosParaPesquisa,
                                                       corner_radius= 32, fg_color='transparent',
                                                        hover_color='#47494d', border_color='#008584', border_width=2, text_color='#75787d')
        self.botaoIniciaPesquisa.grid(row=4, column=2, pady=10)
        
        #Botao inicia pesquisa anunciante
        self.botaoiniciaPesquisaAnunciante = customtkinter.CTkButton(self.rootPesquisaML, text='Inicia Pesquisa de Anunciante', command=self.coletaDadosAnuncianteML,
                                                       corner_radius= 32, fg_color='transparent',
                                                        hover_color='#47494d', border_color='#008584', border_width=2, text_color='#75787d')
        self.botaoiniciaPesquisaAnunciante.grid(row=5, column=2, pady=10)
        
        #Botao voltar pagina inicial
        self.botaoVoltaPaginaInicial = customtkinter.CTkButton(self.rootPesquisaML, text='Volta Pagina Inicial', command=self.voltarPaginaInicial,
                                                       corner_radius= 32, fg_color='transparent',
                                                        hover_color='#47494d', border_color='#008584', border_width=2, text_color='#75787d')
        self.botaoVoltaPaginaInicial.grid(row=6, column=2, pady=10)
   
    #Funcao para gerar o alerta no botao de pesquisa Amazon
    def alertaBotaoPesquisaAmazon(self):
       messagebox.showinfo(title="Alerta!!", message='Pagina em construcao !!')
   
   
   #Funcao para iniciar a pesquisa de Anunciantes onde o comando é chamado no botaoiniciaPesquisaAnunciante
    def coletaDadosAnuncianteML(self):
        pesquisaAnunciante = pesquisaAnuncianteMl(link='', categoria='')
        pesquisaAnunciante.pegaLink()
    
    #Funcao para iniciar a coleta de dados e iniciar a pesquisa baseado no link e categoria do input na pagina root
    def coletaDadosParaPesquisa(self):
        #Coleta os dados inseridos no input de link e categoria
        linkColetado = self.inputEntradaLink.get()
        categoria = self.inpuColetaCategoria.get()
        
        #Chama a funcao de coletaAnunciosML com oo link e categoria selecionado
        pesquisaAnuncio = pesquisaMercadoLivre(link=linkColetado, categoria=categoria)        
        pesquisaAnuncio.coletaAnunciosML()
    
    #Funcao dos botoes de voltar para pagina inicial 
    def voltarPaginaInicial(self):
        self.rootPesquisaML.destroy()
        
        self.root.deiconify()
        
  
    
#Funcao main para iniciar o sistema
def main():
    #Cria a janela principal
    root = customtkinter.CTk()
    app = janelas(root)
    #Fixa o tamanho da janela sem deixar aumentar com o mouse
    root.resizable(width=False, height=False)
    #Define o tamanho da janela
    root.geometry('500x300')
    icon_path = os.path.join(os.path.dirname(__file__), 'assets', 'icon', 'Gunz-3.ico')
    if os.path.exists(icon_path):
        try:
            #Adiciona o icone na janela aberta
            root.iconbitmap(icon_path)
        except Exception as e:
            print(f'Erro ao carregar o icone: {e}')
    else:
        print(f'Error: O arquivo do icone nao foi encontrado no caminho: {icon_path}')
        print('Verificar com o Administrador do Sistema')        
    
    root.mainloop()

#Inicia o main
if __name__ == '__main__':
    main()