
import os

data_dir = 'files/'

filelist = os.listdir(data_dir)  # 该文件夹下所有的文件（包括文件夹）
print(filelist) #文件夹中所有文件名

for file in filelist:
    if ('.flac' in file or '.ape' in file or '.mp3' in file or '.wav' in file):
        oldname = file
        spl_type = oldname.split('.', 1)
        spl_name = spl_type[0].split(' - ')
        newname = spl_name[1] + ' - ' + spl_name[0] + '.' +spl_type[1]
        print(newname)
        os.rename(os.path.join(data_dir,oldname), os.path.join(data_dir,newname))  # 重命名