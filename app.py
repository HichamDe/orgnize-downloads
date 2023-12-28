
#* Python Downloads Management 
#! Run in a testing environment

#? This app will control the downloads of your computer by transfaring files with 
#? specific extantions to the folders selected

#? you can execute this app any where , as long as you use full paths in 
#? the folders location 

#? os module and system
import os,shutil

#? the location of the folders in the system
#* EX: C:\USER\FOLDER_PATH
#* PUT THE LINKS BEFORE TESTING
downloads_folder = r"" # Main Downloads Folder
img_folder = r"" # Images
music_folder = r"" # Music 
video_folder = r"" # Videos
document_folder = r"" # Documents


#? How the programme works : 
#* gets all the files in the downloads folder
#* sort them by extantion
#* send files by a loop into the right folders

#? Catigories
imgs = [] # Images
docs = [] # Documents
vds = [] # Videos
msc = [] # Music

#TODO - Get all files from the main folder :
listDir = os.listdir(downloads_folder) 

#TODO - Sort by Extantion :
#* Looking for imgs : (svg+png+jpeg) 
for Dfile in listDir:
    if ".png" in Dfile or ".jpeg" in Dfile or ".png" in Dfile or ".jpg" in Dfile:
        imgs.append(Dfile)
    elif ".txt" in Dfile or ".docx" in Dfile or ".pdf" in Dfile:
        docs.append(Dfile)
    elif ".mp3" in Dfile:
        msc.append(Dfile)
    elif ".mp4" in Dfile:
        vds.append(Dfile)

#TODO - Move Files 
#* move images
for img in imgs:
    shutil.move(downloads_folder+"\\"+img , img_folder+"\\"+img)
#* move documents
for doc in docs:
    shutil.move(downloads_folder+"\\"+doc , document_folder+"\\"+doc)
#* move videos
for vd in vds:
    shutil.move(downloads_folder+"\\"+vd , video_folder+"\\"+vd)
#* move Music
for music in msc:
    shutil.move(downloads_folder+"\\"+music , music_folder+"\\"+music)