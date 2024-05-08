#Import das Libs utilizadas nessa classe
import os
import tkinter as tk
import customtkinter
import sys
import webbrowser
import warnings
import threading
from PIL import Image, ImageTk
from tkinter import messagebox, filedialog
from classes.pesquisaAnunciosMl.pesquisaAnunciosML import pesquisaMercadoLivre, pd
from classes.pesquisaAnuncianteMl.pesquisaAnuncianteML import pesquisaAnuncianteMl
from classes.chamaDriver.chamaDriver import iniciaDriver



class janelas:
    
    janelaAjudaAberta = False
    
    #Funcao __init__ que cria a primeira e principal janela do sistema com botoes
    def __init__(self, root):
        #Cria a janela root com o titulo de Gunz Program
        self.root = root
        self.root.title('Gunz Program')
        
        #Titulo Geral do aplicativo (Pagina Inicial)
        self.tituloAbaGeral = customtkinter.CTkLabel(self.root, text='WebScraping Ecommerce', font=('Arial', 22, 'bold'))
        self.tituloAbaGeral.place(x=110, y=20)
        
        #Botao para acessar a janela de Pesquisa anuncios mercado livre
        self.botaoPesquisaML = customtkinter.CTkButton(self.root, text='Pesquisa Mercado Livre', width=155, command=self.pesquisaMercadoLivre,
                                                       corner_radius= 32, fg_color='#008584')
        self.botaoPesquisaML.place(x=170, y=95)
        
        #Botao para acessar a janela Pesquisa Amazon
        self.botaoAmazon = customtkinter.CTkButton(self.root, text='Pesquisa Amazon', width=170, command=self.alertaBotaoPesquisaAmazon,
                                                       corner_radius= 32, fg_color='#008584')
        self.botaoAmazon.place(x=170, y=150)
        
        #Botao para acessar a janela de Ajuda
        self.botaoHelp = customtkinter.CTkButton(self.root, text="❔", command=self.telaHelp, width=10, height=10, fg_color='#008485', 
                                                hover_color='#008584', border_color='#fff', corner_radius=50, text_color='#fff')
        self.botaoHelp.place(x=460, y=10)
        
        self.apperance(root=self.root)
        
    #Função para setar a aparencia do sistema
    def apperance(self, root):
                    
        #Label com o nome Tema
        self.escritaModoAparencia = customtkinter.CTkLabel(root, bg_color='transparent', text_color=['#000', '#fff'], text="Tema:")
        self.escritaModoAparencia.place(x=10, y=230)
        
        #Lista com as 3 opcoes de temas: Dark, Light e System
        self.listaModoAparencia = customtkinter.CTkOptionMenu(root, values=['System', 'Dark', 'Light'], command=self.change_apm, corner_radius=32, fg_color='#008584')
        self.listaModoAparencia.place(x=10, y=260)
    
    #Funcao de comando para o botao de tema do sistema
    def change_apm(self, novaAparencia):
        #Instancia novo tema
        customtkinter.set_appearance_mode(novaAparencia)
    
    #Funcao que cria a janela de pesquisa do mercado livre        
    def pesquisaMercadoLivre(self):
        #Fecha a pagina inicial quando aberta a pagina de pesquisa
        self.root.withdraw()
        
        #Cria a pagina de pesquisa
        self.rootPesquisaML = customtkinter.CTkToplevel()
        self.rootPesquisaML.title('Pesquisa Mercado Livre')
        self.rootPesquisaML.resizable(width=False, height=False)
        self.rootPesquisaML.geometry('500x300')
        self.rootPesquisaML.after(200, lambda: self.rootPesquisaML.iconbitmap("assets/Gunz-3.ico"))
        
        #Titulo geral da pagina do Mercado Livre
        self.tituloAbaMercadoLivre = customtkinter.CTkLabel(self.rootPesquisaML, text='WebScraping Mercado Livre', font=('Arial', 22, 'bold'))
        self.tituloAbaMercadoLivre.place(x=110, y=20)
        
        #Label para vazio e assim posicionar o titulo corretamente
        self.vazioMercadoLivre = customtkinter.CTkLabel(self.rootPesquisaML, text='')
        self.vazioMercadoLivre.grid(row=1, column=1, pady=10)
        
        #Label para entrada de link
        self.labelEntradaDeLink = customtkinter.CTkLabel(self.rootPesquisaML, text='Insira o Link aqui', font=('Arial', 12, 'bold'))
        self.labelEntradaDeLink.grid(row=2, column=1, pady=10)
        
        #Entry Entrada de link
        self.inputEntradaLink = customtkinter.CTkEntry(self.rootPesquisaML, placeholder_text="Ex: https://www.mercadolivre.com", border_color='#008584')
        self.inputEntradaLink.grid(row=2, column=2, pady=10, ipadx=70)
        
        #Label para coleta da categoria
        self.labelColetaCategoria = customtkinter.CTkLabel(self.rootPesquisaML, text='Insira a categoria pesquisada', font=('Arial', 12, 'bold'))
        self.labelColetaCategoria.grid(row=3, column=1, pady=10, padx=5)
        
        #Input Coleta Categoria
        self.inpuColetaCategoria = customtkinter.CTkEntry(self.rootPesquisaML, placeholder_text="Ex: Celulares", border_color='#008584')
        self.inpuColetaCategoria.grid(row=3, column=2, pady=10, ipadx=40)
        
        #Botao inicia a pesquisa
        self.botaoIniciaPesquisa = customtkinter.CTkButton(self.rootPesquisaML, text='Inicia Pesquisa de Anuncios', command=self.coletaDadosParaPesquisa,
                                                       corner_radius= 32, fg_color='#008584')
        self.botaoIniciaPesquisa.grid(row=4, column=2, pady=10)
        
        #Botao inicia pesquisa anunciante
        self.botaoiniciaPesquisaAnunciante = customtkinter.CTkButton(self.rootPesquisaML, text='Inicia Pesquisa de Anunciante', command=self.coletaDadosAnuncianteML,
                                                       corner_radius= 32, fg_color='#008584')
        self.botaoiniciaPesquisaAnunciante.grid(row=5, column=2, pady=10)
        
        #Botao voltar pagina inicial
        self.botaoVoltaPaginaInicial = customtkinter.CTkButton(self.rootPesquisaML, text='Volta Pagina Inicial', command=self.voltarPaginaInicial,
                                                       corner_radius= 32, fg_color='#008584')
        self.botaoVoltaPaginaInicial.grid(row=6, column=2, pady=10)
        
        #Adiciona o protocolo de encerramento do sistema pela janela de pesquisa Mercado Livre
        self.rootPesquisaML.protocol("WM_DELETE_WINDOW", self.confirmarSaida)
    
    # Função para carregar e redimensionar imagens
    def carregarEDimensionarImagem(self,caminho, tamanho):
        imagem = Image.open(caminho)
        imagemRedimensionada = imagem.resize(tamanho)
        return ImageTk.PhotoImage(imagemRedimensionada)

    # Função para criar botões
    def criarBotaoHelp(self, master, imagem, comando):
        botao = customtkinter.CTkButton(master, image=imagem, command=comando,
                                        corner_radius=32, fg_color='transparent', hover_color='#008485', text=None,
                                        height=0, width=0)
        botao.pack(padx=(30, 0), side='left')

    #Função que cria uma janela de Help com informações do sistema
    def telaHelp(self, event=None):

        if janelas.janelaAjudaAberta:
            #Fecha a janela de ajuda se já estiver aberta
            self.janelaHelp.destroy()
            #Altera o estado da variável de controle
            self.janelaAjudaAberta = False
        else:
            #Cria a janela de ajuda se não estiver aberta
            self.janelaHelp = customtkinter.CTkToplevel(self.root)
            self.janelaHelp.title('Sobre')
            self.janelaHelp.resizable(width=False, height=False)
            self.janelaHelp.geometry('500x300')
            self.janelaHelp.after(200, lambda: self.janelaHelp.iconbitmap("assets/Gunz-3.ico"))
            
            if getattr(sys, 'frozen', False):
                # Em um executavel esse bloco deve ajustar as imagens para que sejam encontradas
                self.caminhoImagemGithub = os.path.join(sys._MEIPASS, 'assets', 'github.png')
                self.caminhoImagemLinkedin = os.path.join(sys._MEIPASS, 'assets', 'linkedin.png')
                self.caminhoImagemPortfolio = os.path.join(sys._MEIPASS, 'assets', 'portfolio.png')
                self.caminhoImagemPix = os.path.join(sys._MEIPASS, 'assets', 'qrCodePix.png')
            else:
                self.caminhoImagemGithub = './assets/github.png'
                self.caminhoImagemLinkedin = './assets/linkedin.png'
                self.caminhoImagemPortfolio = './assets/portfolio.png'
                self.caminhoImagemPix = './assets/qrCodePix.png'

            # Label sobre a versão do app
            self.labelInformacaoWebScraping = customtkinter.CTkLabel(self.janelaHelp, text="WebScraping E-Commerce - ver 1.0", font=('Arial', 16, 'bold'))
            self.labelInformacaoWebScraping.pack(pady=(80, 0))
            # Label sobre o autor do sistema
            self.labelInformacaoDesenvolvedor = customtkinter.CTkLabel(self.janelaHelp, text="Desenvolvido por Caio Araujo Ⓒ - 2024", font=('Arial', 14))
            self.labelInformacaoDesenvolvedor.pack(pady=(0, 10))
            
            warnings.filterwarnings("ignore", category=UserWarning)
            
            # Botão para acessar a Documentação
            self.botaoDocumentacao = customtkinter.CTkButton(self.janelaHelp, text='Documentação📃', command=self.acesseDocumentacao,
                                        corner_radius=32, fg_color='#008485', font=('Arial', 14, 'bold'))
            self.botaoDocumentacao.pack(padx=(0, 0), side='top')

            # Carrega e redimensiona imagens
            self.imagemGithub = self.carregarEDimensionarImagem(self.caminhoImagemGithub, (30, 30))
            self.imagemLinkedin = self.carregarEDimensionarImagem(self.caminhoImagemLinkedin, (30, 30))
            self.imagemPortfolio = self.carregarEDimensionarImagem(self.caminhoImagemPortfolio, (30, 30))
            self.imagemPix = self.carregarEDimensionarImagem(self.caminhoImagemPix, (100, 100))

            # Cria os botões
            self.criarBotaoHelp(self.janelaHelp, self.imagemGithub, self.acesseGithub)
            self.criarBotaoHelp(self.janelaHelp, self.imagemLinkedin, self.acesseLinkedin)
            self.criarBotaoHelp(self.janelaHelp, self.imagemPortfolio, self.acessePortfolio)
            self.criarBotaoHelp(self.janelaHelp, self.imagemPix, self.acesseDoacaoPix)
            
            warnings.filterwarnings("default", category=UserWarning)

            #Define a janela de ajuda como modal
            self.janelaHelp.grab_set()

            #Altera o estado da variável de controle
            self.janela_de_ajuda_aberta = True

    #Funcao que cria uma janela com o progresso da pesquisa sendo feita
    def telaProgresso(self):
        #Abre a janela de progresso da pesquisa
        self.janelaProgresso = customtkinter.CTkToplevel()
        self.janelaProgresso.title("Carregando...")
        self.janelaProgresso.geometry("400x150")
        self.janelaProgresso.after(200, lambda: self.janelaProgresso.iconbitmap("assets/Gunz-3.ico"))
        
        self.tituloJanelaProgresso = customtkinter.CTkLabel(self.janelaProgresso, text="Realizando a coleta de dados, não feche o sistema.\n Aguarde!!!", font=('Arial', 14, 'bold'))
        self.tituloJanelaProgresso.pack(pady=30, padx=20)
        
        #Adiciona a barra de progresso
        self.barraProgresso = customtkinter.CTkProgressBar(self.janelaProgresso, orientation='horizontal', mode='indeterminate', progress_color='#008485', width=330, height=10)
        self.barraProgresso.pack(padx=20)
        # Inicia a barra de progresso
        self.barraProgresso.start()
        
        # Torna a janela de progresso modal para impedir interação com a janela principal
        self.janelaProgresso.grab_set()
        
        return self.janelaProgresso, self.barraProgresso
            
    #Funcao com o link do GitHub    
    def acesseGithub(self):
        webbrowser.open('https://github.com/CaioGunz')
    
    #Funcao com o link do LinkedIn        
    def acesseLinkedin(self):
        webbrowser.open('https://www.linkedin.com/in/caiobarbosadearaujo/')
    
    #Funcao com o link do Portfolio        
    def acessePortfolio(self):
        webbrowser.open('https://caiogunz.github.io/portfolio-curriculo/')
    
    #Funcao com o link do PIX
    def acesseDoacaoPix(self):
        webbrowser.open('https://nubank.com.br/cobrar/enynq/661554fa-a284-4ee1-b85c-99e97e21bdc5')

    #Funcao com o link da Documentacao
    def acesseDocumentacao(self):
        webbrowser.open('https://caiogunz.github.io/coletaEcommerceAutomatica/')
    
    #Funcao para perguntar ao usuario se ele deseja encerrar o sistema
    def confirmarSaida(self):
    # Pergunta ao usuário se deseja realmente sair
        if messagebox.askokcancel("Sair", "Deseja encerrar? :("):
            # Se o usuário confirmar, fecha a janela de pesquisa
            self.rootPesquisaML.destroy()
            # Encerra o sistema
            sys.exit()
   
    #Funcao para gerar o alerta no botao de pesquisa Amazon
    def alertaBotaoPesquisaAmazon(self):
        
        messagebox.showinfo(title="Alerta!!", message='Pagina em construcao !!')
   
   #Funcao para iniciar a pesquisa de Anunciantes onde o comando é chamado no botaoiniciaPesquisaAnunciante
    def coletaDadosAnuncianteML(self):
        #Abre a janela de carregamento dos dados
        janelaProgresso, barraProgresso = self.telaProgresso()
        
        def executaPesquisa():
            # Abrir a janela de seleção de arquivo
            file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
            
            if file_path:
                # Chamada para iniciar a pesquisa com o arquivo selecionado
                pesquisaAnunciante = pesquisaAnuncianteMl(link='', categoria='', file_path=file_path)
                pesquisaAnunciante.pegaLink()
            
            #Para o carregamento dos dados e fecha a janela
            barraProgresso.stop()
            janelaProgresso.destroy()

        #Executa o codigo e faz com que a barra nao fique travada
        pesquisaThread = threading.Thread(target=executaPesquisa)
        pesquisaThread.start()
    
    #Funcao para iniciar a coleta de dados e iniciar a pesquisa baseado no link e categoria do input na pagina root
    def coletaDadosParaPesquisa(self):
        
        #Abre a janela de carregamento dos dados
        janelaProgresso, barraProgresso = self.telaProgresso()
        
        def executaColetaEPesquisa():
            #Coleta os dados inseridos no input de link e categoria
            linkColetado = self.inputEntradaLink.get()
            categoria = self.inpuColetaCategoria.get()
            
            #Define o nome do arquivo padrão
            default_file_name = 'pesquisaAnunciosMercadoLivre.csv'
            
            # Abre a janela de seleção de arquivo para salvar o arquivo a ser pesquisado
            file_path = filedialog.asksaveasfilename(defaultextension=".csv", initialfile=default_file_name, filetypes=[("CSV Files", "*.csv")])
            
            if file_path:
                #Atualiza o nome do arquivo com o valor escolhido pelo usuario
                default_file_name = os.path.basename(file_path)
                    
                #Chama a funcao de coletaAnunciosML com oo link e categoria selecionado
                pesquisaAnuncio = pesquisaMercadoLivre(link=linkColetado, categoria=categoria)        
                pesquisaAnuncio.coletaAnunciosML(file_name=file_path)

            #Para o carregamento dos dados e fecha a janela
            barraProgresso.stop()
            janelaProgresso.destroy()
        
        coletaTherad = threading.Thread(target=executaColetaEPesquisa)
        coletaTherad.start()
    
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
    root.after(200, lambda: root.iconbitmap("assets/Gunz-3.ico"))
    
    root.mainloop()

#Inicia o main
if __name__ == '__main__':
    main()