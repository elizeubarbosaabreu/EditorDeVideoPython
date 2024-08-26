from addlogo import Logo
from fatiador import Fatiador
from youtubedownloader import Youtube
from addsrt import Legendar
from legendador import Transcriber
from timestamp import now


def baixar_video(url):
    download = Youtube(url)
    download.Download()

def criar_video_curto(path_video, passo):
    fatia = Fatiador(path_video=path_video, passo=passo)
    print(fatia.info())
    fatia.fatiador()

def adicionar_logotipo():
    pass

def gerar_legenda():
    pass

def adicionar_legenada():
    pass

def rotacionar_video():
    pass

def adicionar_texto():
    pass

def adicionar_gif():
    pass

def concatecenar_video():
    pass


def main():
    print(35*"#")
    path_video = input("Localização do video: ")
    passo = int(input("tamanho dos videos curtos em segundos: "))
    criar_video_curto(path_video, passo)

if __name__ == "__main__":
    main()
