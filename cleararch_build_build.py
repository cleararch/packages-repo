import os
import subprocess


if os.system("git version")!=0:
    print("需要 git。")
    os.exit(2)
if os.system("pacman -h")!=0:
    print("需要 pacman。")
    os.exit(2)
build_list=["linux-tikogasa","filesystem"]
for i in build_list:
    if os.system("git checkout "+i) !=0:
        print("git 仓库不完整。")
        os.exit(2)
    if os.system("makepkg -i") !=0:
        print(i+" 包构建失败")
        os.exit(1)
    
print("软件包构建成功，生成")
