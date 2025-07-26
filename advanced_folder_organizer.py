import os
import shutil

def organize_individually(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            ext = filename.split('.')[-1].lower()
            target_folder = os.path.join(folder_path, ext + "_files")

            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            shutil.move(file_path, os.path.join(target_folder, filename))

    print(f"[✓] Sorted inside: {folder_path}")

def organize_into_one(source_folders, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for folder_path in source_folders:
        if not os.path.exists(folder_path):
            print(f"[X] Not found: {folder_path}")
            continue

        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)

            if os.path.isfile(file_path):
                ext = filename.split('.')[-1].lower()
                target_folder = os.path.join(destination_folder, ext + "_files")

                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)

                shutil.move(file_path, os.path.join(target_folder, filename))

        print(f"[✓] Processed: {folder_path}")

    print(f"\n✅ All files moved and sorted in: {destination_folder}")

if __name__ == "__main__":
    print("📁 Enter the folder paths (comma-separated):")
    user_input = input(">>> ")
    folders = [f.strip() for f in user_input.split(",")]

    print("\n🔧 Choose how to sort files:")
    print("1 - Sort each folder separately")
    print("2 - Move & sort all into one target folder")

    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        for f in folders:
            if os.path.exists(f):
                organize_individually(f)
            else:
                print(f"[X] Folder not found: {f}")

    elif choice == "2":
        destination = input("📦 Enter destination folder path:\n>>> ").strip()
        organize_into_one(folders, destination)

    else:
        print("❌ Invalid choice. Please run the script again.")
