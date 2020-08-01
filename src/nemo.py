import os
import fnmatch
from os.path import join

import sys

import subprocess

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

print('Found %s Unity projects\n' % (len(u_paths)))

for u in u_paths:
    project_path = u
    project_name = os.path.basename(project_path)
    print('Project ' + project_name)
    print('  Path ' + project_path)

    project_path = os.path.join(project_path, "Assets/")

    cs_number_cmd = 'find "' + project_path + '" -name "*.cs" | wc -l'
    cs_number_output = subprocess.check_output(cs_number_cmd, shell=True)
    cs_number_output = cs_number_output.decode("utf8")

    cs_lines_cmd = '(find "' + project_path + '" -name "*.cs" | xargs -I {} cat {}) | wc -l'
    cs_lines_output = subprocess.check_output(cs_lines_cmd, shell=True)
    cs_lines_output = cs_lines_output.decode("utf8")

    print('  Total CS scripts: ' + cs_number_output.strip() + ' ( LOC: ' + \
        cs_lines_output.strip() + ')')

    shader_number_cmd = 'find "' + project_path + '" -name "*.shader" | wc -l'
    shader_number_output = subprocess.check_output(shader_number_cmd, shell=True)
    shader_number_output = shader_number_output.decode("utf8")

    shader_lines_cmd = '(find "' + project_path + '" -name "*.shader" | xargs -I {} cat {}) | wc -l'
    shader_lines_output = subprocess.check_output(shader_lines_cmd, shell=True)
    shader_lines_output = shader_lines_output.decode("utf8")

    print('  Total shader scripts: ' + shader_number_output.strip() + ' ( LOC: ' + \
        shader_lines_output.strip() + ')')