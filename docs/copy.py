import os
import shutil

def copy_md_to_txt(src_folder, dest_folder):
    print(f"Looking in source folder: {src_folder}")
    if not os.path.exists(src_folder):
        print("The source folder does not exist.")
        return
    
    print(f"Writing to destination folder: {dest_folder}")
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    for root, dirs, files in os.walk(src_folder):
        print(f"Checking directory: {root}")
        for file in files:
            print(f"Checking file: {file}")
            if file.endswith('.md'):
                src_path = os.path.join(root, file)
                rel_path = os.path.relpath(root, src_folder)
                dest_dir = os.path.join(dest_folder, rel_path)
                
                if not os.path.exists(dest_dir):
                    os.makedirs(dest_dir)

                dest_path = os.path.join(dest_dir, f"{os.path.splitext(file)[0]}.txt")
                shutil.copy2(src_path, dest_path)
                print(f"Copied {src_path} to {dest_path}")

if __name__ == "__main__":
    src_folder = r"C:\Users\evela\Desktop\ArchipelagoDomeKeeper\docs"
    dest_folder = r"docs txt"
    copy_md_to_txt(src_folder, dest_folder)
    print("Running script")
