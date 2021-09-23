"""
    Text to Handwriting
    - Convert any text into handwriting and create image

    Author : Sudhanshu Motewar
    Date   : 24/09/21
"""

import pywhatkit

text = input("Enter text = ")
pywhatkit.text_to_handwriting(text, rgb=(0, 0, 255))
