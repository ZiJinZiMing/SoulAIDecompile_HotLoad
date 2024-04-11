import os
import subprocess
import shutil


def decompile_lua(folder_path, lua_decompiler_path, OnlyLuaFile):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.lua'):
                # 打印.lua文件的路径
                lua_file_path = os.path.join(root, file)
                print(lua_file_path)
                new_lua_file_path = lua_file_path + '_new'
                # 调用DSLuaDecompiler.exe文件，传入.lua文件作为参数
                subprocess.run([lua_decompiler_path, lua_file_path, '-o', new_lua_file_path], check=True)
                # 反编译的lua文件替换原有luac文件
                os.remove(lua_file_path)
                os.rename(new_lua_file_path, lua_file_path)
                folder_path_lua = os.path.join(folder_path, file)

                # 仅保留lua的情况下删掉其他文件，并且放lua到folder_path
                if OnlyLuaFile:
                    os.rename(lua_file_path, folder_path_lua)
    if OnlyLuaFile:
        # 删除其余文件夹和文件 
        os.remove(os.path.join(folder_path, '_yabber-bnd4.xml'))
        GR_dir = os.path.join(folder_path, 'GR')
        script_dir = os.path.join(folder_path, 'script')
        if os.path.isdir(GR_dir):
            shutil.rmtree(GR_dir)
        if os.path.isdir(script_dir):
            shutil.rmtree(script_dir)

def process_dcx(yabber_path, script_dir, lua_decompiler_path, OnlyLuaFile):
    for item in os.listdir(script_dir):
        if item.endswith('.luabnd.dcx'):
            # 获取文件名（不包括扩展名）
            file_name = item[:-len('.luabnd.dcx')]
            # 构建新的文件夹名称
            new_folder_name = f"{file_name}-luabnd-dcx"
            # 构建完整的文件路径
            file_path = os.path.join(script_dir, item)
            # 调用Yabber.exe文件，传入.luabnd.dcx文件作为参数
            subprocess.run([yabber_path, file_path], check=True)

            # 构建生成的文件夹完整路径
            new_folder_path = os.path.join(script_dir, new_folder_name)
            # 递归遍历生成的文件夹，打印所有.lua文件
            if os.path.isdir(new_folder_path):
                decompile_lua(new_folder_path, lua_decompiler_path, OnlyLuaFile)


# 这里需要填写对绝对路径
Yabber_exe = "C:/DevTools/SoulAIDecompile_HotLoad/Yabber/Yabber.exe"
DSLuaDecompiler_exe = "C:/DevTools/SoulAIDecompile_HotLoad/DSLuaDecompiler/DSLuaDecompiler.exe"
Script_Dir = "C:/DevTools/SoulAIDecompile_HotLoad/script"
# 是否仅保留lua文件，不保留文件结构
OnlyLuaFile = True
process_dcx(Yabber_exe, Script_Dir, DSLuaDecompiler_exe, OnlyLuaFile)
