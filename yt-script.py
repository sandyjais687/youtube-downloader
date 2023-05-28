import yt_dlp

def download_link(conf_data, url):
    with yt_dlp.YoutubeDL(conf_data) as ydl:
        ydl.download([url])
    quit()


def retrive_info(url):
    ydl = yt_dlp.YoutubeDL({'listformats': True})
    info = ydl.extract_info(url, download=False)
    # formats = get_available_formats(url)
    user_opt=int(input("""
    *****************************************************************
    What do you want to download. Enter Respective Number.
    1.\tDownload audio only.
    2.\tDownload video only(If Audio is already merged in video).
    3.\tDownload video and audio.
    *****************************************************************
    
    Enter choice :\t"""))


    if user_opt == 1:
        audio_format = int(input("Enter Audio Format:\t"))
        ydl_opts = {
            'format': f"{audio_format}",
            'outtmpl': '%(title)s.%(ext)s'
        }
        download_link(ydl_opts,url)

    if user_opt == 2:
        video_format = int(input("Enter Video Format:\t"))
        ydl_opts = {
            'format': f"{video_format}",
            'outtmpl': '%(title)s.%(ext)s'
        }
        download_link(ydl_opts,url)

    if user_opt == 3:
        video_format = int(input("Enter Video Format:\t"))
        audio_format = int(input("Enter Audio Format:\t"))
        ydl_opts = {
            'format': f"{video_format}+{audio_format}",
            'outtmpl': '%(title)s.%(ext)s'
        }
        download_link(ydl_opts,url)

    else:
        print("Please enter valid choice....\n\n\n")
        return retrive_info(url)

      
    # with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    #     ydl.download([url])


#main program
video_url = input('Enter Video Link:\t')
retrive_info(video_url)
