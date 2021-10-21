"""
    Image To Ascii Art Generator
    - Generates an ascii art of the image provided and writes it to a text file.
    Author : Rudransh Joshi (GitHub: FireHead90544)
    Date : 10th Oct. 2021
"""

import pywhatkit # pip install pywhatkit
import os

imgPath = input("Enter path to the image: ")
if os.path.exists(imgPath):
  pywhatkit.image_to_ascii_art(imgPath, 'output.txt')
else:
  print("Invalid path to image.")
