import os
import glob

# Folder paths
input_folder_path = 'images'
output_folder_path = 'output_patterns'

def get_image_filenames(folder_path):
    """
    Retrieve image file paths and their names from the specified folder.
    Creates output folders based on image names.
    """
    # Get all PNG and JPG image files
    image_files = glob.glob(os.path.join(folder_path, '*.png')) + glob.glob(os.path.join(folder_path, '*.jpg'))

    # Extract image names (without extensions)
    image_names = [os.path.splitext(os.path.basename(image))[0] for image in image_files]

    # Create a subfolder for each image name in the output folder
    for folder in image_names:
        create_folder(os.path.join(output_folder_path, folder))
   
    return image_files, image_names

def create_folder(folder_name):
    """
    Create a folder if it does not already exist.
    """
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

if __name__ == "__main__":
    # Get image files and names
    image_files, image_names = get_image_filenames(input_folder_path)
