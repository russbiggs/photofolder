import os
import shutil

def photo_func(input_folder, output_folder):
    in_folder = os.walk(input_folder)
    out_folder = output_folder
    if not os.path.exists(out_folder):
        os.makedirs(out_folder)
    for subdir, dirs, files in in_folder:
        if subdir == out_folder:
            pass
        for item in files:
            if item.endswith(('.jpg', '.JPG')):
                base_name = os.path.splitext(item)[0]
                out_name = out_folder + '\\' + base_name + '.jpg'
                image = os.path.join(subdir, item)
                shutil.copy2(image, out_name)