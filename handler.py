import os
from typing import ContextManager

def generate_header(c, name, flag=False, url=""):
    if flag:
        s = "#"*c + " [" + name +"]" + "(" + url + ")"
    else:
        s = "#"*c + " " + name
    return s + "\n"

posts = "./posts"
index_file = "index.md"
contents = "contents.md"

file_type_list = ["md", "html"]

f_index = open(index_file, "w")
s = generate_header(1, "Category")
f_index.write(s)

i = 0
for root, dirs, files in os.walk(posts):
    # print(root)
    i += 1
    # 跳过posts目录
    if i == 1: continue
    c = root.count("\\")
    # print(c)
    header_name = os.path.split(root)[-1]
    # 如果存在文件，则目录添加链接
    flag = False
    for file in files:
        file_split = file.split(".")
        file_name = file_split[0]
        file_type = file_split[1]
        if file_type in file_type_list:
            flag = True
            break
    if flag:
        # 添加相对链接
        contents_url = root + "/" + contents
        s =  generate_header(c, header_name.title(), flag = True, url = contents_url)
        print(s)
        f_index.write(s)
        f_contents = open(contents_url, "w")
        s = generate_header(1, "Contents")
        f_contents.write(s)
        for file in files:
            if file == contents: continue
            file_split = file.split(".")
            file_name = file_split[0]
            file_type = file_split[1]
            if file_type in file_type_list:
                s = generate_header(2, file_name, flag=True, url="./"+file)
                f_contents.write(s)
        f_contents.close()
    else:
        s =  generate_header(c, header_name.title(), flag = False)
        f_index.write(s)
f_index.close()
print("Successful!")



