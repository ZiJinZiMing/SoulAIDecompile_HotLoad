import os
import subprocess
import shutil

def clear_directory(directory):
    """ 清空指定的文件夹 """
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")

# 示例名称数组
#
# names = ["aicommon","m10_00_00_00", "m11_00_00_00", "m11_01_00_00", "m11_02_00_00", "m12_00_00_00", "m13_00_00_00", "m15_00_00_00", "m17_00_00_00", "m20_00_00_00", "m25_00_00_00", "m25_01_00_00"]  # 这里应替换为您的名称数组
# names = ["m11_00_00_00"]  # 这里应替换为您的名称数组
# names = ["m11_02_00_00"]  # 这里应替换为您的名称数组
names = ["m11_01_00_00"]  # 永真、弦一郎
# names = ["m11_02_00_00"]  # 剑圣一心
# names = ["m17_00_00_00"]  # 狮子猿
current_directory = os.getcwd()
Yabber_exe = "./Yabber/Yabber.exe"  # 替换为外部程序的路径
destination_directory = "C:/Program Files (x86)/Steam/steamapps/common/Sekiro/mods/script"  # 替换为目标文件夹的路径

# 清空目标文件夹
clear_directory(destination_directory)

for name in names:
    source_dir_path = os.path.join(current_directory, name + "-luabnd-dcx")
    
    # 执行外部程序
    subprocess.run([Yabber_exe, source_dir_path])

    # 生成的文件路径
    generated_file = os.path.join(current_directory, f"{name}.luabnd.dcx")

    # 检查文件是否存在并移动
    if os.path.exists(generated_file):
        shutil.move(generated_file, destination_directory)
        print(f"Moved '{generated_file}' to '{destination_directory}'")
    else:
        print(f"File '{generated_file}' not found after execution.")
