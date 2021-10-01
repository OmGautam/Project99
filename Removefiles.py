import shutil
import os
import time

def main():
    deletedFolderCount = 0
    deletedFileCount = 0
    
    path = "/path"
    days = 30
    seconds = time.time()-(days*24*60*60)
    if os.path.exists(path):
        for rootFolder,folder,files in os.walk(path):
            if seconds>=get_file_or_folder_age(rootFolder):
                removeFolder(rootFolder)
                deletedFolderCount+=1
                break
            else:
                for folder in folders:
                    folderPath = os.path.join(rootFolder,folder)
                    if seconds>=get_file_or_folder_age(folderPath):
                        removeFolder(folderPath)
                        deletedFolderCount+=1
                for files in files:
                    filePath=os.path.join(rootFolder,file)
                    if seconds>=get_file_or_folder_age(filePath):
                        removeFile(filePath)
                        deletedFileCount+=1
        else:
            if seconds>=get_file_or_folder_age(path):
                removeFile(path)
                deletedFileCount+=1
    else:
        print(f'"{path}"is not found')
        deletedFileCount+=1
    print(f"Total folders deleted:{deletedFolderCount}")
    print(f"Total files deleted:{deletedFileCount}")

def removeFile(path):
    if not os.remove(path):
        print(f"{path} is removed successfully")
    else:
        print("Unable to delete"+path)

def removeFolder(path):
    if not shutil.rmtree(path):
        print(f"{path} is removed successfully")
    else:
        print("Unable to delete"+path)

def get_file_or_folder_age(path):
    ctime = os.stat(path).st_ctime
    return ctime

if __name__ == '__main__':
    main()
    
    
