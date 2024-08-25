from PIL import Image
import os
import shutil
from get_filenames import get_image_filenames, input_folder_path, output_folder_path

def resize_image(tile, target_size):
    """
    Resize the image so that either its width or height matches the target size (2000 pixels),
    while maintaining the aspect ratio.
    """
    original_width, original_height = tile.width, tile.height

    # Determine the scaling factor based on the larger dimension
    if original_width >= original_height:
        scaling_factor = target_size / original_width
    else:
        scaling_factor = target_size / original_height

    # Calculate new dimensions while maintaining the aspect ratio
    new_width = int(original_width * scaling_factor)
    new_height = int(original_height * scaling_factor)
    
    return tile.resize((new_width, new_height))

def tiled(tile, pattern_width, pattern_height, pattern_type, name, image_format):
    """
    Create a pattern from the tile and save it in the respective folder.
    """
    # Construct filename for the pattern
    filename = os.path.join(output_folder_path, name, f"{name}_{pattern_type}_pattern.jpg")
    pattern = Image.new("RGB", (pattern_width, pattern_height))

    # Paste the tile to create the pattern
    for y in range(0, pattern_height, tile.height):
        for x in range(0, pattern_width, tile.width):
            pattern.paste(tile, (x, y))
    
    # Save the pattern image in the appropriate format
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
            image_format = tile.format  # Get the format of the original image (e.g., "PNG" or "JPEG")

            # Resize the tile to approximately 2000px
            resize_tile_2000 = resize_image(tile, 2000)
            resize_filename_2000 = os.path.join(output_folder_path, image_name, f"{image_name}_tile_2000.{image_format.lower()}")
            resize_tile_2000.save(resize_filename_2000)

            # Resize the tile to approximately 500px
            resize_tile_500 = resize_image(tile, 500)
            resize_filename_500 = os.path.join(output_folder_path, image_name, f"{image_name}_tile_500.{image_format.lower()}")
            resize_tile_500.save(resize_filename_500)

            # Create the main pattern
            tiled(resize_tile_2000, 13000, 13000, "main", image_name, image_format)

            # Create patterns for each size/type
            for w, h, pattern_type in patterns:
                tiled(resize_tile_500, w, h, pattern_type, image_name, image_format)
    
            # Move the original image to the output folder
            destination = os.path.join(output_folder_path, image_name, os.path.basename(image_file))
            shutil.move(image_file, destination)
