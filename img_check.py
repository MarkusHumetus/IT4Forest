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

def to_jpg_converter(folder_path, image_name):
    '''convert images to the jpg format (remove initial format!!)
        INPUT:  path where the image is and the name of the image 
        OUTPUT: save image in the same directory and delete image with the original format''' 
    path_file = os.path.join(folder_path, image_name) 
    try: 
        im = Image.open(path_file)
        new_name= image_name.split('.')[0] +'.jpg'
        image_new_format = os.path.join(folder_path, new_name)
        im.save(image_new_format)
        im.close()
    except: 
        print (f'image {image_name} could not be transformed' )
    remove_file (folder_path, image_name) 

def remove_file (folder_path, name_file):
    ''' remove file if exists. Else, it shows a warning message
            INPUT: path where the file is and name of the file with extension (.doc, .rmd, .jpg, ....)
            OUTPUT: warning message in case any error on name or path or deleting the file if all is fine
            
            path ha d'estar amb el format correcte!!
        '''
    # Path
    path_file = os.path.join(folder_path, name_file) 
    print (path_file)
    
    # Remove the file
    if os.path.exists(path_file):
        os.remove(path_file)
        print (name_file + ' deleted!!')
    else:
        print ('No file found with such name and route!')