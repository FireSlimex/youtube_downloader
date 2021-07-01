from pytube import YouTube

while True:
    try:
        YTLINK = input("Please Enter the YouTube Link here: ")
        SRC = YouTube(YTLINK)

        ys = SRC.streams.get_highest_resolution()

        print(f"Downloading the Video {SRC.title} with a length from {SRC.length} Seconds")
        ys.download(output_path="Downloads")
        print("Downloaded the Video in the Download Folder")
        break
    except:
        print("Retry please")
        pass

