from __future__ import unicode_literals
import youtube_dl

i = input('enter youtube link: ')
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
w=youtube_dl.YoutubeDL(ydl_opts)
w.download([i])
