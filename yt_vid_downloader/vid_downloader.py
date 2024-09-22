import time
import pytubefix
from shutil import rmtree
from os import scandir, makedirs, remove
from os.path import join, exists
from moviepy.editor import *
from datetime import datetime

def dl_vid(link, **mp3):
  """Gets the video and audio from youtube and downloads it. Returns the video title, audio path, and video path in a set in order."""
  yt = pytubefix.YouTube(link)
  path  = "C://Users//Jj//Documents//python_projects//yt_vid_downloader"
  
  for key, value in mp3.items():
    if value is True:
      paths = "C://Users//Jj//Documents//python_projects//yt_vid_downloader//music"
      aud_path = make_dirs(path, mp3=True)
      audio = yt.streams.filter(only_audio=True).first()
      audio.download(aud_path)


      return (paths, aud_path)
      
    elif value is False:
      # getting the video and audio file from youtube
      paths = make_dirs(path, mp3=False)
      vid = yt.streams.filter(adaptive=True).filter(mime_type='video/webm').first()
      audio = yt.streams.filter(only_audio=True).first()

      # downloading the audio and video file 
      audio.download(paths[1])
      vid.download(paths[0])
      
      return (vid.title, paths[0], paths[1])

def make_dirs(path, **mp3):
  """Making audio and video folder to store the audio and video to be merged.
  Returns video path and audio path in a set in order"""

  for key, value in mp3.items():
    if value is True:
      aud_path = join(path, "tem_audio")

      if not exists(aud_path):
        makedirs(aud_path)

      return aud_path
    
    elif value is False:
      aud_path = join(path, "tem_audio")
      vid_path = join(path, "tem_video")

      if not exists(aud_path):
        makedirs(aud_path)
      if not exists(vid_path):
        makedirs(vid_path)

      return(vid_path, aud_path)


def merge(vid_dir_path ,filename, vidpath, audpath):
  """Merges the audio with the sound"""

  with scandir(audpath) as aud_dir:
    for audio in aud_dir:
      audio_name = audio.name 
      audio = AudioFileClip(join(audpath, audio_name))
  with scandir(vidpath) as vid_dir:
    for video in vid_dir:
      video = VideoFileClip(video.path)
  
  merged_vid = video.set_audio(audio)
  merged_vid.write_videofile(join(vid_dir_path, f'{filename}.mp4'), temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac", threads=4)

  video.close()
  audio.close()

def convert_to_mp3(path, aud_path):
  with scandir(aud_path) as music_dir:
    for music in music_dir:
      musicname = music.name.split(".")
      musicname.pop()
      file_name = " ".join(musicname)
      file_to_convert = AudioFileClip(music.path)
      file_to_convert.write_audiofile(join(path, f"{file_name}.mp3"))
      file_to_convert.close()

def delete_aud_vid(audpath, vidpath=None, **mp3):
  """Removes temprary folders for video and audio"""

  for key, value in mp3.items():
    if value is True:
      rmtree(audpath)
          
    elif value is False:      
      rmtree(audpath)
      rmtree(vidpath)

      
def main():
  vid_path = "C://Users//Jj//Documents//python_projects//yt_vid_downloader//video_folder"

  choice = input("Do you want to download a video or a music (M for music/V for video)? ").casefold()

  match choice:
    case "m":
      link = input("Insert the link of the video you want to download: ")
      path = dl_vid(link, mp3=True)
      convert_to_mp3(path[0], path[1])
      delete_aud_vid(path[1], mp3=True)

    case "v":
      link = input("Insert the link of the video you want to download: ")
      file_info = dl_vid(link, mp3=False)
      time.sleep(3)
      merge(vid_path ,file_info[0], file_info[1], file_info[2])
      time.sleep(1)
      delete_aud_vid(file_info[1], file_info[2], mp3=False)

    case _:
      print("Invalid choice")


if __name__=="__main__":
  main()





