from .base import Video, Play
import time

def video_menu():
    from .menu import main
    vid_choice = str(input("""    
    ===================================
    YOUTUBE VIDEO DOWNLOAD
    Select Quality

    1. Highest
    2. Lowest
    3. Back

    Select Your Choice:"""))
    
    if vid_choice in ['1', 'Highest', 'highest']:

        link = str(input("Please Drop Link of Video here: "))

        print("Wait...")

        try:
            Video(link).download()
            time.sleep(2)
            print("Check your current directory...")
            time.sleep(2)
            print("Downloaded Successfully")

            time.sleep(3)
        except:
            print("Invalid Link of Youtube Video")
            time.sleep(2)
        
        video_menu()

    elif vid_choice in ['2', 'Lowest', 'lowest']:
        
        link = str(input("Please Drop Link of Video here: "))

        print("Wait...")
        
        try:
            Video(link).download('low_resolution')
            time.sleep(2)
            print("Check your current directory...")
            time.sleep(2)
            print("Downloaded Successfully")

            time.sleep(3)
        except:
            print("Invalid Link of Youtube Video")
            time.sleep(2)
        
        video_menu()


    elif vid_choice in ['3', 'Back', 'back']:
        main()

    else:
        video_menu()


def playlist_menu():

    vid_choice = str(input("""    
    ===================================
    YOUTUBE PLAYLIST DOWNLOAD
    Select Quality

    1. Highest
    2. Lowest
    3. Back

    Select Your Choice:"""))
    
    if vid_choice in ['1', 'Highest', 'highest']:
        link = str(input("Please Drop Link of Playlist here: "))

        try:
            Play(link).download()
        except:
            print("Invalid Link of Youtube Playlist")
            time.sleep(2)
        
        playlist_menu()

    elif vid_choice in ['2', 'Lowest', 'lowest']:
        link = str(input("Please Drop Link of Playlist here: "))

        try:
            Play(link).download('low_resolution')
        except:
            print("Invalid Link of Youtube Playlist")
            time.sleep(2)

        playlist_menu()

    elif vid_choice in ['3', 'Back', 'back']:
        main()

    else:
        playlist_menu()


def main():  

    opt = str(input(f"""
    ===================================
    YOUTUBE DOWNLOADER (By EitoZX)
    What Do You Want To Downlod?

    1. Video
    2. Playlist
    3. Exit

    Select Your Choice:
    """))

    print(opt)

    if opt == "1":
        video_menu()

    if opt == "2":
        playlist_menu()

    elif opt == "3":
        exit()
        
    else:
        main()


# playlist_menu()