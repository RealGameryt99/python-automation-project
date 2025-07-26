import os
import shutil

def organize_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            ext = filename.split('.')[-1].lower()
            target_folder = os.path.join(folder_path, ext + "_files")

            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            shutil.move(file_path, os.path.join(target_folder, filename))

if __name__ == "__main__":
    path = input("Enter folder path to organize: ")
    organize_folder(path)
