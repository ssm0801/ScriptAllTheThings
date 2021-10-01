
'''
Convert To jpg
A quick utility that will take the input file and convert it to a .jpg version using the same base name.
Author : Hershil Piplani
Date : 1/10/21
'''
import os
import sys
from PIL import Image

if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        im = Image.open(sys.argv[1])
        target_name = sys.argv[1] + ".jpg"
        rgb_im = im.convert('RGB')
        rgb_im.save(target_name)
        print("Saved as " + target_name)
    else:
        print(sys.argv[1] + " not found")
else:
    print("Usage: test.py <file>")
 
