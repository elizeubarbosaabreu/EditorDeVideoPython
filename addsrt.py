import ffmpeg
from timestamp import now

class Legendar:

    def __init__(self, path_video="", path_srt=""):
        self.path_video = path_video
        self.path_srt = path_srt

    def adicionar(self):
        try:
            # Comando para adicionar legenda ao vídeo e manter o áudio original
            ffmpeg.input(self.path_video)\
                .output(f"legenda_{now()}.mp4", vf=f"subtitles={self.path_srt}", acodec="copy")\
                .run(overwrite_output=True)            
        except ffmpeg.Error as e:
            return (f"Ocorreu um erro ao processar o vídeo: {e}")


        
def main():
    path_video = input("Caminho do vídeo a ser legendado: ")
    path_srt = input("Caminho da legenda o formato srt: ")
    adicionar_legenda = Legendar(path_video=path_video, path_srt=path_srt)
    adicionar_legenda.adicionar()

if __name__ == "__main__":
    main()
