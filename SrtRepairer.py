import glob
import os
import re
import shutil
import time


# main class
class SrtRepairer:
    def __init__(self, source_pathname, target_folder_name):
        self.path_name = ''
        self.source_pathname = source_pathname
        self.target_folder_name = target_folder_name

    def move_files(self):
        # counting start
        print("Moving srt files to target folder...")
        start = time.perf_counter()

        # main function
        file_pathes = glob.glob(self.source_pathname, recursive=True)
        for path in file_pathes:
            parent_name = os.path.basename(os.path.dirname(path))
            target_folder_path = os.path.join(
                os.getcwd(), self.target_folder_name, parent_name)

            os.makedirs(target_folder_path, exist_ok=True)

            shutil.copy(path, target_folder_path)

        self.path_name = os.getcwd()+'\\'+self.target_folder_name+'\**\*.srt'

        # counting end
        end = time.perf_counter()
        print(f"Done in {end-start:.2f} second(s).\n")

    def repair_files(self):
        # counting start
        print("Repairing str files...")
        start = time.perf_counter()

        # main function
        file_pathes = glob.glob(self.path_name, recursive=True)
        for path in file_pathes:
            with open(path, 'r', encoding='utf-8') as f:
                data = f.read()

                pattern_1 = r'^0\n'
                data = re.sub(pattern_1, '', data)

                pattern_2 = r'\d+\n\n'
                data = re.sub(pattern_2, r'\n', data)

            with open(path, 'w', encoding='utf-8') as f:
                f.writelines(data)

        # counting end
        end = time.perf_counter()
        print(f"Done in {end-start:.2f} second(s).\n")
