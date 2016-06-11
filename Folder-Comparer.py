import os
from shutil import copyfile

original_folder = os.listdir('C:/Users/Oliver/Dropbox/Shoit/Smug')

new_folder = os.listdir('images')


def find_difference(source_folder, dest_folder):
    """
    :param source_folder: A folder of images
    :param dest_folder: A folder of images
    :return: All the images that are in source_folder but not in dest_folder
    """
    difference = []
    for img in source_folder:
        if img not in dest_folder:
            difference = difference + [img]
    sync_files(difference, 'images/')


def sync_files(difference, destination):
    for i in range(len(difference)):
        copyfile(difference[i], destination)


def main():
    find_difference(original_folder, new_folder)


if __name__ == "__main__":
    main()
