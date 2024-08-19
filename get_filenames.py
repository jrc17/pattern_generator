import os
import glob

# Folder containing your images
input_folder_path = 'images'
output_folder_path = "output_patterns"

def get_image_filenames(folder_path):
    # Get all PNG and JPG image files in the folder
    image_files = glob.glob(os.path.join(folder_path, '*.png')) + glob.glob(os.path.join(folder_path, '*.jpg'))

    image_names = [os.path.splitext(os.path.basename(image))[0] for image in image_files]

    for folder in image_names: 
        create_folder(os.path.join(output_folder_path,folder) )
   

    return image_files,image_names
# Print the list of filenames with extensions

def create_folder(folder_name):
     if not os.path.exists(folder_name):
          os.makedirs(folder_name)

if __name__ == "__main__":
    folder_path = 'images'
    image_files, image_names = get_image_filenames(input_folder_path)

    
 