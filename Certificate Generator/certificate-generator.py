"""
    Certificate Generator
    - Generate thousands of certificates at just one click

    Author : Sudhanshu Motewar
    Date   : 28/03/21
"""

from PIL import Image, ImageDraw, ImageFont
import os
import csv

# font for name on certificate
font = ImageFont.truetype('merriweather-italic.ttf', 100)

# open csv file containing name
with open('names.csv') as names_file:
    names = csv.reader(names_file)
    # iterate over names
    for name in names:
        # open certificate image
        image = Image.open('certificate.jpg')
        draw = ImageDraw.Draw(image)

        # find dimensions of text on certificate
        width_of_text, height_of_text = draw.textsize(name[0], font)
        # find x coordinate of starting point of text such that it is horizontally centered
        x_coordinate = (image.width - width_of_text) / 2

        # draw the text on certificate
        draw.text((x_coordinate, 625), name[0], font=font, fill=(255, 255, 255))

        # if Output dir does not exist then create it
        if not os.path.exists('./Output'):
            os.mkdir('./Output')

        # save edited image in Output dir
        image.save("Output/{0}.jpg".format(name[0]))
