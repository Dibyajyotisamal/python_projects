#Sometimes while copying files, a group of files might lose their extension names.I have faced the problem multiple times in the past. Now that i have learnt python, i made a solution for the issue.

import os

with os.scandir() as entries:
    for entry in entries:
        if entry.name=='extensionSetter.py':continue
        os.rename(entry.name,f"{entry.name}.mp4")