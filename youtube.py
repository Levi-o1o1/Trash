from yt_dlp import YoutubeDL
# paste here your video link :
url = ""


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
ydl_opts =  { 'format': 'bestvideo+bestaudio/best','merge_output_format': 'mp4',}
ydl_opts ={ 'outtmpl': '%(title)s.%(ext)s',}
with YoutubeDL(ydl_opts) as ydl:ydl.download([url])

# Note: you need to install yt_dlp library first
# HOW TO INSTALL:
# pip install yt_dlp 
# if show any erorr like module not found so you need .venv python virtual inverment 