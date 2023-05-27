import yt_dlp


def download_video(url):
    ydl = yt_dlp.YoutubeDL({'listformats': True})
    info = ydl.extract_info(url, download=False)
    # formats = get_available_formats(url)
    print("\n\n***********************\nIF VIDEO IS AVAILABLW WITH AUDIO THE TYPE 'NO'/'no' DURING AUDIO SELECTION\n***********************")
    video_format = int(input("Enter Video Format:\t"))
    audio_format = eval(input("Enter Audio Format:\t"))
    if isinstance(audio_format, int):
        ydl_opts = {
            'format': f"{video_format}+{audio_format}",
            'outtmpl': '%(title)s.%(ext)s'
        }
    else:
         ydl_opts = {
            'format': f"{video_format}",
            'outtmpl': '%(title)s.%(ext)s'
        }       
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


# Example usage
video_url = input('Enter Video Link:\t')
download_video(video_url)
