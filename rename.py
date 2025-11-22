import os
import re

# 当前目录
folder = "."

# 匹配允许保留的字符：英文、数字、下划线、点、括号（去掉空格）
pattern = re.compile(r"[A-Za-z0-9_.()]+")  

for filename in os.listdir(folder):
    if filename.lower().endswith(".mp3"):
        name, ext = os.path.splitext(filename)
        # 使用正则保留英文、数字、下划线、点、括号
        new_name = "".join(pattern.findall(name))
        if not new_name:
            new_name = "file"
        new_filename = f"{new_name}{ext}"
        if new_filename != filename:
            print(f"Renaming: {filename} → {new_filename}")
            os.rename(os.path.join(folder, filename), os.path.join(folder, new_filename))
