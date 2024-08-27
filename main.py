from addlogo import Logo
from fatiador import Fatiador
from youtubedownloader import Youtube
from addsrt import Legendar
from legendador import Transcriber
from rotate import Rotate
from timestamp import now


def baixar_video():
    url = input("url do vídeo do youtube: ")
    download = Youtube(url)
    download.Download()

def criar_video_curto(): 
    path_video = input("Onde está o vídeo para ser dividido: ") 
    passo = int(input("Qual o tamanho desejado dos vídeos curtos (15, 30, 60, 120): "))
    diretorio = input("Diretório onde desejas salvar os vídeos curtos: ")
    fatia = Fatiador(path_video=path_video, passo=passo, diretorio=diretorio)
    print(fatia.info())
    fatia.fatiador()

def adicionar_logotipo():
    path_video = input('Caminho relativo do vídeo: ')
    path_logo = input('Caminho relativo do logotipo: ')
    logotipo = Logo(path_video=path_video, path_logo=path_logo)
    logotipo.add_logo()

def gerar_legenda():
    input_video = input("Vídeo para ser legendado: ")
    max_words = int(input("Quantidade de palavras exibidas na tela (ideal 5): "))
    transcriber = Transcriber(input_video=input_video, max_words=max_words)
    print("Estamos usando a inteligência artificial para extrair legendas\naguarde...")
    transcriber.transcribe_to_srt()
    print("Legenda pronta para ser adicionada ao clip")

def adicionar_legenda():
    path_video = input("Caminho do vídeo a ser legendado: ")
    path_srt = input("Caminho da legenda o formato srt: ")
    adicionar_legenda = Legendar(path_video=path_video, path_srt=path_srt)
    adicionar_legenda.adicionar()

def rotacionar_video():
    video_path = input("Caminho do vídeo para rotacionar: ")
    paisagem_to_portrait_video = Rotate(video_path)
    paisagem_to_portrait_video.portrait()

def main():
    while True:
        print(35*"#")
        print("Escolha uma funcionalidade:")
        print("1. Baixar vídeo do YouTube")
        print("2. Criar vídeo curto")
        print("3. Adicionar logotipo ao vídeo")
        print("4. Gerar legenda")
        print("5. Adicionar legenda ao vídeo")
        print("6. Rotacionar vídeo")
        print("0. Sair")
        print(35*"#")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == "1":
            baixar_video()
        elif escolha == "2":
            criar_video_curto()
        elif escolha == "3":
            adicionar_logotipo()
        elif escolha == "4":
            gerar_legenda()
        elif escolha == "5":
            adicionar_legenda()
        elif escolha == "6":
            rotacionar_video()
        elif escolha == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
