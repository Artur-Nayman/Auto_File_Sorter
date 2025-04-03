# File Organizer

## Overview
This script automatically organizes files from a specified source directory into categorized destination folders based on file extensions. It uses the `watchdog` library to monitor changes in the source directory and moves files accordingly.

## Features
- Monitors the `Downloads` directory for new or modified files.
- Automatically moves files to designated folders based on their type:
  - **Images** (`.jpg`, `.png`, `.jpeg`, `.gif`, `.jpe`, `.webp`) → `Pictures/pictures`
  - **Videos** (`.mov`, `.mp4`, `.mpg`, `.mp4v`, `.m4v`, `.mpv`) → `Pictures/video`
  - **Audio** (`.mp3`, `.aac`, `.m4a`, `.wav`, `.flac`, `.wma`) → `Pictures/sound`
  - **Documents** (`.pdf`, `.doc`, `.docx`, `.xls`, `.xlsx`, `.ppt`, `.pptx`) → `Pictures/document`
  - **Programs** (`.exe`, `.bat`, `.cmd`, `.com`, `.msi`, `.app`, `.dmg`, `.sh`, `.elf`, `.jar`, `.py`) → `Pictures/program`
  - **Compressed Files & Archives** (`.dir`, `.zip`, `.7z`, `.rar`, `.tar`, `.tar.gz`) → `Pictures/dir`
  - **Others** → `Pictures/other`
- Ensures files are not overwritten by renaming duplicates uniquely.

## Requirements
- Python 3.x
- Required libraries:
  ```sh
  pip install watchdog
  ```

## Usage
1. Update the `source_dir` and destination directories in the script as needed.
2. Run the script:
   ```sh
   python file_organizer.py
   ```
3. The script will run continuously, monitoring the source directory and automatically organizing new files.
4. Stop the script using `Ctrl + C`.

## Customization
- Modify the `source_dir` and destination directory paths to fit your system.
- Add or remove file extensions in the respective lists to customize categorization.

## Troubleshooting
- If the script does not start, ensure `watchdog` is installed using `pip install watchdog`.
- If files are not moving correctly, check if the destination directories exist or create them manually.
- Run the script in a terminal with logging enabled to identify issues.

## License
This script is open-source and free to use and modify.

