from pytube import YouTube

ask = input("Link: ").strip()

stream = YouTube(ask)
folder = ("your folder")

print("Title: ", stream.title)

stream_down = stream.streams.get_highest_resolution()
stream_down.download(folder)