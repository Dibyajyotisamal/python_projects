import os
import shutil


def create_folder_if_not_present(name):
    if not os.path.exists(name):
        os.makedirs(name)


extensions = {
    "Images": {'.ai', '.bmp', '.gif', '.ico', '.jpeg',
               '.jpg', '.png', '.ps', '.psd', '.svg', '.tif', '.tiff'},
    "Audio": {'.aif', '.cda', '.mid', '.midi',
              '.mpa', '.ogg', '.wav', '.wma', '.wpl', '.mp3'},
    "Compressed": {'.7z', 'arj', '.deb', '.pkg',
                   '.rar', '.rpm', '.tar.gz', '.z', '.zip'},
    "Videos": {'.3g2', '.3gp', '.avi', '.flv', '.h264', '.m4v', '.mkv',
               '.mov', '.mp4', '.mov', '.mp4', '.mpeg', '.rm', '.swf', '.wmv'},
    "Docs": {'.doc', '.docx', '.pptm', '.ppt', '.pdf', '.txt'},
    "Others": {None}
}


# make folders to categorize into
for i in extensions.keys():
    create_folder_if_not_present(i)


# classify the files and categorize them
with os.scandir() as entries:
    for entry in entries:
        file_ext = f".{entry.name.split('.')[-1]}"
        for folder, extension in extensions.items():
            if entry.is_file() and file_ext in extension:
                shutil.move(entry.path, folder)
                break
            elif entry.is_file() and folder == "Others":
                shutil.move(entry.path, folder)
