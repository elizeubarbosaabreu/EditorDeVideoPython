from moviepy.editor import *
from timestamp import now

class Fatiador:

    def __init__(self, path_video='', inicio=0, passo=15):
        self.path_video = path_video
        self.inicio = inicio
        self.passo = passo

    def info(self):
        
        video = VideoFileClip(self.path_video)
        return (
            f'''
            {25 * '#'}   
            Nome: {video.filename}
            Duração: {video.duration}
            Tamanho: {video.size}
            Aspecto: {video.aspect_ratio}
            FPS: {video.fps}
            {25 * '#'} 
            ''')
        

    def fatiador(self): 
        
        video = VideoFileClip(self.path_video)

        while(self.fim<= video.duration):
            try:
                shorts = video.subclip(self.inicio, self.fim)    
                shorts.resize(width=480).fx(vfx.fadeout, 1).fx(vfx.fadein, 1)

                filename = f'saida/video_{now()}.mp4'

                shorts.write_videofile(filename, fps=30, threads=1)
                self.inicio += self.passo
                self.fim += self.passo
                if self.fim > video.duration:
                    self.fim = video.duration
            except Exception as e:
                break
        
def main():

    path_video = r'/home/elizeu/Área de trabalho/VideoEditor/arquivos/Unicesumar Institucional-(1080p24).mp4'
    fatia = Fatiador(path_video=path_video)
    print(fatia.info())

if __name__ == '__main__':
    main()
