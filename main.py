import os
import shutil
parent_dir="Your_Directory"
entries = os.listdir(parent_dir)
for entry in entries:
     print(entry) #Gives name o files in given directory
new_list=[]
for entry in entries:
    new_list.append(entry.split(".")[-1])
print(set(new_list)) #Gives the extentions of the files present

for extension in set(new_list):
    path=os.path.join(parent_dir, extension)
    if not os.path.isdir(extension):
            os.makedirs(path ,exist_ok=True) #Creates the folder by the name of extension
for entry in entries:
    ext = entry.split(".")[-1]
    shutil.move(parent_dir +"\\" + entry, parent_dir +"\\"+ ext +"\\"+ entry)  #move files as per their extension

