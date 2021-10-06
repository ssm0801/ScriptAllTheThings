from pytube import YouTube, Playlist
import time

class Video(YouTube):
    def __init__(self, url):
        self.url = YouTube(url)
        
    def download(self, type : str = 'high_resolution'):
        self.url.streams.get_highest_resolution().download()
        if type == 'low_resolution':
            self.url.streams.get_lowest_resolution().download()
    


class Play(Playlist):
    def __init__(self, url : str):
        self.url = Playlist(url)
        
    def download(self, type : str = 'high_resolution'):
        
        count = 0
        for i in self.url.videos:

            print("Wait...")
            
            if type == 'low_resolution':
                i.streams.get_lowest_resolution().download()
            else:
                i.streams.get_highest_resolution().download()

            count = count + 1
            
            time.sleep(2)
            print("Check your current directory...")
            time.sleep(2)
            
            print(count ," Video Downloaded Successfully!")

# Play('https://www.youtube.com/playlist?list=PLCnqvb4OGG10qseF62egHuv5FNmhJxASQ').download()