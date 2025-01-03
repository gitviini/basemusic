from __future__ import unicode_literals
import yt_dlp as youtube_dl

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

    def main():
        yt_url = "\
    https://www.youtube.com/watch?v=MoIvVdToAOw&list=RDEMOdoxonAT4dC80CkTOEKMYw&start_radio=1\
        "
        download_audio(yt_url)

    main()
except Exception as erro:
    print(erro)