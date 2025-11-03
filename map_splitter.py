from PIL import Image
import numpy as np
from pathlib import Path

def is_uniform_image(img):
    if img.mode != 'L':
        img = img.convert('L')
    
    # unique()関数を使用して異なる値の数を確認
    return len(np.unique(np.array(img))) == 1

root_dir = "maps"

map_names = ["hospital", "pal_office", "pal_office_7th_floor", "small_house", "small_warehouse", "willow_garage"]

crop_width, crop_height = 100,100

for map_name in map_names:
    img_path = Path(root_dir) / Path(map_name) / Path("map.pgm")
    img = Image.open(img_path)
    width, height = img.size

    for ix in range(0, width, crop_width):
        for iy in range(0, height, crop_height):
            try:
                img_crop = img.crop((ix, iy, ix+crop_width, iy+crop_height))
                if not is_uniform_image(img_crop):
                    img_crop.save(f"dataset/map/{map_name}_{ix}_{iy}.jpg")
            except:
                pass
        
