from shutil import move
from os import scandir, rename, makedirs
from os.path import exists, splitext, join
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

path = "C:\\Users\\Jj\\Documents\\school works"
doc_path = "C:\\Users\\Jj\\Documents\\school works\\Documents" 
doc_img = "C:\\Users\\Jj\\Documents\\school works\\Images"
doc_vid = "C:\\Users\\Jj\\Documents\\school works\\Videos"
doc_aud = "C:\\Users\\Jj\\Documents\\school works\\Audio"
sub_folder = ["UTS", "Calculus", "MMW", "CED", "STS", "Pco", "Chemistry", "Core Values", "PLD", "PATHFIT"]  
gen_folder = ["Documents", "Images", "Videos", "Audio"]
image = [".jpeg", ".png", ".jpg", ".gif"]
videos = [".mp4", ".avi"]
audio = [".mp3", ".wav", ".msv"]
dir_file = {"docx": "Word",
            "xlsx": "Excel",
            "ppt": "Powerpoint",
            "pptx": "Powerpoint",
            "pdf": "PDF"}

def make_unique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    # * IF FILE EXISTS, ADDS NUMBER TO THE END OF THE FILENAME
    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1

    return name


def move_file(dest, entry, name):
    if exists(f"{dest}/{name}"):
        unique_name = make_unique(dest, name)
        oldName = join(dest, name)
        newName = join(dest, unique_name)
        rename(oldName, newName)
    move(entry, dest)
        
class Organize(FileSystemEventHandler):
  def on_modified(self, event):
    for folders in gen_folder:
      if not exists(path + "\\" + folders):
        makedirs(path + "\\" + folders)
    for subj in sub_folder:
      for folders in dir_file.values():
        if not exists(doc_path + "\\" + subj +  "\\" + folders):
          makedirs(doc_path + "\\" + subj +  "\\" + folders)

    with scandir(path) as files:
      for file in files:
        name = file.name
        self.check_docs(file, name)
        self.check_img(file, name)
        self.check_vid(file, name)
        self.check_audio(file, name)

  def check_docs(self, file, name):
    for subj in sub_folder:
      for ext, folder in dir_file.items():
          if name.endswith(ext) and (subj.casefold() in name.casefold()):
            move_file(f"{doc_path}\\{subj}\\{folder}", file, name)
            print("moved")

  def check_img(self, file, name):  
    for img in image:
        if name.endswith(img):
            move_file(doc_img, file, name)
            print("moved")

  def check_vid(self, file, name):
    for vid in videos:
        if name.endswith(vid):
          move_file(doc_vid, file, name)
          print("moved")

  def check_audio(self, file, name):
    for aud in audio:
        if name.endswith(aud):
          move_file(doc_aud, file, name)
          print("moved")

if __name__=="__main__":

  path = "C:\\Users\\Jj\\Documents\\school works"

  event_handler = Organize()
  observer = Observer()
  observer.schedule(event_handler, path, recursive=True)
  observer.start()


  try:
    print('Monitoring')
    while True:
      time.sleep(10)
  except KeyboardInterrupt:
    observer.stop
    print('Done')
  
  observer.join()