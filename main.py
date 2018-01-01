import os
from PIL import Image

rootFolder = "D:\\work\\tmp\\photo\\"

def getImageInfo():
	
	print "calling getImageInfo"
	
	fileList = os.listdir(rootFolder)
	
	for file in fileList:
	
		fullPath = os.path.join(rootFolder, file)
	
		createDate = Image.open(fullPath)._getexif()[36867]
	
		print 'fileName: ' + createDate
	
	
if __name__ == '__main__':
	getImageInfo()