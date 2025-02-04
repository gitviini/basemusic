from __future__ import unicode_literals
import yt_dlp as youtube_dl

def progress():
    print("progress")

try:
    # baixa yt_url para o mesmo diretório no qual o script é executado
    def download_audio(yt_url):
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([yt_url])
except Exception as erro:
    print(erro)