from pytube import YouTube

link = input("Add youtube video link here: ")
yt = YouTube(link)
title = yt.title
print(title)
confirm = input("Is this your video?(y/n): ")

if confirm == "y":
    print('''
Select format: 
for MP4
1080P type 1, 720P type 2, 360P type 3
For audio
160KBPS type 4, 70 KBPS type 5''')
    user_format = input(": ")
    if user_format == "1":
        user_format = 137
    elif user_format == "2":
        user_format = 22
    elif user_format == "3":
        user_format = 18
    elif user_format == "4":
        user_format = 251
    elif user_format == "5":
        user_format = 250
    else:
        print("Enter a Valid option")

print(f"{title} is downloading")
# print(yt.thumbnail_url)
convert = yt.streams.get_by_itag(user_format)
convert.download()

