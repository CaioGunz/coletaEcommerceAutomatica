import os
import tkinter as tk
import customtkinter
from classes.pesquisaAnunciosMl.pesquisaAnunciosML import pesquisaMercadoLivre


class janelas:
    
    def __init__(self, root):
        self.root = root
        self.root.title('Gunz Program')
        
        self.botaoPesquisaML = customtkinter.CTkButton(self.root, text='Pesquisa Mercado Livre', command=self.pesquisaMercadoLivre)
        self.botaoPesquisaML.grid(row=1, column=2, pady=10)
        
    def pesquisaMercadoLivre(self):
        
        #Fecha a pagina inicial quando aberta a pagina de pesquisa
        self.root.withdraw()
        
        #Cria a pagina de pesquisa
        self.rootPesquisaML = tk.Toplevel()
        self.rootPesquisaML.title('Pesquisa Mercado Livre')
        self.rootPesquisaML.resizable(width=False, height=False)
        self.rootPesquisaML.geometry('500x300')
        self.iconeJanelas(self.rootPesquisaML)
        
        #Label para entrada de link
        self.labelEntradaDeLink = tk.Label(self.rootPesquisaML, text='Insira o Link aqui', font=('Arial', 12, 'bold'))
        self.labelEntradaDeLink.grid(row=1, column=1, pady=10)
        
        #Entry Entrada de link
        self.inputEntradaLink = tk.Entry(self.rootPesquisaML)
        self.inputEntradaLink.grid(row=1, column=2, pady=10, ipadx=70)
        
        #Label para coleta da categoria
        self.labelColetaCategoria = tk.Label(self.rootPesquisaML, text='Insira a categoria pesquisada', font=('Arial', 12, 'bold'))
        self.labelColetaCategoria.grid(row=2, column=1, pady=10)
        
        #Input Coleta Categoria
        self.inpuColetaCategoria = tk.Entry(self.rootPesquisaML)
        self.inpuColetaCategoria.grid(row=2, column=2, pady=10, ipadx=40)
        
        #Botao inicia a pesquisa
        self.botaoIniciaPesquisa = customtkinter.CTkButton(self.rootPesquisaML, text='Inicia Pesquisa', command=self.coletaDadosParaPesquisa)
        self.botaoIniciaPesquisa.grid(row=3, column=2, pady=10)
        
        
        #Botao voltar pagina inicial
        self.botaoVoltaPaginaInicial = customtkinter.CTkButton(self.rootPesquisaML, text='Volta Pagina Inicial', command=self.voltarPaginaInicial)
        self.botaoVoltaPaginaInicial.grid(row=5, column=1, pady=10)
    
    def coletaDadosParaPesquisa(self):
        linkColetado = self.inputEntradaLink.get()
        categoria = self.inpuColetaCategoria.get()
        
        pesquisaAnuncio = pesquisaMercadoLivre(link=linkColetado, categoria=categoria)
        pesquisaAnuncio.novoModeloColeta()
    
    def voltarPaginaInicial(self):
        self.rootPesquisaML.destroy()
        
        self.root.deiconify()
        
    
    def iconeJanelas(self, root):
        icon_path = os.path.join(os.path.dirname(__file__), 'assets', 'icon', 'logoGunzComEscrita.ico')
        if os.path.exists(icon_path):
            root.iconbitmap(icon_path)
        else:
            print(f'Error: O arquivo do icone nao foi encontrado no caminho: {icon_path}')
            print('Verificar com o Administrador do Sistema')        
    

def main():
    root = tk.Tk()
    app = janelas(root)
    root.resizable(width=False, height=False)
    root.geometry('500x300')
    icon_path = os.path.join(os.path.dirname(__file__), 'assets', 'icon', 'logoGunzComEscrita.ico')
    if os.path.exists(icon_path):
        root.iconbitmap(icon_path)
    else:
        print(f'Error: o arquivo de icone não foi encontrado no caminho: {icon_path}')
        print('Informe o ADMINISTRADOR do sistema')
    root.mainloop()
    
if __name__ == '__main__':
    main()