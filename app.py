import tkinter as tk
from PIL.Image import *
from tkinter import filedialog, messagebox
from addlogo import Logo
from fatiador import Fatiador
from youtubedownloader import Youtube
from addsrt import Legendar
from legendador import Transcriber
from rotate import Rotate

class VideoEditorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Editor de Vídeos")
        self.geometry("400x400")

        # Criando os botões para cada funcionalidade
        tk.Button(self, text="Baixar vídeo do YouTube", command=self.baixar_video).pack(pady=10)
        tk.Button(self, text="Criar vídeo curto", command=self.criar_video_curto).pack(pady=10)
        tk.Button(self, text="Adicionar logotipo ao vídeo", command=self.adicionar_logotipo).pack(pady=10)
        tk.Button(self, text="Gerar legenda", command=self.gerar_legenda).pack(pady=10)
        tk.Button(self, text="Adicionar legenda ao vídeo", command=self.adicionar_legenda).pack(pady=10)
        tk.Button(self, text="Rotacionar vídeo", command=self.rotacionar_video).pack(pady=10)
        tk.Button(self, text="Sair", command=self.quit).pack(pady=10)

    def baixar_video(self):
        url = tk.simpledialog.askstring("URL do vídeo", "Digite a URL do vídeo do YouTube:")
        if url:
            try:
                download = Youtube(url)
                download.Download()
                messagebox.showinfo("Sucesso", "Download concluído com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao baixar vídeo: {e}")

    def criar_video_curto(self): 
        path_video = filedialog.askopenfilename(title="Selecione o vídeo para ser dividido")
        passo = tk.simpledialog.askinteger("Tamanho do vídeo curto", "Qual o tamanho desejado dos vídeos curtos (15, 30, 60, 120):")
        diretorio = filedialog.askdirectory(title="Selecione o diretório para salvar os vídeos curtos")
        if path_video and passo and diretorio:
            try:
                fatia = Fatiador(path_video=path_video, passo=passo, diretorio=diretorio)
                fatia.fatiador()
                messagebox.showinfo("Sucesso", "Vídeos curtos criados com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao criar vídeos curtos: {e}")

    def adicionar_logotipo(self):
        path_video = filedialog.askopenfilename(title="Selecione o vídeo")
        path_logo = filedialog.askopenfilename(title="Selecione o logotipo")
        if path_video and path_logo:
            try:
                logotipo = Logo(path_video=path_video, path_logo=path_logo)
                logotipo.add_logo()
                messagebox.showinfo("Sucesso", "Logotipo adicionado com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao adicionar logotipo: {e}")

    def gerar_legenda(self):
        input_video = filedialog.askopenfilename(title="Selecione o vídeo para ser legendado")
        max_words = tk.simpledialog.askinteger("Máximo de palavras", "Quantidade de palavras exibidas na tela (ideal 5):")
        if input_video and max_words:
            try:
                transcriber = Transcriber(input_video=input_video, max_words=max_words)
                transcriber.transcribe_to_srt()
                messagebox.showinfo("Sucesso", "Legenda gerada com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao gerar legenda: {e}")

    def adicionar_legenda(self):
        path_video = filedialog.askopenfilename(title="Selecione o vídeo a ser legendado")
        path_srt = filedialog.askopenfilename(title="Selecione a legenda (formato SRT)")
        if path_video and path_srt:
            try:
                adicionar_legenda = Legendar(path_video=path_video, path_srt=path_srt)
                adicionar_legenda.adicionar()
                messagebox.showinfo("Sucesso", "Legenda adicionada com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao adicionar legenda: {e}")

    def rotacionar_video(self):
        video_path = filedialog.askopenfilename(title="Selecione o vídeo para rotacionar")
        if video_path:
            try:
                paisagem_to_portrait_video = Rotate(video_path)
                paisagem_to_portrait_video.portrait()
                messagebox.showinfo("Sucesso", "Vídeo rotacionado com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao rotacionar vídeo: {e}")

if __name__ == "__main__":
    app = VideoEditorApp()
    app.mainloop()
