import os
import fnmatch
from os.path import join

import sys

search_path = sys.argv[1]

assets_file_path = []
psettings_file_path = []

for root, subFolders, files in os.walk(search_path):
    for folder in subFolders:
        if folder == 'Assets':
            assets_file_path.append(root)
        if folder == "ProjectSettings":
            psettings_file_path.append(root)

u_paths = []

for f in assets_file_path:
    for f2 in psettings_file_path:
        if f == f2:
            u_paths.append(f)
            break

for u in u_paths:
    print(u)