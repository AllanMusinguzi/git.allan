import yt_dlp

#Enter the url for the download
url = input("Enter video url: ")
download_directory = '/home/allan/Home/Videos/movies'

ydl_opts = {
    'outtmpl' : f'{download_directory}/%(title)s.%(ext)s',
    'format':'best' #best or worst for video quality
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Video downloaded successfully!")
