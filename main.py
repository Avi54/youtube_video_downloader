import youtube_dl
import os
import requests

def check_video_url(video_url):
    request = requests.get(video_url)
    return request.status_code == 200

def download():
    video_playlist = input('video or playlist link: ')

    # checks if link is valid
    is_valid = check_video_url(video_playlist)
    
    if is_valid:
        # directory in which the user wants to save the files 
        directory = input('name of directory to download files: ')
        SAVE_PATH = os.path.join(os.getcwd(), directory.casefold().strip()) 

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': SAVE_PATH + '/%(title)s.%(ext)s'
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_playlist])

if __name__ == "__main__":
    download()
