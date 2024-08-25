from moviepy.editor import *
from timestamp import now
from PIL.Image import *

class Logo:

    def __init__(self, posx=100, posy=100, width=100, height=100, path_video="", path_logo=""):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.path_video = path_video
        self.path_logo = path_logo

    def add_logo(self):
        # Carregar o vídeo e redimensioná-lo (se necessário)
        shorts = VideoFileClip(self.path_video)
        
        # Carregar o logotipo, definir sua duração e redimensioná-lo
        logotipo = ImageClip(self.path_logo).set_duration(shorts.duration)\
                    .margin(right=self.posx, top=self.posy, opacity=0)\
                    .set_pos(("right", "top"))\
                    .resize((self.width, self.height))  # Redimensionar para a largura e altura especificadas

        # Combinar o vídeo com o logotipo
        video_com_logo = CompositeVideoClip([shorts, logotipo], size=shorts.size)

        # Salvar o vídeo com o logotipo aplicado
        video_com_logo.write_videofile(f"saida/video_com_logo_{now()}.mp4", fps=30, threads=1)

def main():
    path_video = input('Caminho relativo do vídeo: ')
    path_logo = input('Caminho relativo do logotipo: ')
    logotipo = Logo(path_video=path_video, path_logo=path_logo)
    logotipo.add_logo()

if __name__ == "__main__":
    main()
