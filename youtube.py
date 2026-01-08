from yt_dlp import YoutubeDL
# in url paste here your video link :
url = ""











# ignore this:
ydl_opts =  { 'format': 'bestvideo+bestaudio/best','merge_output_format': 'mp4',}
ydl_opts ={ 'outtmpl': '%(title)s.%(ext)s',}
with YoutubeDL(ydl_opts) as ydl:ydl.download([url])