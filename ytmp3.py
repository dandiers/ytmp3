import os
import pytz
from pystyle import *
from pytube import YouTube
from datetime import datetime
from tqdm import tqdm

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')    
    title = f"""
         
         
         
         
         
         
                 
         
        
               {datetime.now(pytz.timezone('Asia/Jakarta')).strftime("%A, %d %B %Y %H:%M WIB")}  
    
▓██   ██▓▄▄▄█████▓ ███▄ ▄███▓ ██▓███     ▄▄▄█████▓ ██░ ██  ██▀███  ▓█████ ▓█████ 
 ▒██  ██▒▓  ██▒ ▓▒▓██▒▀█▀ ██▒▓██░  ██▒   ▓  ██▒ ▓▒▓██░ ██▒▓██ ▒ ██▒▓█   ▀ ▓█   ▀ 
  ▒██ ██░▒ ▓██░ ▒░▓██    ▓██░▓██░ ██▓▒   ▒ ▓██░ ▒░▒██▀▀██░▓██ ░▄█ ▒▒███   ▒███   
  ░ ▐██▓░░ ▓██▓ ░ ▒██    ▒██ ▒██▄█▓▒ ▒   ░ ▓██▓ ░ ░▓█ ░██ ▒██▀▀█▄  ▒▓█  ▄ ▒▓█  ▄ 
  ░ ██▒▓░  ▒██▒ ░ ▒██▒   ░██▒▒██▒ ░  ░     ▒██▒ ░ ░▓█▒░██▓░██▓ ▒██▒░▒████▒░▒████▒
   ██▒▒▒   ▒ ░░   ░ ▒░   ░  ░▒▓▒░ ░  ░     ▒ ░░    ▒ ░░▒░▒░ ▒▓ ░▒▓░░░ ▒░ ░░░ ▒░ ░
 ▓██ ░▒░     ░    ░  ░      ░░▒ ░            ░     ▒ ░▒░ ░  ░▒ ░ ▒░ ░ ░  ░ ░ ░  ░
 ▒ ▒ ░░    ░      ░      ░   ░░            ░       ░  ░░ ░  ░░   ░    ░      ░   
 ░ ░                     ░                         ░  ░  ░   ░        ░  ░   ░  ░
 ░ ░                                             
                                  
 Note !   
 Script ini di buat untuk mendownload youtube video mp3.
 Jika ingin mengubah script sebaiknya izin dandier.
   """
    print(Colorate.Vertical(Colors.DynamicMIX((Col.red, Col.purple)), Center.XCenter(title if os.name == "nt" else title)))

if __name__ == '__main__':
    banner()
    video_url = input(f"{Col.pink}video url:{Col.white} ")
    if video_url.startswith(("http://", "https://")):
        yt = YouTube(video_url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        print(Colorate.Vertical(Colors.DynamicMIX((Col.green, Col.green)), Center.XCenter(f"\nTitle: {audio_stream.title}.mp3")))
        audio_stream.download(filename='tmp_file.mp3', skip_existing=True)
        os.rename('tmp_file.mp3', f"{audio_stream.title}.mp3")
        print(Colorate.Vertical(Colors.DynamicMIX((Col.green, Col.green)), Center.XCenter(f"\nSuccessfully Downloaded {audio_stream.title}.mp3")))
    else:
        print(Colorate.Vertical(Colors.DynamicMIX((Col.red, Col.red)), Center.XCenter("Video URL must start with https")))
            
