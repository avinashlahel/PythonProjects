import os
import shutil

"""Uses shutil to move files from one folder to another"""

def create_folder(folder: str, extension: str):
    """create folder if it doesnt exit"""
    path_final = os.path.join(folder, extension[1:])
    if not os.path.exists(path_final):
        os.makedirs(path_final)

    return path_final



def sort_files_per_ext(source_path: str):
    """Moves files to new location and deletes the empty folders"""
    for root_dir, sub_dirs, filenames in os.walk(source_path):
        for filename in filenames:
            file_path = os.path.join(root_dir, filename)
            ext = os.path.splitext(filename)[1]
            if ext:
                target_folder = create_folder(root_dir, ext)
                target_path = os.path.join(target_folder, filename)
                print(f'{file_path} will be moved to {target_path}')
                shutil.move(file_path, target_path)

    remove_empty_dirs(source_path)


def remove_empty_dirs(path: str):
    for root_dir, sub_dirs, filenames in os.walk(path, topdown= False):
        for curr_dir in sub_dirs:
            dir_path = os.path.join(root_dir, curr_dir)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)


if __name__ == '__main__':
    sort_files_per_ext('./test')