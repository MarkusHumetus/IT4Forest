import os


def check_format_images(path):
    non_jpg_images = non_jpg_files (path)
    jpg_images= jpg_files (path)
    print (f'In the folder \n {path} \n there are {len(os.listdir(path))} files: {len(jpg_images)} .jpg images and {len(non_jpg_images)} non jpg images. \n')


def non_jpg_files(folder_path):
    '''returns a list with the names of files that are non .jpg images.
            INPUT: path to be checked
            OUTPUT: list of images that are not .jpg'''
    list_no_jpg=[]
    new_list_files= os.listdir(folder_path)
    for i in range(0, len(new_list_files)):
        if new_list_files[i].split('.')[1] !='jpg':
            list_no_jpg.append (new_list_files[i])
    return list_no_jpg

def jpg_files(folder_path):
    '''returns a list with the names of files that are .jpg images.
            INPUT: path to be checked
            OUTPUT: list of images that are not .jpg'''
    list_jpg=[]
    new_list_files= os.listdir(folder_path)
    for i in range(0, len(new_list_files)):
        if new_list_files[i].split('.')[1] =='jpg':
            list_jpg.append (new_list_files[i])
    return list_jpg