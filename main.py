from pytube import YouTube
import pytube
import os


def main(mp4=None, mp3=None):
    video_url = input('Enter YouTube video URL: ')

    if os.name == 'nt':
        path = os.getcwd() + '\\'
    else:
        path = os.getcwd() + '/'

    name = pytube.extract.video_id(video_url)
    YouTube(video_url).streams.filter(only_audio=True).first().download(filename=name + '.mp4')
    location = path + name + '.mp4'
    renametomp3 = path + name + '.mp3'
    os.rename(location, renametomp3)


if __name__ == '__main__':
    main()