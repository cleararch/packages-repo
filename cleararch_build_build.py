import os,shutil
import subprocess


# 检查依赖
if os.system("git version")!=0:
    print("需要 git。")
    os.exit(2)
if os.system("pacman -h")!=0:
    print("需要 pacman。")
    os.exit(2)
if os.system("repo-add")!=0:
    print("需要 repo-add")
    os.exit(2)

# 编译程式档
build_list=["linux-tikogasa","filesystem"]
packages_name=[]
os.mkdir("/tmp/build_repo")
for i in build_list:
    if os.system("git checkout "+i) !=0:
        print("git 仓库不完整。")
        os.exit(2)
    if os.system("makepkg -i") !=0:
        print(i+" 包构建失败")
        os.exit(1)
    for k in os.listdir("./"):
        if k.find(".pkg.tar")!=-1:
           packages_name.append(k)
           shutil.copyfile(k,"/tmp/build_repo/"+k)
           continue
    print(i+" 包构建失败")
    os.exit(1)


# 生成仓库档案
print("软件包构建成功，生成仓库档案。")
repo_files=" ".join(packages_names)
if os.system("repo add "+repo_files)!=0:
    print("无法构建仓库档案。")
    os.exit(1)
os.exit(0)
