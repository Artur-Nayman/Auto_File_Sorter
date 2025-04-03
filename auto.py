import os
import shutil
import sys
import logging
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, DirModifiedEvent, FileModifiedEvent

source_dir = "/Users/artur/Downloads"
dest_dir_sfx = "/Users/artur/Pictures/sound"
dest_dir_music = "/Users/artur/Pictures/music"
dest_dir_video = "/Users/artur/Pictures/video"
dest_dir_pictures = "/Users/artur/Pictures/pictures"

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
                if name.endswith(".wav") or name.endswith(".mp3"):
                    dest = dest_dir_sfx
                    move(dest, entry, name)
                elif name.endswith(".mov") or name.endswith(".mp4"):
                    dest = dest_dir_video
                    move(dest, entry, name)
                elif name.endswith(".jpg") or name.endswith(".png") or name.endswith(".jpeg"):
                    dest = dest_dir_pictures
                    move(dest, entry, name)
                else:
                    dest = dest_dir_music
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