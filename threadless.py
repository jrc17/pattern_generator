import os
import shutil
from PIL import Image
from get_filenames import get_image_filenames, input_folder_path, output_folder_path

def resize(tile, w,h):
    # assuming 1:1 aspect ratio or a square
    return tile.resize((w,h))

def resize_by_percentage(tile, percentage):
    """
    Resize the image based on a given percentage while maintaining aspect ratio.
    """
    # Calculate the new dimensions based on the percentage
    new_width = int(tile.width * percentage)
    new_height = int(tile.height * percentage)
    
    return tile.resize((new_width, new_height))
 
def tiled(tile, pattern_width, pattern_height, type, name):
    """
    Create a pattern from the tile and save it in the respective folder.
    """
    # Construct filename for the pattern
    filename = os.path.join(output_folder_path, name, f"{name}_{type}_pattern.jpg")
    pattern = Image.new("RGB", (pattern_width, pattern_height))

    # Paste the tile to create the pattern
    for y in range(0, pattern_height, tile.height):
        for x in range(0, pattern_width, tile.width):
            pattern.paste(tile, (x, y))
    
    # Save the pattern image
    # pattern.show()
    pattern.save(filename)

if __name__ == "__main__":
    # Get image files and names
    image_files, image_names = get_image_filenames(input_folder_path)

    # Define pattern sizes and types
    patterns = [
       
        (9038, 8148, "shirt"),
        (5400, 6374, "socks"),
        (5968, 5709, "shoes"),
        (8250, 6415, "leggings"),
        (4050, 7800, "duffle"),
        (3900, 4575, "bag")
    ]

    for image_file, image_name in zip(image_files, image_names):
        with Image.open(image_file) as tile:
            tile.load()

            # resize_tile = tile

            if tile.width >= 4000 and tile.height >= 4000:
                resize_tile_50_percent = resize_by_percentage(tile, 0.5)  # 50% of original size
                
                tiled(resize_tile_50_percent, 13000, 13000, "main", image_name)
                
                resize_tile_25_percent = resize_by_percentage(tile, 0.25)  # 25% of original size
                                 
           
            # else: 
            #     resize_tile = tile.size

            # Create patterns for each size/type
            for w, h, pattern_type in patterns:
                tiled(resize_tile_25_percent, w, h, pattern_type, image_name)
    
            destination = os.path.join(output_folder_path, image_name, os.path.basename(image_file))
            shutil.move(image_file, destination)