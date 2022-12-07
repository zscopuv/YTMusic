from colorama import Fore, Style, init; init();
from pytube import YouTube

def create(LINK):    
    print("\n" + 
          Style.BRIGHT + 
          Fore.BLUE + "Downloading the file " + 
          Fore.LIGHTYELLOW_EX + YouTube(LINK).title)
    try:
        YouTube(LINK).streams.first().download(output_path="cache/", filename=YouTube(LINK).title + ".mp3")
    except:
        print(Style.BRIGHT + Fore.RED + "An error has occurred." + Style.RESET_ALL)

def getName(LINK):
    try:
        return YouTube(LINK).title + ".mp3"
    except: 
        print(Style.BRIGHT + Fore.RED + "An error has occurred." + Style.RESET_ALL)
