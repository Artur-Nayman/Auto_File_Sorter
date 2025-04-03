import os
import shutil
import sys
import logging
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, DirModifiedEvent, FileModifiedEvent

source_dir = "/Users/artur/Downloads"
dest_dir_sfx = "/Users/artur/Pictures/sound"
dest_dir_other = "/Users/artur/Pictures/other"
dest_dir_video = "/Users/artur/Pictures/video"
dest_dir_pictures = "/Users/artur/Pictures/pictures"
dest_dir_dir = "/Users/artur/Pictures/dir"
dest_dir_program = "/Users/artur/Pictures/program"
dest_dir_document = "/Users/artur/Pictures/document"

image_extensions = [".jpg", ".png", ".jpeg", ".gif", ".jpe", ".webp"]
video_extensions = [".mov", ".mp4", ".mpg", ".mp4v", ".m4v", ".mpv"]
audio_extensions = [".mp3", ".aac", ".m4a", ".wav", ".flac", ".wma"]
document_extensions = [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx"]
program_extensions = [".exe", ".bat", ".cmd", ".com", ".msi", ".app", ".dmg", ".sh", ".elf", ".jar", ".py"]
dir_extensions = [".dir", ".zip", ".7z", ".rar", ".tar", ".tar.gz"]



with os.scandir(source_dir) as entries:
    for entry in entries:
        print(entry.name)

def makeUnique(path):
    root, ext = os.path.splitext(path)
    counter = 1
    while os.path.exists(path):
        path = f"{root} ({counter}){ext}"
        counter += 1
    return path


def move(dest, entry, name):
    file_exists = os.path.exists(dest + "/" + name)
    if file_exists:
        unique_name = makeUnique(name)
        os.rename(entry, unique_name)
    shutil.move(entry, dest)

class MoverHandler(FileSystemEventHandler):
    def on_modified(self, event):
        with os.scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                dest = source_dir
                if name.endswith(tuple(image_extensions)):
                    dest = dest_dir_pictures
                    move(dest, entry, name)
                elif name.endswith(tuple(video_extensions)):
                    dest = dest_dir_video
                    move(dest, entry, name)
                elif name.endswith(tuple(audio_extensions)):
                    dest = dest_dir_sfx
                    move(dest, entry, name)
                elif name.endswith(tuple(program_extensions)):
                    dest = dest_dir_program
                    move(dest, entry, name)
                elif name.endswith(tuple(document_extensions)):
                    dest = dest_dir_document
                    move(dest, entry, name)
                elif name.endswith(tuple(dir_extensions)):
                    dest = dest_dir_dir
                    move(dest, entry, name)
                else:
                    dest = dest_dir_other
                    move(dest, entry, name)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()