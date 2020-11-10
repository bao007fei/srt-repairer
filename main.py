import time
from SrtRepairer import SrtRepairer


# 👇 Change code here 👇
source_pathname = r"X:\Xxxx\Xxxxx\**\*.srt"
target_folder_name = "srts"
# 👆 Change code here 👆


print("<--Welcome to srt file repairer-->\n")

foo = SrtRepairer(source_pathname, target_folder_name)
foo.move_files()
foo.repair_files()

print(f"All jobs finished in {time.perf_counter():.2f} second(s).")
