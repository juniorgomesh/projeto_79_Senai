# Importação da biblioteca gráfica
import tkinter as tk

# Importação de um seletor de arquivos
from tkinter import filedialog

# Função: Carregar os arquivos mp3
def carregar_arquivos():
    arquivos = filedialog.askopenfilename(
        title= "Selecione músicas",
        filetypes= [("Arquivos MP3", "*.mp3")]
    )
    
    # Limpa a lista antes de adicionar novos arquivos
    lista.delete(0, tk.END)
    
    # Percorre os arquivos selecionados
    
    for arquivo in arquivos:
        # Adiciona na lista visual
        lista.insert(tk.END, arquivo)