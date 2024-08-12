import os


def move_file(src, dest):
    files = os.listdir(src)  # Lists all the files in the given directory
    i = 0
    for filename in files:
        base_file, ext = os.path.splitext(filename)  # Splits Filename and its Extension
        file_src = os.path.join(src, filename)
        i += 1  # Numbering for each file
        name = str(i)+"Rename"+ext  # The name to be given to each file
        os.rename(file_src, os.path.join(dest, name))


src_path = r'Paste Source Folder Path'
dest_path = r'Paste Destination Folder Path'
move_file(src_path, dest_path)
