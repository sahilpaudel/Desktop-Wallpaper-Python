import urllib as urllib
from bs4 import BeautifulSoup
from PIL import Image
import cStringIO
import ctypes
from ctypes import wintypes
import os
import time

pic_url = "http://www.nationalgeographic.com/photography/photo-of-the-day"

pic_of_the_day = urllib.urlopen(pic_url)
soup = BeautifulSoup(pic_of_the_day, 'html.parser')

imgTag = soup.find('meta', property='og:image')
imgTitle = soup.find('meta', property='twitter:url')

imgTitle = imgTitle['content']
title = imgTitle.split("/")

imgName = title[-2]

src = imgTag['content']
print imgName
print src

folder = '<path-to-your-folder>'

imgPath = str(folder+imgName+'.bmp')
imgPath = os.path.abspath(imgPath);

urllib.urlretrieve(src, imgPath)
time.sleep(3)


def wall(path):
	path = os.path.abspath(path)
	SPI_SETDESKWALLPAPER = 20
	ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, path, 3)

#file = cStringIO.StringIO(urllib.urlopen(imgPath).read())
#Image.open(file).show()
wall(imgPath)

