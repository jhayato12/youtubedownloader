from pytube import YouTube
import os


def mainmp3download():
    link = input("Insert the URL of the video you want to download [quit or Enter to quit]: ")
    downloads_folder = os.path.expanduser("~/Downloads")

    if link.startswith("https://www.youtube.com/"):
        youtube = YouTube(link)
        try:
            youtube = youtube.streams.filter(only_audio=True).first().download(downloads_folder)
            name, ext = os.path.splitext(youtube)
            mp3_file = name + ".mp3"
            os.rename(youtube, mp3_file)
            print("Done")
            mainmp3download()

        except:
            print("There has been an error while downloading your youtube video")
            menu()

    elif link == "quit" or " ":
        menu()

    else:
        print("Not a youtube link")


def mainmp4download():
    link = input("Insert the URL of the video you want to download [quit or Enter to quit]: ")
    downloads_folder = os.path.expanduser("~/Downloads")

    if link.startswith("https://www.youtube.com/"):
        youtube = YouTube(link)
        try:
            youtube = youtube.streams.filter().get_highest_resolution().download(downloads_folder)
            print("Done")
            mainmp4download()

        except:
            print("There has been an error while downloading your youtube video")
            menu()

    elif link == "quit" or " ":
        menu()

    else:
        print("Not a youtube link")


def menu():
    print("[1] youtube to mp3")
    print("[2] youtube to mp4")
    print("[0] Exit the program")


menu()


def userinput():
    try:
        choice = int(input("Enter your option: "))
        while choice != 0:
            if choice == 1:
                mainmp3download()
            elif choice == 2:
                mainmp4download()
            else:
                print("Invalid option")
            choice = int(input("Enter your option: "))
    except:
        print("There has been an issue with your input")
        menu()
        userinput()


userinput()