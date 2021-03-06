from pyutils.cli.flags import verify_flag
from pyutils.cli.clitools import run_cmd

import os
import fnmatch
from os.path import join

import sys


def search_projects():
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

    shader_flag = verify_flag("--shader")
    csharp_flag = verify_flag("--csharp")
    no_flag = not csharp_flag and not shader_flag

    show_cs_files = csharp_flag or no_flag
    show_shader_files = shader_flag or no_flag

    for u in u_paths:
        project_path = u
        project_name = os.path.basename(project_path)
        print('Project ' + project_name)
        print('  Path ' + project_path)

        project_path = os.path.join(project_path, "Assets/")

        if show_cs_files:
            cs_number_cmd = 'find "' + project_path + '" -name "*.cs" | wc -l'
            cs_number_output = run_cmd(cs_number_cmd)

            cs_lines_cmd = '(find "' + project_path + '" -name "*.cs" | xargs -I {} cat {}) | wc -l'
            cs_lines_output = run_cmd(cs_lines_cmd)

            print('  Total CS scripts: ' + cs_number_output.strip() + ' (LOC: ' + \
                cs_lines_output.strip() + ')')

        if show_shader_files:
            shader_number_cmd = 'find "' + project_path + '" -name "*.shader" | wc -l'
            shader_number_output = run_cmd(shader_number_cmd)

            shader_lines_cmd = '(find "' + project_path + '" -name "*.shader" | xargs -I {} cat {}) | wc -l'
            shader_lines_output = run_cmd(shader_lines_cmd)

            print('  Total shader scripts: ' + shader_number_output.strip() + ' (LOC: ' + \
                shader_lines_output.strip() + ')')

            if shader_flag:
                shader_files_cmd = 'find "' + project_path + '" -name "*.shader"'
                shader_files_output = run_cmd(shader_files_cmd)

                shader_files = shader_files_output.split("\n")

                for shader_file in shader_files:
                    shader_name = os.path.basename(shader_file)
                    print("  - %s" % shader_name)


if __name__ == '__main__':
    search_projects()
