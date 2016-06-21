import cv2
from os import listdir


class FrameData:
	def __init__(self, imgRGB,imgD):
		self.imgRGB = imgRGB
		self.imgD = imgD

		
def readFrame( framePath, bfx ):
	
	rgbPath = framePath + "/image/" 
	rgbPath += listdir(rgbPath)[0]
	
	if not(bfx):
		depthPath = framePath + "/depth/" 
	else:
		depthPath = framePath + "/depth_bfx/" 
		
	depthPath += listdir(depthPath)[0]
	
	print(rgbPath)
	print(depthPath)
  
	imgRGB = cv2.imread(rgbPath);
	imgD = cv2.imread(depthPath);

	frameData = FrameData(imgRGB,imgD)
	
	return frameData;
