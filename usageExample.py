import cv2
import SUNRGBD
import random as rand
import numpy as np

frameData = SUNRGBD.readFrame( "/home/zeni/Pictures/SUNRGBD/kv2/kinect2data/000003_2014-05-26_14-24-42_260595134347_rgbf000040-resize", True );

imgRGBWithAnnotations = np.array(frameData.imgRGB, copy=True);

for i in range(0, len(frameData.annotation2D)):

	color = [rand.randint(0,255), rand.randint(0,255), rand.randint(0,255)]
		
	cv2.fillPoly(imgRGBWithAnnotations, [frameData.annotation2D[i]], color)

for i in range(0, len(frameData.annotation2D)):	
	data = frameData.annotation2D[i];
	centroid = np.mean(data,axis=0)
	cv2.putText(imgRGBWithAnnotations, frameData.labels2D[i], (int(centroid[0]), int(centroid[1])), cv2.FONT_HERSHEY_SIMPLEX, 0.7, [0,0,0],2)
	
cv2.imshow("Detph Image", frameData.imgD);
cv2.imshow("RGB Image", frameData.imgRGB);
cv2.imshow("Annotated Image", imgRGBWithAnnotations);

cv2.waitKey(0);