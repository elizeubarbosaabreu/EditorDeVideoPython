from timestamp import now
from moviepy.editor import VideoFileClip

class Rotate:
        
        def __init__(self, video_path=""):
                self.video_path = video_path

        def portrait(self):

            clip = VideoFileClip(self.video_path)

            if clip.size[0]> clip.size[1]:
                    clip = clip.rotate(-90)
                    clip.write_videofile(f'saida/video_{now()}.mp4', fps=30, threads=1)

def main():
       paisagem_to_portrait_video = Rotate(video_path)
       paisagem_to_portrait_video.portrait()
       print("Video rotacionado com sucesso!")

if __name__ == "__main__":
       video_path = input("Caminho do vídeo para rotacionar: ")
       main()