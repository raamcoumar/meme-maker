from PIL import Image, ImageDraw, ImageFont
import textwrap
import sys


def check(files):
    """
    files : List of files

    For now, the program can only accept the following formats:
    .jpg, .jpeg, .png, .bmp

    Returns True of the file format belongs the above mentioned list.
    """
    for file in files:
        try:
            Image.open(file)
        except FileNotFoundError:
            Image.open('files/noFiles.png').show()
            exit()

        file_format = file.split('.')[-1]
        if file_format not in ['jpg','jpeg','png','bmp']:
            Image.open('files/drake.png').show()
            print ("Try again with supported file formats recommended by Drake")
            exit()

    return True

def arrangeTwoImages(topImage, bottomImage):
    """
    Arranges two images vertically
    """
    firstImage = Image.open(topImage)
    firstImageWidth = firstImage.size[0]
    firstImageHeight = firstImage.size[1]

    secondImage = Image.open(bottomImage)
    secondImageWidth = secondImage.size[0]
    secondImageHeight = secondImage.size[1]

    newLayoutWidth = max(firstImageWidth, secondImageWidth)
    newLayoutHeight = firstImageHeight+secondImageHeight
    newLayout = Image.new('RGBA',(newLayoutWidth,newLayoutHeight),'white')
    newLayout.paste(firstImage,(0,0))
    newLayout.paste(secondImage,(0,firstImageHeight))
    newImage = newLayout.crop((0,0,firstImageWidth,newLayoutHeight))

    return newImage

def drawMeme(template):
    """
    template : the image template

    Returns an image object of the finished meme
    """
    meme = template
    meme_width, meme_height = template.size

    #Load Font
    font = ImageFont.truetype(font = './files/impact.ttf',size = int(meme_height/10))

    #Text
    top_text = input('Top text for your meme: ')
    bottom_text = input('Bottom text for your meme: ')

    # getting the width and height from 'font'
    char_width, char_height = font.getsize('A')

    # set limit for the number of characters per line
    char_per_line = meme_width // char_width

    top_text = textwrap.wrap(top_text.upper(), width = char_per_line)
    bottom_text = textwrap.wrap(bottom_text.upper(), width = char_per_line)

    draw = ImageDraw.Draw(meme)

    y = 10 #y-axis postion for the top text
    for line in top_text:
        line_width, line_height = font.getsize(line)
        x = (meme_width - line_width)/2
        draw.text((x, y), line, fill = 'white', font = font)
        y += line_height

    y = meme_height - char_height * len(bottom_text) - 15 # y-axis position for bottom text
    for line in bottom_text:
        line_width, line_height = font.getsize(line)
        x = (meme_width - line_width)/2
        draw.text((x, y), line, fill = 'white', font = font)
        y += line_height

    meme_name = input('Any name for your new meme? ')
    if len(meme_name) > 0:
        meme.save(f'{meme_name}.png')
    else:
        meme.save('FreshlyBrewedMeme.png')

    meme.show()


if __name__ == "__main__":
    files = sys.argv[1:] #Loading the images

    if len(files) == 0:
        Image.open('files/empty.jpg').show()

    elif len(files) == 1:
        if check(files):
            template = Image.open(files[0])
            drawMeme(template)

    elif len(files) == 2:
        if check(files):
            template = arrangeTwoImages(files[0],files[1])
            drawMeme(template)
    else:
        Image.open('files/twoImagesOnly.png').show()
