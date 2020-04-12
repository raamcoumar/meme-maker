# A Simple Command Line Meme Generator tool using Python

Hello! I'm Ramkumar from India. I'm a PG student currently pursuing MBA. I got interested in Data Analysis and Machine Learning since it helps many business to take data driven decision. So get into this domain, I thought I would start from  taking CS50 where I can gain some knowledge about the basics of computer science.

As a final project, I have built a simple command line tool with Python that can be used to create memes!

1. The command line tool gets the images as arguments. Maximum two images can be given. (The limit will be updated in future.)

    - If the argument input has more than two images, the program displays a warning message as a meme and stops.
    - same applies when there are no inputs or when the files are not found
    
2. Due to file support constraints, the program can only support a limited number of formats. If any other file formats are given as input, the program displays a warning message as a meme and stops:

    - .jpg
    - .jpeg
    - .bmp
    - .png
    
3. Pillow package has been used for image manipulation and textWrap has been used for writing text over the image.
4. The most common font for memes is "Impact". The font has been downloaded from https://www.wfonts.com/font/impact
