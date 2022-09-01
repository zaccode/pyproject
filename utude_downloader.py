# pip install pytube
# download video
# from pytube import YouTube

# link = "https://youtu.be/MguxxG7n6pk"
# utube1= YouTube(link)

# title = utube1.title
# # print(utube1.thumbnail_url)

# videos = utube1.streams.all()   #streams means resolution of the video
# vid = list(enumerate(videos))
# for i in vid:
#     print(i)
# print()
# strm = int(input("Enter the Resolution index no: "))
# videos[strm].download("utube")

# print(title + " download Successfully")

#Youtube Audio Download
from pytube import YouTube

link = "https://youtu.be/anGyMHsNEh0"
utube1= YouTube(link)

title = utube1.title
# print(utube1.thumbnail_url)

# videos = utube1.streams.all()   #get all format
videos = utube1.streams.filter(only_audio=True)   #only Audio
vid = list(enumerate(videos))
for i in vid:
    print(i)
print()
strm = int(input("Enter the Resolution index no: "))
videos[strm].download("utube")

print(title + " download Successfully")

#*****************
# #download complete playlist
# from pytube import Playlist
# py = Playlist("https://www.youtube.com/playlist?list=PLbGui_ZYuhigchy8DTw4pX4duTTpvqlh6")

# print(f'Downloading : {py.title}')
# vid = list(enumerate(py.videos))
# for i in vid:
#     print(i)

# for vid in py.videos: 
#     vid.streams.first().download("Django")
#     print(f'Downloading : {vid.title}')

# print("Playlist download Successfully")

    
