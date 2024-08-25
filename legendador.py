from faster_whisper import WhisperModel
from moviepy.editor import VideoFileClip
from timestamp import now
class Transcriber:
    def __init__(self, model_size="tiny", max_words=5):
        self.model = WhisperModel(model_size)
        self.max_words = max_words
    
    def format_time(self, seconds):
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        seconds = int(seconds % 60)
        milliseconds = int((seconds % 1) * 1000)
        return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"
    
    def split_segment(self, segment_text, start_time, end_time):
        words = segment_text.split()
        segments = []
        total_words = len(words)
        time_per_word = (end_time - start_time) / total_words

        for i in range(0, total_words, self.max_words):
            part_words = words[i:i+self.max_words]
            part_start_time = start_time + i * time_per_word
            part_end_time = part_start_time + len(part_words) * time_per_word
            segments.append({
                "start_time": part_start_time,
                "end_time": part_end_time,
                "text": " ".join(part_words)
            })

        return segments
    
    def transcribe_to_srt(self, audio_file, output_srt):
        segments, _ = self.model.transcribe(audio_file)
        with open(output_srt, 'w') as texto:
            index = 1
            for segment in segments:
                start_time = segment.start
                end_time = segment.end
                split_segments = self.split_segment(segment.text, start_time, end_time)

                for split_segment in split_segments:
                    texto.write(f"{index}\n")
                    texto.write(f"{self.format_time(split_segment['start_time'])} --> {self.format_time(split_segment['end_time'])}\n")
                    texto.write(f"{split_segment['text']}\n\n")
                    index += 1

        print("Legenda pronta")


if __name__ == '__main__':    
    
    model = WhisperModel("tiny")

    input_video = input("Video para ser legendado: ")

    # Carrega o vídeo
    video = VideoFileClip(input_video)

    # Extrai o áudio e salva como .mp3

    video.audio.write_audiofile('.audio.mp3')
    transcriber = Transcriber(max_words=5)
    
    transcriber.transcribe_to_srt(".audio.mp3", f"saida/legenda_{now()}.srt")


    print("Legenda pronta para ser adicionada ao clip")