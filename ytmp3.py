import os
import pytz
import datetime
from pystyle import *
from pytube import YouTube
from datetime import datetime, timedelta

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
    video_url = input(f"{Col.pink}      video url:{Col.white} ")
    if video_url.startswith(("http://", "https://")):
        yt = YouTube(video_url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_stream.download()
        os.rename(f"{audio_stream.title}.{audio_stream.subtype}", f"{audio_stream.title}.mp3")
        print(Colorate.Vertical(Colors.DynamicMIX((Col.green, Col.green)), Center.XCenter(f"\nBerhasil Download {audio_stream.title}.mp3")))
    else:
        print(Colorate.Vertical(Colors.DynamicMIX((Col.red, Col.red)), Center.XCenter("Video Url Harus Berawalan https")))