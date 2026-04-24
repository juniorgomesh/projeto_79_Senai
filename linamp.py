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
