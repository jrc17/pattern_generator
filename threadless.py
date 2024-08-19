from PIL import Image

filename = "yellow.png"

with Image.open(filename) as tile:
    tile.load()
   

    # general tile for most assets
    resize_tile_2000 = tile.resize((2000,2000))
    resize_tile_2000.save("tile_2000.png")

    resize_tile_500 = tile.resize((500,500))
    resize_tile_500.save("tile_500.png")


    def tiled(tile, pattern_width, pattern_height,type):
        # make a pattern 
        filename = type+"_pattern.jpg"
        pattern = Image.new("RGB",(pattern_width,pattern_height))

        for y in range(0,pattern_height,tile.height):
            for x in range(0,pattern_width,tile.width):
                pattern.paste(tile,(x,y))
        
        pattern.save(filename)
        

 

    tiled(resize_tile_2000, 13000, 13000,"main" )
    tiled(resize_tile_500, 9038, 8148,"shirt" )
    tiled(resize_tile_500, 5400, 6374,"socks" )
    tiled(resize_tile_500, 5968, 5709,"shoes" )
    tiled(resize_tile_500, 8250, 6415,"leggings" )
    tiled(resize_tile_500, 4050, 7800,"duffle" )
    tiled(resize_tile_500, 3900, 4575,"bag" )