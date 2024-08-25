import yt_dlp
from timestamp import now
from yt_dlp.utils import download_range_func

class Youtube:

    def __init__(self, url=""):
        self.url = url

    def Download(self):

        yt_opts = {
            'verbose': True,
            'force_keyframes_at_cuts': True,
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',  # Especifica vídeo e áudio em MP4
            'postprocessors': [{  # Inclui um pós-processador para mesclar vídeo e áudio
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }],
        }

        with yt_dlp.YoutubeDL(yt_opts) as ydl:
            ydl.download(self.url)

def main():
    baixar_video = Youtube(url)
    baixar_video.Download()

if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=TJDJoD5Upp0&t=573s"
    main()