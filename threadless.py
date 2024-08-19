import os
from PIL import Image
from get_filenames import get_image_filenames, input_folder_path, output_folder_path
# filename = "orange.png"

def tiled(tile, pattern_width, pattern_height,type,name):
        # make a pattern 
        filename = os.path.join(output_folder_path,name, f"{name}_{type}_pattern.jpg")
        pattern = Image.new("RGB",(pattern_width,pattern_height))

        for y in range(0,pattern_height,tile.height):
            for x in range(0,pattern_width,tile.width):
                pattern.paste(tile,(x,y))
        
        pattern.save(filename)

if  __name__ == "__main__":
    
    # folder_path = 'images'
    image_files, image_names = get_image_filenames(input_folder_path)

    for image_file, original_name in zip(image_files, image_names):
        with Image.open(image_file) as tile:
            tile.load()
        
            # filename = os.path.join(output_folder_path,original_name, f"{original_name}_{type}_pattern.jpg")
            # general tile for most assets
            resize_tile_2000 = tile.resize((2000,2000))
            resize_tile_2000.save(os.path.join(output_folder_path,original_name,f"{original_name}_tile_2000.png"))

            resize_tile_500 = tile.resize((500,500))
            resize_tile_500.save(os.path.join(output_folder_path,original_name,f"{original_name}_tile_500.png"))
        

            tiled(resize_tile_2000, 13000, 13000,"main",original_name )

        # for now this works as the code is small 
        #if i want to expand it , it might be better to generilize it or something and add metadata
            
            patterns = [(9038, 8148,"shirt"),
                        ( 5400, 6374,"socks"),
                        (5968, 5709,"shoes"),
                        (8250, 6415,"leggings"),
                        (4050, 7800,"duffle"),
                        (3900, 4575,"bag")
                        ]

            for w,h,type in patterns: tiled(resize_tile_500, w,h,type,original_name)

